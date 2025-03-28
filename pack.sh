#!/bin/bash
# shellcheck disable=SC2317

# Repository root
ROOTDIR=$( cd -- "$( dirname -- "$0" )/.." &> /dev/null && pwd )

# Vendor functions
prepackall() { return 0; }
packall() { return 0; }
postpackall() { return 0; }

# Convenience functions
checkerror() {
    if [ "$1" != 0 ]
    then
        printf "%s - Error %s\n" "$2" "$1" >&2
        exit "$1"
    fi
}

# Sourcing the vendor script
export VENDOR_ERRORCODE=0
source "$ROOTDIR/vnd/vendor.sh"
checkerror $? "Failed to source the vendor script"

# Vendor error function
checkvendorerror() {
    if [ $VENDOR_ERRORCODE == 0 ]
    then
        export VENDOR_ERRORCODE=$1
    fi
}

# Run any vendor actions before packing
prepackall "$@"
checkerror $VENDOR_ERRORCODE "Failed to run pre-packing function from the vendor"

# Pack all artifacts using vendor action
packall "$@"
checkerror $VENDOR_ERRORCODE "Failed to run artifact packing function from the vendor"

# Run any vendor actions after packing
postpackall "$@"
checkerror $VENDOR_ERRORCODE "Failed to run post-packing function from the vendor"

# Inform success
echo Pack successful.
