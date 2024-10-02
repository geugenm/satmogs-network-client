# OpenAPI Python Client for SATNOGS Network

This documentation describes how to automatically generate a Python client for the SATNOGS Network API using the `openapi-python-client` tool.


## Installation

To get started, you need to install the [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client/tree/main). 
You can do this using `pip`:

```bash
pip install openapi-python-client
```

## Generating the Client
Once you have installed the client, you can generate the Python client by running the following command:

```bash
openapi-python-client generate --path openapi3_0.json 
```

## Note 
The `openapi3_0.yml` is taken from one of the artifacts of [satnogs-network](https://gitlab.com/librespacefoundation/satnogs/satnogs-network), job with `api`, like `#12345678: api`

Converted to json via [swagger](https://editor-next.swagger.io/)

The only change made is in [observations_list](../api/client/api/observations/observations_list.py)

P.S. Satnogs, follow freaking standards to avoid wasting time!!!