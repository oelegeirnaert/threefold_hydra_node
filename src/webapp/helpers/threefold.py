import os
import socket
import subprocess


def get_env_value(from_key):
    return os.environ.get(from_key.upper())
