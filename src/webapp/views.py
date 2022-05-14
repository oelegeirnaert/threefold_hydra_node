from typing import Dict
import json
import os
import socket
import subprocess
from time import sleep

from flask import Flask, render_template, request, redirect

from webapp.helpers import hydra, threefold
from webapp.models import Credential, UserAccount

from webauthn import (
    generate_registration_options,
    verify_registration_response,
    generate_authentication_options,
    verify_authentication_response,
    options_to_json,
)
from webauthn.helpers.structs import (
    AuthenticatorSelectionCriteria,
    UserVerificationRequirement,
    RegistrationCredential,
    AuthenticationCredential,
)
from webauthn.helpers.cose import COSEAlgorithmIdentifier


# Create our Flask app
app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)


################
#
# RP Configuration
#
################

socket_hostname = socket.gethostname()
rp_id = "localhost"
origin = f"http://localhost:8001"
rp_name = "Sample RP"
user_id = "some_random_user_identifier_like_a_uuid"
username = f"your.name@{rp_id}"
print(f"User ID: {user_id}")
print(f"Username: {username}")
print(f"{hydra.get_cli_info('getinfo')}")
print(f"{threefold.get_env_value('APP_VERSION')}")

# A simple way to persist credentials by user ID
in_memory_db: Dict[str, UserAccount] = {}

# Register our sample user
in_memory_db[user_id] = UserAccount(
    id=user_id,
    username=username,
    credentials=[],
)

# Passwordless assumes you're able to identify the user before performing registration or
# authentication
logged_in_user_id = user_id

# A simple way to persist challenges until response verification
current_registration_challenge = None
current_authentication_challenge = None


################
#
# Views
#
################


@app.route("/")
def index():
    context = {
        "username": username,
        "fake_response": hydra.get_fake_response(),
        "app_name": threefold.get_env_value("WEBAPP_NAME"),
        "app_version": threefold.get_env_value("WEBAPP_VERSION"),
        "general_info": hydra.get_cli_info("getinfo"),
        "wallet_info": hydra.get_cli_info("getwalletinfo"),
        "staking_info": hydra.get_cli_info("getstakinginfo"),
        "public_ssh_key": threefold.get_env_value("SSH_KEY"),
        "server_epoch_time": threefold.get_server_epoch_time(),
    }
    return render_template("index.html", **context)


################
#
# Registration
#
################


@app.route("/generate-registration-options", methods=["GET"])
def handler_generate_registration_options():
    global current_registration_challenge
    global logged_in_user_id

    user = in_memory_db[logged_in_user_id]

    options = generate_registration_options(
        rp_id=rp_id,
        rp_name=rp_name,
        user_id=user.id,
        user_name=user.username,
        exclude_credentials=[
            {"id": cred.id, "transports": cred.transports, "type": "public-key"} for cred in user.credentials
        ],
        authenticator_selection=AuthenticatorSelectionCriteria(
            user_verification=UserVerificationRequirement.REQUIRED
        ),
        supported_pub_key_algs=[
            COSEAlgorithmIdentifier.ECDSA_SHA_256,
            COSEAlgorithmIdentifier.RSASSA_PKCS1_v1_5_SHA_256,
        ],
    )

    current_registration_challenge = options.challenge

    return options_to_json(options)


@app.route("/verify-registration-response", methods=["POST"])
def handler_verify_registration_response():
    global current_registration_challenge
    global logged_in_user_id

    body = request.get_data()

    try:
        credential = RegistrationCredential.parse_raw(body)
        verification = verify_registration_response(
            credential=credential,
            expected_challenge=current_registration_challenge,
            expected_rp_id=rp_id,
            expected_origin=origin,
        )
    except Exception as err:
        return {"verified": False, "msg": str(err), "status": 400}

    user = in_memory_db[logged_in_user_id]

    new_credential = Credential(
        id=verification.credential_id,
        public_key=verification.credential_public_key,
        sign_count=verification.sign_count,
        transports=json.loads(body).get("transports", []),
    )

    user.credentials.append(new_credential)

    return {"verified": True}


################
#
# Authentication
#
################


@app.route("/generate-authentication-options", methods=["GET"])
def handler_generate_authentication_options():
    global current_authentication_challenge
    global logged_in_user_id

    user = in_memory_db[logged_in_user_id]

    options = generate_authentication_options(
        rp_id=rp_id,
        allow_credentials=[
            {"type": "public-key", "id": cred.id, "transports": cred.transports} for cred in user.credentials
        ],
        user_verification=UserVerificationRequirement.REQUIRED,
    )

    current_authentication_challenge = options.challenge

    return options_to_json(options)


@app.route("/verify-authentication-response", methods=["POST"])
def hander_verify_authentication_response():
    global current_authentication_challenge
    global logged_in_user_id

    body = request.get_data()

    try:
        credential = AuthenticationCredential.parse_raw(body)

        # Find the user's corresponding public key
        user = in_memory_db[logged_in_user_id]
        user_credential = None
        for _cred in user.credentials:
            if _cred.id == credential.raw_id:
                user_credential = _cred

        if user_credential is None:
            raise Exception("Could not find corresponding public key in DB")

        # Verify the assertion
        verification = verify_authentication_response(
            credential=credential,
            expected_challenge=current_authentication_challenge,
            expected_rp_id=rp_id,
            expected_origin=origin,
            credential_public_key=user_credential.public_key,
            credential_current_sign_count=user_credential.sign_count,
            require_user_verification=True,
        )
    except Exception as err:
        return {"verified": False, "msg": str(err), "status": 400}

    # Update our credential's sign count to what the authenticator says it is now
    user_credential.sign_count = verification.new_sign_count

    return {"verified": True}


@app.route("/stop-server", methods=["GET"])
def stop_hydra_server():
    hydra.stop_server()
    return redirect("/", code=302)


@app.route("/start-server", methods=["GET"])
def start_hydra_server():
    hydra.start_server()
    return redirect("/", code=302)


@app.route("/stream")
def stream():
    def generate():
        with open("/root/.hydra/debug.log") as f:
            while True:
                yield f.read()
                sleep(1)

    return app.response_class(generate(), mimetype="text/plain")
