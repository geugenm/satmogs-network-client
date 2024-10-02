# OpenAPI Python Client for SATNOGS Network

API accessed form [here](https://network.satnogs.org/api/)

More about [API](https://docs.satnogs.org/projects/satnogs-network/en/stable/)

## Installation:

1. Clone this repo
2. Go to the root of the repo
3. run `pip install .` or `python ./setup.py install`

## Usage:

Insert desired data to `config.ini`

The example of `config.ini`:
```ini
[API]
base_url = https://network.satnogs.org
token = <your_api_key>
satellite_norad_cat_id = 44420
start_date = 2020-01-01
end_date = 2020-03-01

[Paths]
cache_dir = cache
```

To obtain your API key, go to [https://network.satnogs.org](https://network.satnogs.org), register your account and get your API key in Profile -> Dashboard -> API Key.

This documentation describes how to automatically generate a Python client for the SATNOGS Network API using the `openapi-python-client` tool.

## Generating the Client

To get started, you need to install the [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client/tree/main). 
You can do this using `pip`:

```bash
pip install openapi-python-client
```

Once you have installed the client, you can generate the Python client by running the following command:

```bash
openapi-python-client generate --path openapi3_0.json
```

## Note 
The `openapi3_0.yml` is taken from one of the artifacts of [satnogs-network](https://gitlab.com/librespacefoundation/satnogs/satnogs-network), job with `api`, like `#12345678: api`

Converted to json via [swagger](https://editor-next.swagger.io/)

The only change made is in [observations_list](../api/client/api/observations/observations_list.py)

P.S. Satnogs, follow freaking standards to avoid wasting time!!!

License :
-------
[![license](https://img.shields.io/github/license/deckbsd/glouton-satnogs-data-downloader)](LICENSE)