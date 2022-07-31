sudo rm -rf swagger_client
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3 generate \
 -i /local/open_api/CoolAPI-resolved.yaml -l python -o /local/swagger_client \
 -DpackageName=cool_open_client.client --library asyncio
rm -rf cool_open_client/client
cp -R swagger_client/cool_open_client/client cool_open_client/
