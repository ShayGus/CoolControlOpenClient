sudo rm -rf cool_open_client/client
cp -R swagger_client/cool_open_client/client cool_open_client/
rm -rf dist
rm -rf *.egg-info
python -m build
# pip install dist/cool_open_client-*.whl --force-reinstall