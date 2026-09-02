#!/bin/bash

docker exec -it homeassistant bash
wget -O - https://get.hacs.xyz | bash -
