#!/bin/bash

rm -rf cool_open_client/client
cp -R swagger_client/cool_open_client/client cool_open_client/
sudo rm -rf dist
sudo rm -rf *.egg-info
python -Im build
# pip install dist/cool_open_client-*.whl --force-reinstall