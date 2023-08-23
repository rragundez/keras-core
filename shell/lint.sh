#!/bin/bash -e

base_dir=$(dirname $(dirname $0))
targets="${base_dir}/*.py ${base_dir}/keras_core/"

isort --check ${targets}
black --check ${targets}
flake8 ${targets}
