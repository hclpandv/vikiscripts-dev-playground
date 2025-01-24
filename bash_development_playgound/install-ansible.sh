#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive
apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y
apt-get install -y software-properties-common
apt-get install -y python3-pip
pip3 install ansible
