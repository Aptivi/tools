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


# Dependency update hook
def h_execute_updatedeps(parser, updatedeps_action_args):
    # Parse arguments
    arguments = parser.parse_known_args(updatedeps_action_args)
    result = arguments[0]
    extra_args = arguments[1]
    if (result.verbose):
        print("%r" % (result.verbose))

    # Execute pre-updatedeps actions
    preupdatedeps = None
    try:
        from vnd_updatedeps import vnd_preupdatedeps
        preupdatedeps = vnd_preupdatedeps
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_preupdatedeps is not defined')
            traceback.print_exception(iexc)
    if (preupdatedeps is not None):
        try:
            print("Executing pre-updatedeps actions...")
            preupdatedeps()
        except Exception as exc:
            print('Pre-updatedeps actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Update project dependencies for the project
    updatedeps = None
    try:
        from vnd_updatedeps import vnd_updatedeps
        updatedeps = vnd_updatedeps
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_updatedeps is not defined')
            traceback.print_exception(iexc)
    if (updatedeps is not None):
        try:
            print("Updating dependencies for project...")
            updatedeps(extra_args)
        except Exception as exc:
            print('Dependency update actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-updatedeps actions
    postupdatedeps = None
    try:
        from vnd_updatedeps import vnd_postupdatedeps
        postupdatedeps = vnd_postupdatedeps
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_postupdatedeps is not defined')
            traceback.print_exception(iexc)
    if (postupdatedeps is not None):
        try:
            print("Executing post-updatedeps actions...")
            postupdatedeps()
        except Exception as exc:
            print('Post-updatedeps actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
