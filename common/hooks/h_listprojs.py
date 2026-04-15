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
import adt_conf
project_root = frag_pt_getprojectroot(adt_conf.on_self)
vendor_dir = project_root + '/vendor/'
vendor_script_dir = vendor_dir + 'vnd_listprojs.py'
if not (os.path.isdir(vendor_dir)):
    print('Vendor directory doesn\'t exist.')
    sys.exit()
sys.path.append(vendor_dir)


# Listing projects hook
def h_execute_listprojs(parser, listprojs_action_args):
    # Parse arguments
    arguments = parser.parse_known_args(listprojs_action_args)
    result = arguments[0]
    extra_args = arguments[1]
    if (result.verbose):
        print("%r" % (result.verbose))
        
    # Check vendor script
    if not (os.path.isfile(vendor_script_dir)):
        print('Listing projects vendor script doesn\'t exist. Doing nothing...')
        sys.exit()

    # Execute pre-listprojs actions
    prelistprojs = None
    try:
        from vnd_listprojs import vnd_prelistprojs
        prelistprojs = vnd_prelistprojs
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_prelistprojs is not defined')
            traceback.print_exception(iexc)
    if (prelistprojs is not None):
        try:
            print("Executing pre-listprojs actions for %s..." % (project_root))
            prelistprojs()
        except Exception as exc:
            print('Pre-listprojs actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Listing projects the project
    listprojs = None
    try:
        from vnd_listprojs import vnd_listprojs
        listprojs = vnd_listprojs
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_listprojs is not defined')
            traceback.print_exception(iexc)
    if (listprojs is not None):
        try:
            print("Listing project files for project %s..." % (project_root))
            listprojs(extra_args)
        except Exception as exc:
            print('Listing project files actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-listprojs actions
    postlistprojs = None
    try:
        from vnd_listprojs import vnd_postlistprojs
        postlistprojs = vnd_postlistprojs
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_postlistprojs is not defined')
            traceback.print_exception(iexc)
    if (postlistprojs is not None):
        try:
            print("Executing post-listprojs actions for %s..." % (project_root))
            postlistprojs()
        except Exception as exc:
            print('Post-listprojs actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
