#!/bin/bash
# shellcheck disable=SC2317

# Repository root
ROOTDIR=$( cd -- "$( dirname -- "$0" )/.." &> /dev/null && pwd )

# Vendor functions
prelocalize() { return 0; }
localize() { return 0; }
postlocalize() { return 0; }

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

# Run any vendor actions before localization
prelocalize "$@"
checkerror $VENDOR_ERRORCODE "Failed to run pre-localization function from the vendor"

# Localize all dependencies using vendor action
localize "$@"
checkerror $VENDOR_ERRORCODE "Failed to run localization function from the vendor"

# Run any vendor actions after localization
postlocalize "$@"
checkerror $VENDOR_ERRORCODE "Failed to run post-localization function from the vendor"

# Inform success
echo Localization successful.
