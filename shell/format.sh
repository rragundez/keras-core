#!/bin/bash -e

base_dir=$(dirname $(dirname $0))
targets="${base_dir}/*.py ${base_dir}/keras_core/ ${base_dir}/benchmarks/"

isort ${targets}
black ${targets}
flake8 ${targets}
