import os
import socket
import subprocess


def get_wallet_info():
    try:
        p = subprocess.Popen("hydra-cli getwalletinfo", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p.communicate()
    except Exception as e:
        return "Hydra Application not found."


def get_staking_info():
    try:
        p = subprocess.Popen("hydra-cli getstakinginfo", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p.communicate()
    except Exception as e:
        return "Hydra Application not found."
