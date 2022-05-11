# Dockerfile based on https://github.com/Hydra-Chain/community-tools/blob/main/node-docker/Dockerfile

FROM ubuntu:20.04

# Environment Variables
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y
RUN apt upgrade -y
RUN apt install -y tzdata
RUN apt -y install unzip build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils git cmake libboost-all-dev libgmp3-dev libzmq3-dev wget
RUN apt -y install software-properties-common

# install leveldb
RUN mkdir /root/dev
WORKDIR /root/dev
RUN wget -N http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz
RUN tar -xvf db-4.8.30.NC.tar.gz
RUN sed -i s/__atomic_compare_exchange/__atomic_compare_exchange_db/g db-4.8.30.NC/dbinc/atomic.h
RUN ./db-4.8.30.NC/dist/configure --enable-cxx --prefix=/usr/local
RUN make && make install

RUN apt update -y
RUN apt-get -y install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libprotobuf-dev protobuf-compiler qrencode git python3.8-venv nano

# set timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# get hydra
WORKDIR /root
RUN mkdir -p Hydra
WORKDIR /root/Hydra

RUN wget -N https://github.com/Hydra-Chain/node/releases/download/hydra_v0.18.5.4/hydra-0.18.5.4-ubuntu20.04-x86_64-gnu.zip
RUN unzip -o hydra-0.18.5.4-ubuntu20.04-x86_64-gnu.zip
RUN mkdir ~/.hydra
RUN cp hydra.conf ~/.hydra/

# ports to expose
ARG TESTNET_PORT=1334
ARG MAINNET_PORT=3338
EXPOSE $TESTNET_PORT
EXPOSE $MAINNET_PORT

COPY ./docker_entry.sh /root/Hydra/bin/docker_entry.sh

ENV PATH="/root/Hydra/bin:${PATH}"

WORKDIR /root/Hydra/bin
# RUN chmod +x ./run-hydrad.sh
# RUN chmod +x ./run-flask.sh
#CMD ["./run-hydrad.sh"]

# Added by Oele Geirnaert
WORKDIR /opt/
RUN mkdir hydra_threefold
RUN cd hydra_threefold

# RUN git clone https://github.com/oelegeirnaert/threefold_hydra_node.git

ENV VIRTUAL_ENV=/opt/hydra_threefold/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#Expose 5000 for Flask
EXPOSE 5000

# ENTRYPOINT ["/bin/sh", "-c" , "run-flask.sh && run-hydrad.sh"]

ENV WEBAPP_NAME=Thydra
ENV WEBAPP_VERSION=1.1
ENV REPO_URL=https://github.com/oelegeirnaert/threefold_hydra_node.git
ENV REPO_DESTINATION=/opt/hydra_threefold/threefold_hydra_node
ENV PIP_REQUIRMENTS_FILE=$REPO_DESTINATION/src/requirements.txt
ENV FLASK_APP=$REPO_DESTINATION/src/webapp/views.py
ENV FLASK_ENV=development
ENV FLASK_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

ENTRYPOINT ["/bin/sh", "-c" , "docker_entry.sh"]
