#!/bin/bash
# Generate Python client from OpenAPI spec using OpenAPI Generator
# OpenAPI Generator is the modern, actively-maintained successor to Swagger Codegen

sudo rm -rf swagger_client
docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i /local/open_api/CoolAPI-resolved.yaml \
  -g python \
  -o /local/swagger_client \
  --package-name cool_open_client.client \
  --library asyncio
rm -rf cool_open_client/client
cp -R swagger_client/cool_open_client/client cool_open_client/
