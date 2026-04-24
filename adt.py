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

# Importing the scripts
from scripts.proj_actions import \
    s_build, \
    s_clean, \
    s_test, \
    s_increment, \
    s_vendorize, \
    s_gendocs, \
    s_packdocs, \
    s_packbin, \
    s_pushbin, \
    s_liquidize, \
    s_updatedeps, \
    s_listprojs
from scripts.standalone_actions import \
    s_intreport, \
    s_dnresxlang
from scripts.git_standalone_actions import \
    s_tags, \
    s_branches, \
    s_commits, \
    s_status, \
    s_revert, \
    s_commit, \
    s_push, \
    s_reset, \
    s_hardclean

# Configuration module
import adt_conf

# Project root
from common.fragments.frag_projecttools import frag_pt_getprojectroot

# Processing the arguments
import argparse
import sys
parser = argparse.ArgumentParser(
         prog='adt.py',
         add_help=False)
parser.add_argument('action',
                    metavar='action',
                    choices=[
                        # Project-specific actions
                        'build', 'clean', 'test', 'increment', 'vendorize',
                        'gendocs', 'packdocs', 'packbin', 'pushbin',
                        'liquidize', 'updatedeps', 'listprojs',

                        # Standalone actions
                        'intreport', 'dnresxlang',

                        # Standalone Git actions
                        'tags', 'branches', 'commits', 'status', 'revert',
                        'commit', 'push', 'reset', 'hardclean'
                    ])
parser.add_argument('--nobanner',
                    action='store_true')
parser.add_argument('--self',
                    action='store_true')

# Buffer issue fix
sys.stdout.reconfigure(line_buffering=True)

# Main
version = '1.0.1.0'
if __name__ == "__main__":
    # Configuration
    parser_args = parser.parse_known_args()
    adt_conf.action = parser_args[0].action
    adt_conf.nobanner = parser_args[0].nobanner
    adt_conf.on_self = parser_args[0].self
    adt_conf.project_path = frag_pt_getprojectroot(adt_conf.on_self)
    actargs = parser_args[1]

    # Show banner if required
    if not adt_conf.nobanner:
        print(f'\n\n        == Aptivi Development Toolkit (ADT) v{version} ==\n\n')
        print(f'Action:  {adt_conf.action} {actargs}')
        print(f'Project: {adt_conf.project_path}\n')

    # Match action
    match adt_conf.action:
        # Project-specific
        case "build":
            s_build(actargs)
        case "clean":
            s_clean(actargs)
        case "test":
            s_test(actargs)
        case "increment":
            s_increment(actargs)
        case "vendorize":
            s_vendorize(actargs)
        case "gendocs":
            s_gendocs(actargs)
        case "packdocs":
            s_packdocs(actargs)
        case "packbin":
            s_packbin(actargs)
        case "pushbin":
            s_pushbin(actargs)
        case "liquidize":
            s_liquidize(actargs)
        case "updatedeps":
            s_updatedeps(actargs)
        case "listprojs":
            s_listprojs(actargs)

        # Standalone
        case "intreport":
            s_intreport(actargs)
        case "dnresxlang":
            s_dnresxlang(actargs)

        # Git standalone
        case "tags":
            s_tags(actargs)
        case "branches":
            s_branches(actargs)
        case "commits":
            s_commits(actargs)
        case "status":
            s_status(actargs)
        case "revert":
            s_revert(actargs)
        case "commit":
            s_commit(actargs)
        case "push":
            s_push(actargs)
        case "reset":
            s_reset(actargs)
        case "hardclean":
            s_hardclean(actargs)
