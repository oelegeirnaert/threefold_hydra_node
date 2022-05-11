import os
import socket
import subprocess
import json


def get_cli_info(hydra_cli_argument):
    try:
        p = (
            subprocess.check_output("hydra-cli -{0}".format(hydra_cli_argument).split())
            .decode("utf8")
            .replace("'", '"')
        )
        data = json.loads(p)
        s = json.dumps(data, indent=4, sort_keys=True)
        return s
    except Exception as e:
        return "Hydra Application not found."


def get_wallet_info():
    try:
        p = subprocess.Popen("hydra-cli -getwalletinfo", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p.communicate()
    except Exception as e:
        return "Hydra Application not found."


def get_staking_info():
    try:
        p = subprocess.Popen("hydra-cli -getstakinginfo", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p.communicate()
    except Exception as e:
        return "Hydra Application not found."
