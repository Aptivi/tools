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
from common.fragments.frag_projecttools import frag_pt_getprojectroot
project_root = frag_pt_getprojectroot()
vendor_dir = project_root + '/vendor/'
vendor_script_dir = vendor_dir + 'vnd_gendocs.py'
if not (os.path.isdir(vendor_dir)):
    print('Vendor directory doesn\'t exist.')
    sys.exit(2)
sys.path.append(vendor_dir)


# Documentation generation hook
def h_execute_gendocs(parser, gendocs_action_args):
    # Parse arguments
    arguments = parser.parse_known_args(gendocs_action_args)
    result = arguments[0]
    extra_args = arguments[1]
    if (result.verbose):
        print("%r" % (result.verbose))

    # Check vendor script
    if not (os.path.isfile(vendor_script_dir)):
        print('Documentation generation vendor script doesn\'t exist. Doing nothing...')
        sys.exit(3)

    # Execute pre-gendocs actions
    pregendocs = None
    try:
        from vnd_gendocs import vnd_pregendocs
        pregendocs = vnd_pregendocs
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_pregendocs is not defined')
            traceback.print_exception(iexc)
    if (pregendocs is not None):
        try:
            print("Executing pre-gendocs actions for %s..." % (project_root))
            pregendocs()
        except Exception as exc:
            print('Pre-gendocs actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Documentation generation the project
    gendocs = None
    try:
        from vnd_gendocs import vnd_gendocs
        gendocs = vnd_gendocs
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_gendocs is not defined')
            traceback.print_exception(iexc)
    if (gendocs is not None):
        try:
            print("Generating documentation for project %s..." % (project_root))
            gendocs(extra_args)
        except Exception as exc:
            print('Documentation generation actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-gendocs actions
    postgendocs = None
    try:
        from vnd_gendocs import vnd_postgendocs
        postgendocs = vnd_postgendocs
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_postgendocs is not defined')
            traceback.print_exception(iexc)
    if (postgendocs is not None):
        try:
            print("Executing post-gendocs actions for %s..." % (project_root))
            postgendocs()
        except Exception as exc:
            print('Post-gendocs actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
