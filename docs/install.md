# Proof Of Concept: Can we get output from Hydra Daemon into a webpage on Threefold?

## Project Setup

~~~
cd /opt

mkdir hydra_threefold

cd hydra_threefold
git clone https://github.com/oelegeirnaert/threefold_hydra_node.git

python3 -m venv venv
source venv/bin/activate

pip install falcon gunicorn
~~~


## Run the WebApp

~~~
gunicorn --reload hydra_node:app -b 127.0.0.1:8089
~~~

## Application ToDo's:
- [ ] Create new docker image where Hydra daemon is included
- [ ] Add falcon and gunicorn to the same docker image
- [ ] Update entry point (.sh script) to start hydra and gunicorn
- [ ] Create new FLIST from Docker

## Research ToDo's:
- [ ] Server HTML pages from Falcon

Flask Demo: https://github.com/duo-labs/duo-blog-going-passwordless-with-py-webauthn/blob/main/src/app.py
