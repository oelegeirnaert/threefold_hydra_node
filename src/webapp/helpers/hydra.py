import os
import socket
import subprocess
import json


def get_cli_info(hydra_cli_argument):
    fake_response = False

    try:
        p = (
            subprocess.check_output("hydra-cli {0}".format(hydra_cli_argument).split())
            .decode("utf8")
            .replace("'", '"')
        )
        data = json.loads(p)
        s = json.dumps(data, indent=4, sort_keys=True)
        return s
    except Exception as e:
        print(e)

    if fake_response:
        hydra_cli_argument = hydra_cli_argument.lower()
        if hydra_cli_argument == "getwalletinfo":
            return {
                "balance": 0.0,
                "hdseedid": "247604ba520b6f1fab52e344073e419c961610cb",
                "immature_balance": 0.0,
                "keypoololdest": 1652280696,
                "keypoolsize": 1000,
                "keypoolsize_hd_internal": 1000,
                "paytxfee": 0.0,
                "private_keys_enabled": True,
                "stake": 0.0,
                "txcount": 0,
                "unconfirmed_balance": 0.0,
                "walletname": "",
                "walletversion": 169900,
            }

        if hydra_cli_argument == "getstakinginfo":
            return {
                "difficulty": 1974018.687392613,
                "enabled": True,
                "errors": "",
                "expectedtime": 0,
                "netstakeweight": 1187883547515220,
                "pooledtx": 0,
                "search-interval": 0,
                "staking": False,
                "weight": 0,
            }

        if hydra_cli_argument == "getinfo":
            return {
                "balance": 0.0,
                "blocks": 0,
                "burnedcoins": "0.0",
                "connections": 1,
                "difficulty": {"proof-of-stake": 1.52587890625e-05, "proof-of-work": 1.52587890625e-05},
                "errors": "",
                "keypoololdest": 1652280696,
                "keypoolsize": 2000,
                "locked": {
                    "chunks_free": 2,
                    "chunks_used": 2002,
                    "free": 1408,
                    "locked": 65536,
                    "total": 65536,
                    "used": 64128,
                },
                "moneysupply": "0.0",
                "protocolversion": 70017,
                "proxy": "",
                "relayfee": 0.004,
                "stake": 0.0,
                "testnet": False,
                "timeoffset": 0,
                "version": 180504,
                "walletversion": 169900,
            }
        return None


def stop_server():
    get_cli_info("stop")
    print("STOPPING SERVER")


def start_server():
    print("START SERVER")
