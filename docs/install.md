# Proof Of Concept: Can we get output from Hydra Daemon into a webpage on Threefold?

## Project Setup

- [x] Currently using Falcon, but will be migrated to Flask. (As we have found a repo that is already using the WebAuthn with flask.)

~~~
cd /opt

mkdir hydra_threefold

cd hydra_threefold
git clone https://github.com/oelegeirnaert/threefold_hydra_node.git

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
~~~


## Run the WebApp

~~~
./start_server.sh
~~~

## Application ToDo's:
- [x] Create POC WebApp in Flask
- [x] Create new docker image where Hydra daemon is included
- [x] Add flask to docker image
- [x] Get two services running in parallel: Hydra Daemon & Webserver
- [ ] Make flask production ready
- [x] Update entry point (.sh script) to start hydra and gunicorn (IMPROVEMENT NEEDED)
- [ ] Create new FLIST from Docker (WIP)
- [ ] Protect against DDOS attacks
- [ ] Setup HTTPS
- [x] Show Time (important for Blockchain)
- [x] Make a page for logs (/root/.hydra/debug.log)
- [ ] Make webapp updateable
