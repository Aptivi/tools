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


# Binary pushing hook
def h_execute_pushbin(arguments):
    result = arguments[0]
    extra_args = arguments[1]
    if (result.verbose):
        print("%r" % (result.verbose))

    # Execute pre-pushbin actions
    prepushbin = None
    try:
        from vnd_pushbin import vnd_prepushbin
        prepushbin = vnd_prepushbin
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_prepushbin is not defined')
            traceback.print_exception(iexc)
    if (prepushbin is not None):
        try:
            print("Executing pre-pushbin actions...")
            prepushbin()
        except Exception as exc:
            print('Pre-pushbin actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Binary pushing the project
    pushbin = None
    try:
        from vnd_pushbin import vnd_pushbin
        pushbin = vnd_pushbin
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_pushbin is not defined')
            traceback.print_exception(iexc)
    if (pushbin is not None):
        try:
            print("Pushing binary for project...")
            pushbin(extra_args)
        except Exception as exc:
            print('Binary pushing actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-pushbin actions
    postpushbin = None
    try:
        from vnd_pushbin import vnd_postpushbin
        postpushbin = vnd_postpushbin
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_postpushbin is not defined')
            traceback.print_exception(iexc)
    if (postpushbin is not None):
        try:
            print("Executing post-pushbin actions...")
            postpushbin()
        except Exception as exc:
            print('Post-pushbin actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
