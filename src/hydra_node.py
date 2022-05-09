import falcon
import os
import socket
import subprocess


class IndexResource:
    def get_staking_info(self):
        try:
            p = subprocess.Popen("hydra-cli getstakinginfo", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            return p.communicate()
        except Exception as e:
            return "Hydra Application not found."

    def on_get(self, req, resp):
        """Handle GET requests."""
        hydra_info = {
            "wallet_address": os.environ.get(
                "WALLET_ADDRESS", "Cannot load your wallet address from the environment variables."
            ),
            "staking_info": str(self.get_staking_info()),
        }

        resp.media = hydra_info


app = falcon.App()
app.add_route("/", IndexResource())
