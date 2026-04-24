#!/usr/bin/env python3

#
# Copyright 2025-2026 Aptivi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the “Software”), to deal in the Software without
# restriction, including without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#

# Importing necessary components
import sys
import os
import traceback


# Binary packing hook
def h_execute_packbin(arguments):
    result = arguments[0]
    extra_args = arguments[1]
    if (result.verbose):
        print("%r" % (result.verbose))

    # Execute pre-packbin actions
    prepackbin = None
    try:
        from vnd_packbin import vnd_prepackbin
        prepackbin = vnd_prepackbin
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_prepackbin is not defined')
            traceback.print_exception(iexc)
    if (prepackbin is not None):
        try:
            print("Executing pre-packbin actions...")
            prepackbin()
        except Exception as exc:
            print('Pre-packbin actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Binary packing the project
    packbin = None
    try:
        from vnd_packbin import vnd_packbin
        packbin = vnd_packbin
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_packbin is not defined')
            traceback.print_exception(iexc)
    if (packbin is not None):
        try:
            print("Packing binary for project...")
            packbin(extra_args)
        except Exception as exc:
            print('Binary packing actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-packbin actions
    postpackbin = None
    try:
        from vnd_packbin import vnd_postpackbin
        postpackbin = vnd_postpackbin
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_postpackbin is not defined')
            traceback.print_exception(iexc)
    if (postpackbin is not None):
        try:
            print("Executing post-packbin actions...")
            postpackbin()
        except Exception as exc:
            print('Post-packbin actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
