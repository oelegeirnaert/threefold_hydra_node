# Proof Of Concept: Can we get output from Hydra Daemon into a webpage on Threefold?

## Project Setup
cd /opt

mkdir hydra_threefold

cd hydra_threefold
git clone https://github.com/oelegeirnaert/threefold_hydra_node.git

python3 -m venv venv
source venv/bin/activate

pip install falcon gunicorn

## Run the WebApp
gunicorn --reload hydra_node:app -b 127.0.0.1:8089
