import os
import socket
import subprocess
import json


def get_cli_info(hydra_cli_argument):
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
        return "Hydra Application not found."
