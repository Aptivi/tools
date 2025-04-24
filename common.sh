#!/bin/bash
# shellcheck disable=SC2317

# Repository root
ROOTDIR=$( cd -- "$( dirname -- "$0" )/.." &> /dev/null && pwd )

# Action declaration
ACTION=$1
if [ -z $ACTION ]; then
    ACTION=build
fi

# Vendor functions
eval "pre${ACTION}() { return 0; }"
eval "${ACTION}() { return 0; }"
eval "post${ACTION}() { return 0; }"

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

# Run any vendor actions before action
pre${ACTION} "$@"
checkerror $VENDOR_ERRORCODE "Failed to run pre${ACTION} function from the vendor"

# Run any vendor actions during action
${ACTION} "$@"
checkerror $VENDOR_ERRORCODE "Failed to run ${ACTION} function from the vendor"

# Run any vendor actions after action
post${ACTION} "$@"
checkerror $VENDOR_ERRORCODE "Failed to run post${ACTION} function from the vendor"

# Inform success
echo "Action ${ACTION} successful."
