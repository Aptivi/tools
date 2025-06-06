#!/bin/bash
# shellcheck disable=SC2317

# Script root
ROOTDIR=$( cd -- "$( dirname -- "$0" )" &> /dev/null && pwd )
bash "$ROOTDIR/common.sh" increment "$@"
