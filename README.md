# Let's get a Hydra node running on Threefold grid

Our mission is to make an easy onboarding process to have a Hydra Node running on Threefold.
The whole process should be as simple as possible and fully documented.

The next step is to create a simple WebApplication that will be deployed to a virtual machine that also contains the Hydra Daemon.
This WebApplication will accept user input, and send it to the Hydra Daemon

## Official pages
- Hydra Chain: https://hydrachain.org/
- ThreeFold: https://threefold.io/

## Proof of concept: Can we run a Hydra node on Threefold?
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
  - [ ] Authenthication method?
    As we want to make the webapp as secure as possible, I was thinking to include a new standard of authentication, which is called WebAuthN (https://webauthn.io/) where you'll create a public/private key with a second device, which may be your mobile phone.
    The website webauthn.io allows you to test this new standard. It's a standard defined by the Web consortium, so in the feature all browsers are supposed to implement this
      
## WebApp
- [ ] Load environments variables
  - [ ] Which? to be decided

## Questions
- [ ] How to secure against DDOS attacks?
- [ ] How will we call our super fancy Hydra node running on ThreeFold?

# How I see it?
So, as a first step: we'll need to create a new docker with our new webapplication and hydra daemon > convert it to a new FLIST.
Afterwards, this FLIST can be used to deploy a new VM with a public ip address.
As this webapplication will have public ip address, it should be accessible after having your VM deployed.
The webapplication will contain a mechanism to detect if it's the first launch.
If it's the first launch, the webapplication will ask for new private/public keys (and probably via the new WebAuthN method) and save it into the environment variables of the virtual machine.
Next, you'll need to authenticate with this new credentials into the webappliation and provide all the info needed to have a Hydra node running with delegated staking.

After each save of the webapplication, the information needs to be sent to the Hydra daemon.
A mechanism to read the node information should also be created to show it in our webapplicaction.
