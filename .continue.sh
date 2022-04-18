#!/bin/bash

set -eo pipefail

../xpulumi/.venv/bin/python -m xpulumi --tb init-env "$@"
