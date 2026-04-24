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


# Clean hook
def h_execute_clean(parser, clean_action_args):
    # Parse arguments
    arguments = parser.parse_known_args(clean_action_args)
    result = arguments[0]
    extra_args = arguments[1]
    if (result.verbose):
        print("%r" % (result.verbose))

    # Execute pre-clean actions
    preclean = None
    try:
        from vnd_clean import vnd_preclean
        preclean = vnd_preclean
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_preclean is not defined')
            traceback.print_exception(iexc)
    if (preclean is not None):
        try:
            print("Executing pre-clean actions...")
            preclean()
        except Exception as exc:
            print('Pre-clean actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Clean the project
    clean = None
    try:
        from vnd_clean import vnd_clean
        clean = vnd_clean
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_clean is not defined')
            traceback.print_exception(iexc)
    if (clean is not None):
        try:
            print("Cleaning project...")
            clean(extra_args)
        except Exception as exc:
            print('Clean actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-clean actions
    postclean = None
    try:
        from vnd_clean import vnd_postclean
        postclean = vnd_postclean
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_postclean is not defined')
            traceback.print_exception(iexc)
    if (postclean is not None):
        try:
            print("Executing post-clean actions...")
            postclean()
        except Exception as exc:
            print('Post-clean actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
