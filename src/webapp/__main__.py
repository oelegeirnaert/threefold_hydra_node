from helpers import threefold, hydra

################
#
# RP Configuration
#
################

rp_id = "localhost"
origin = "http://localhost:5000"
rp_name = "Sample RP"
user_id = "some_random_user_identifier_like_a_uuid"
username = f"your.name@{rp_id}"
print(f"User ID: {user_id}")
print(f"Username: {username}")
print(f"{hydra.get_staking_info()}")
print(f"{threefold.get_env_value('wallet_address')}")

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
