#!/bin/bash
# shellcheck disable=SC2317

# Repository root
ROOTDIR=$( cd -- "$( dirname -- "$0" )/.." &> /dev/null && pwd )

# Vendor functions
prepushall() { return 0; }
pushall() { return 0; }
postpushall() { return 0; }

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

# Run any vendor actions before pushing
prepushall "$@"
checkerror $VENDOR_ERRORCODE "Failed to run pre-pushing function from the vendor"

# Push all artifacts using vendor action
pushall "$@"
checkerror $VENDOR_ERRORCODE "Failed to run artifact pushing function from the vendor"

# Run any vendor actions after pushing
postpushall "$@"
checkerror $VENDOR_ERRORCODE "Failed to run post-pushing function from the vendor"

# Inform success
echo Push successful.
