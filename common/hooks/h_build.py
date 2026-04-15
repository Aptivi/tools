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
vendor_script_dir = vendor_dir + 'vnd_build.py'
if not (os.path.isdir(vendor_dir)):
    print('Vendor directory doesn\'t exist.')
    sys.exit(2)
sys.path.append(vendor_dir)


# Build hook
def h_execute_build(parser, build_action_args):
    # Parse arguments
    arguments = parser.parse_known_args(build_action_args)
    result = arguments[0]
    extra_args = arguments[1]
    if (result.verbose):
        print("%r %s" % (result.verbose, result.build_args))

    # Check vendor script
    if not (os.path.isfile(vendor_script_dir)):
        print('Build vendor script doesn\'t exist. Doing nothing...')
        sys.exit(3)

    # Execute pre-build actions
    prebuild = None
    try:
        from vnd_build import vnd_prebuild
        prebuild = vnd_prebuild
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_prebuild is not defined')
            traceback.print_exception(iexc)
    if (prebuild is not None):
        try:
            print("Executing pre-build actions for %s..." % (project_root))
            prebuild()
        except Exception as exc:
            print('Pre-build actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Build the project
    build = None
    try:
        from vnd_build import vnd_build
        build = vnd_build
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_build is not defined')
            traceback.print_exception(iexc)
    if (build is not None):
        try:
            print("Building project %s..." % (project_root))
            build(result.build_args, extra_args)
        except Exception as exc:
            print('Build actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-build actions
    postbuild = None
    try:
        from vnd_build import vnd_postbuild
        postbuild = vnd_postbuild
    except ImportError as iexc:
        if (result.verbose):
            print('Function vnd_postbuild is not defined')
            traceback.print_exception(iexc)
    if (postbuild is not None):
        try:
            print("Executing post-build actions for %s..." % (project_root))
            postbuild()
        except Exception as exc:
            print('Post-build actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
