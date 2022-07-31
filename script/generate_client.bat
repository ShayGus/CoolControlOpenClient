rmdir swagger_client /S /Q
docker run --rm -v %cd%:/local swaggerapi/swagger-codegen-cli-v3^
        generate -i /local/open_api/CoolAPI-resolved.yaml^
        -l python -o /local/swagger_client^
        -DpackageName=cool_open_client.client --library asyncio
rmdir cool_open_client\client /S /Q
mkdir cool_open_client\client
xcopy swagger_client\cool_open_client\client cool_open_client\client /E /Y /H
