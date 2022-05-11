#!/bin/bash

FLASK_ENV=development FLASK_APP=flask_hydra_node:app /opt/hydra_threefold/venv/bin/flask run -h 0.0.0.0
