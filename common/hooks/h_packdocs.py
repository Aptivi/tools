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


# Documentation packing hook
def h_execute_packdocs(parser, packdocs_action_args):
    # Parse arguments
    arguments = parser.parse_known_args(packdocs_action_args)
    result = arguments[0]
    extra_args = arguments[1]
    if (result.verbose):
        print("%r" % (result.verbose))

    # Execute pre-packdocs actions
    prepackdocs = None
    try:
        from vnd_packdocs import vnd_prepackdocs
        prepackdocs = vnd_prepackdocs
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_prepackdocs is not defined')
            traceback.print_exception(iexc)
    if (prepackdocs is not None):
        try:
            print("Executing pre-packdocs actions...")
            prepackdocs()
        except Exception as exc:
            print('Pre-packdocs actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Documentation packing the project
    packdocs = None
    try:
        from vnd_packdocs import vnd_packdocs
        packdocs = vnd_packdocs
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_packdocs is not defined')
            traceback.print_exception(iexc)
    if (packdocs is not None):
        try:
            print("Packing documentation for project...")
            packdocs(extra_args)
        except Exception as exc:
            print('Documentation packing actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-packdocs actions
    postpackdocs = None
    try:
        from vnd_packdocs import vnd_postpackdocs
        postpackdocs = vnd_postpackdocs
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_postpackdocs is not defined')
            traceback.print_exception(iexc)
    if (postpackdocs is not None):
        try:
            print("Executing post-packdocs actions...")
            postpackdocs()
        except Exception as exc:
            print('Post-packdocs actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
