# crypto-trade-test

This repository contains my experiments with automated crypto trading.

# Setup Steps
1. Create an account on bitfinex or similar. Set up a (sub)account with paper money and create your API keys following the bitfinex documentation.
2. Experiment with example python code to interact with the trading platform. Read the API documentation.

# Some notes on REST APIs
Unique URIs (resource identifiers): URIs differentiate different types of resources.
POST : create resource
GET: Read
Put : Modify
Delete: remove resource

CRUD: Create/Read/Update/Delete

REST API codes

200 - Success

400 - something wrong with the request

500 - something wrong with the server

Idempotent - Making multiple requests is same as making a single request. POST is not idempotent.
REST APIs are stateless, every API request is independent from each other.
REST allows data transfer in XML, JSON and HTML.

# Some notes on Websockets
Useful for broacasting services.
