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


# Test hook
def h_execute_test(parser, test_action_args):
    # Parse arguments
    arguments = parser.parse_known_args(test_action_args)
    result = arguments[0]
    extra_args = arguments[1]
    if (result.verbose):
        print("%r %s" % (result.verbose, result.test_args))

    # Execute pre-test actions
    pretest = None
    try:
        from vnd_test import vnd_pretest
        pretest = vnd_pretest
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_pretest is not defined')
            traceback.print_exception(iexc)
    if (pretest is not None):
        try:
            print("Executing pre-test actions...")
            pretest()
        except Exception as exc:
            print('Pre-test actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Test the project
    test = None
    try:
        from vnd_test import vnd_test
        test = vnd_test
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_test is not defined')
            traceback.print_exception(iexc)
    if (test is not None):
        try:
            print("Testing project...")
            test(result.test_args, extra_args)
        except Exception as exc:
            print('Test actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-test actions
    posttest = None
    try:
        from vnd_test import vnd_posttest
        posttest = vnd_posttest
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_posttest is not defined')
            traceback.print_exception(iexc)
    if (posttest is not None):
        try:
            print("Executing post-test actions...")
            posttest()
        except Exception as exc:
            print('Post-test actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
