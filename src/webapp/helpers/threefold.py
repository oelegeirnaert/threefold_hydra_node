import os
import socket
import subprocess
import time


def get_env_value(from_key):
    return os.environ.get(from_key.upper())


def get_server_epoch_time():
    return int(time.time()) * 1000
