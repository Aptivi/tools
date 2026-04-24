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


# Vendorize hook
def h_execute_vendorize(parser, vendorize_action_args):
    # Parse arguments
    arguments = parser.parse_known_args(vendorize_action_args)
    result = arguments[0]
    extra_args = arguments[1]
    if (result.verbose):
        print("%r" % (result.verbose))

    # Execute pre-vendorize actions
    prevendorize = None
    try:
        from vnd_vendorize import vnd_prevendorize
        prevendorize = vnd_prevendorize
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_prevendorize is not defined')
            traceback.print_exception(iexc)
    if (prevendorize is not None):
        try:
            print("Executing pre-vendorize actions...")
            prevendorize()
        except Exception as exc:
            print('Pre-vendorize actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Vendorize the project
    vendorize = None
    try:
        from vnd_vendorize import vnd_vendorize
        vendorize = vnd_vendorize
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_vendorize is not defined')
            traceback.print_exception(iexc)
    if (vendorize is not None):
        try:
            print("Vendorizing project...")
            vendorize(extra_args)
        except Exception as exc:
            print('Vendorize actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-vendorize actions
    postvendorize = None
    try:
        from vnd_vendorize import vnd_postvendorize
        postvendorize = vnd_postvendorize
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_postvendorize is not defined')
            traceback.print_exception(iexc)
    if (postvendorize is not None):
        try:
            print("Executing post-vendorize actions...")
            postvendorize()
        except Exception as exc:
            print('Post-vendorize actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
