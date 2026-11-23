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
from argparse import Namespace
import sys
import traceback

# Configuration module
import adt_conf


# Install hook
def h_execute(arguments: tuple[Namespace, list[str]]):
    extra_args = arguments[1]

    # Execute pre-install actions
    preinstall = None
    try:
        from vnd_install import vnd_preinstall
        preinstall = vnd_preinstall
    except ImportError as iexc:
        if (adt_conf.verbose):
            print('Function vnd_preinstall is not defined')
            traceback.print_exception(iexc)
    if (preinstall is not None):
        try:
            print("Executing pre-install actions...")
            preinstall()
        except Exception as exc:
            print('Pre-install actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Install the project
    install = None
    try:
        from vnd_install import vnd_install
        install = vnd_install
    except ImportError as iexc:
        if (adt_conf.verbose):
            print('Function vnd_install is not defined')
            traceback.print_exception(iexc)
    if (install is not None):
        try:
            print("installing project...")
            install(extra_args)
        except Exception as exc:
            print('install actions failed')
            traceback.print_exception(exc)
            sys.exit(1)

    # Execute post-install actions
    postinstall = None
    try:
        from vnd_install import vnd_postinstall
        postinstall = vnd_postinstall
    except ImportError as iexc:
        if (adt_conf.verbose):
            print('Function vnd_postinstall is not defined')
            traceback.print_exception(iexc)
    if (postinstall is not None):
        try:
            print("Executing post-install actions...")
            postinstall()
        except Exception as exc:
            print('Post-install actions failed')
            traceback.print_exception(exc)
            sys.exit(1)
