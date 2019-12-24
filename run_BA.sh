#!/bin/bash

set -eux

export LC_ALL=en_US.UTF-8
script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
PIPFILE=$script_dir/Pipfile
export PIPENV_PIPFILE=$(cd $(dirname $PIPFILE) && pwd)/$(basename $PIPFILE) # get abspath
pipenv run python $script_dir/BA.py $@

