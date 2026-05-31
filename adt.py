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
from scripts.proj_actions import *
from scripts.standalone_actions import *
from scripts.git_standalone_actions import *

# Configuration module
import adt_conf

# Project root
from common.fragments.frag_projecttools import frag_pt_getprojectroot

# Other necessary imports
import argparse
import os
import sys

# Function mapping
function_map = {
    # Project-specific
    'build': s_build,
    'clean': s_clean,
    'test': s_test,
    'increment': s_increment,
    'vendorize': s_vendorize,
    'gendocs': s_gendocs,
    'packdocs': s_packdocs,
    'packbin': s_packbin,
    'pushbin': s_pushbin,
    'liquidize': s_liquidize,
    'updatedeps': s_updatedeps,
    'listprojs': s_listprojs,

    # Standalone
    'intreport': s_intreport,
    'dnresxlang': s_dnresxlang,
    
    # Git standalone
    'tags': s_tags,
    'branches': s_branches,
    'commits': s_commits,
    'status': s_status,
    'revert': s_revert,
    'commit': s_commit,
    'push': s_push,
    'reset': s_reset,
    'hardclean': s_hardclean,
}

# Main
version = '1.1.0.0'
if __name__ == "__main__":
    # Processing the arguments
    parser = argparse.ArgumentParser(
            prog='adt.py',
            add_help=False)
    parser.add_argument('action')
    parser.add_argument('--nobanner', action='store_true')
    parser.add_argument('--self', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--path')
    parser.add_argument('--version', action='version', version=f'{version}')

    # Buffer issue fix
    sys.stdout.reconfigure(line_buffering=True)

    # Configuration
    parser_args = parser.parse_known_args()
    adt_conf.action = parser_args[0].action
    adt_conf.nobanner = parser_args[0].nobanner
    adt_conf.on_self = False if parser_args[0].path else parser_args[0].self
    adt_conf.verbose = parser_args[0].verbose
    adt_conf.project_path = frag_pt_getprojectroot(adt_conf.on_self,
                                                   parser_args[0].path)
    adt_conf.project_name = os.path.basename(adt_conf.project_path)
    actargs = parser_args[1]

    # Show banner if required
    if not adt_conf.nobanner:
        print('\n\n')
        print(f'                == Aptivi Development Toolkit (ADT) v{version} ==')
        print('\n\n')
        if adt_conf.verbose:
            print(f'Action:  {adt_conf.action} {actargs}')
            print(f'Project: {adt_conf.project_name} [{adt_conf.project_path}]\n')

    # Match action
    if adt_conf.action in function_map:
        function_map[adt_conf.action](actargs)
    else:
        s_custom_action(actargs)
