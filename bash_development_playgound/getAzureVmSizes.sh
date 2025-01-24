#!/usr/bin/env bash

MAGENTA=$(tput setaf 5)
POWDER_BLUE=$(tput setaf 153)
NORMAL=$(tput sgr0)

LOCATION="${1:-eastasia}"
echo "${POWDER_BLUE}Showing all VM Sizes in Location : ${LOCATION} .. ${NORMAL}"
echo "${MAGENTA}Default Location is eastasia. Pass location as 1st Param to change. ${NORMAL}"
az vm list-sizes -l ${LOCATION} -o table --query "[].name"