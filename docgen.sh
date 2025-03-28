#!/bin/bash

# Repository root
ROOTDIR=$( cd -- "$( dirname -- "$0" )/.." &> /dev/null && pwd )

# Vendor functions
predocgenerate() { return 0; }
docgenerate() { return 0; }
postdocgenerate() { return 0; }

# Convenience functions
checkerror() {
    if [ $1 != 0 ]
    then
        printf "$2 - Error $1\n" >&2
        exit $1
    fi
}

# Sourcing the vendor script
export VENDOR_ERRORCODE=0
source $ROOTDIR/vnd/vendor.sh
checkerror $? "Failed to source the vendor script"

# Vendor error function
checkvendorerror() {
    if [ $VENDOR_ERRORCODE == 0 ]
    then
        export VENDOR_ERRORCODE=$1
    fi
}

# Run any vendor actions before generation
predocgenerate "$@"
checkerror $VENDOR_ERRORCODE "Failed to run pre-generation function from the vendor"

# Generate using vendor action
docgenerate "$@"
checkerror $VENDOR_ERRORCODE "Failed to run documentation generation function from the vendor"

# Run any vendor actions after generation
postdocgenerate "$@"
checkerror $VENDOR_ERRORCODE "Failed to run post-generation function from the vendor"

# Inform success
echo Build successful.
