# Let's get a Hydra node running on Threefold grid

Proof of concept: Can we run a Hydra node on Threefold?
- Create a profile on https://play.grid.tf/
- Create a new VM:
  - FList: https://hub.grid.tf/weynandkuijpers.3bot/hydra.flist 
    - Converted docker https://hub.docker.com/r/locktrip/hydra-node image via https://hub.grid.tf/ 
    - Sourcecode docker: https://github.com/Hydra-Chain/community-tools/blob/main/node-docker/Dockerfile
  - Entry Point: /root/Hydra/bin/run-hydrad.sh
  - Root File System (GB): 5
  - CPU: 2
  - Memory (MB): 2048
  - Public IPV4 address

- [x] Proof of concept succeeded - https://forum.threefold.io/t/grant-suggestion-deploy-a-hydra-node-on-tfgrid/2493/25

Next poc:
- [ ] Create a simple WebApp that can communicate with the Hydra Daemon

# Roadmap WebApp POC
- [ ] Create new docker file
  - [ ] Install the Hydra Daemon
  - [ ] Install the Webserver for remote management of the Hydra node
  - [ ] Authenthication method? To be decided but preferably SSH key pair (Can https://webauthn.io/ be an option?)

## WebApp
- [ ] Load environments variables
  - [ ] Which? to be decided

## Questions
- [ ] How to secure against DDOS attacks?

