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


# Increment hook
def h_execute_increment(arguments):
    result = arguments[0]
    if (result.verbose):
        print("%r %s %s %s" % (result.verbose,
                               result.old_version, result.new_version,
                               result.api_versions))
        
    # Execute pre-increment actions
    preincrement = None
    try:
        from vnd_increment import vnd_preincrement
        preincrement = vnd_preincrement
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_preincrement is not defined')
            traceback.print_exception(iexc)
    if (preincrement is not None):
        try:
            print("Executing pre-increment actions...")
            preincrement()
        except Exception as exc:
            print('Pre-increment actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Increment the project
    increment = None
    try:
        from vnd_increment import vnd_increment
        increment = vnd_increment
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_increment is not defined')
            traceback.print_exception(iexc)
    if (increment is not None):
        try:
            print("Incrementing project...")
            increment(result.old_version, result.new_version,
                      result.api_versions)
        except Exception as exc:
            print('Increment actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-increment actions
    postincrement = None
    try:
        from vnd_increment import vnd_postincrement
        postincrement = vnd_postincrement
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_postincrement is not defined')
            traceback.print_exception(iexc)
    if (postincrement is not None):
        try:
            print("Executing post-increment actions...")
            postincrement()
        except Exception as exc:
            print('Post-increment actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
