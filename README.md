# [![RIPE API](res/logo.png)](https://docs.platforme.com)

The Python based RIPE Core API client.

## Configuration

| Name | Type | Description |
| ----- | ----- | ----- |
| **RIPE_BASE_URL** | `str` | The base URL to be used in the remote API calls (defaults to `http://localhost/api/`). |
| **RIPE_USERNAME** | `str` | The username to be used in the authenticated remote calls (defaults to `None`). |
| **RIPE_PASSWORD** | `str` | The password to be used in the authenticated remote calls (defaults to `None`). |
| **RIPE_SECRET_KEY** | `str` | The secret key to be used for stateless (no session) authentication (defaults to `None`). |

## License

RIPE API is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://travis-ci.org/ripe-tech/ripe-api.svg?branch=master)](https://travis-ci.org/ripe-tech/ripe-api)
[![Coverage Status](https://coveralls.io/repos/ripe-tech/ripe-api/badge.svg?branch=master)](https://coveralls.io/r/ripe-tech/ripe-api?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/ripe-api.svg)](https://pypi.python.org/pypi/ripe-api)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
