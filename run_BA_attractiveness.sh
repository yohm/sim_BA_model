#!/bin/bash

set -eux

script_dir=$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)
PIPFILE=$script_dir/Pipfile
export PIPENV_PIPFILE=$(cd $(dirname $PIPFILE) && pwd)/$(basename $PIPFILE) # get abspath
pipenv run papermill $script_dir/BA_attractiveness.ipynb out.ipynb -f _input.json
pipenv run jupyter nbconvert --to html out.ipynb
