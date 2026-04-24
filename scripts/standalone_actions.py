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

# Processing the arguments
import argparse

# Other imports
from common.fragments.frag_manual import frag_manual_genlink


# Functions
def s_intreport(intreport_action_args):
    parser = argparse.ArgumentParser(
        prog='adt intreport',
        description='Report maker - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure#standalone-actions'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    parser.add_argument('-l', '--local',
                        action="store_true",
                        help='Upload to local path')
    parser.add_argument('-lp', '--local-path',
                        help='Upload to specified local path instead of '
                             'to the SSH server')
    parser.add_argument('-r', '--remote',
                        action="store_true",
                        help='Upload to remote')
    parser.add_argument('-rp', '--remote-path',
                        help='Upload to specified remote path'
                             'in the SSH server',
                        default="/usr/local/share/aptdev")
    parser.add_argument('-sh', '--server-host',
                        help='Host name or IP address of the SSH server '
                             'to upload info to',
                        default="127.0.0.1")
    parser.add_argument('-sp', '--server-port',
                        help='Port of the SSH server to upload info to',
                        default=22)
    parser.add_argument('-su', '--server-username',
                        help='SSH server username to authenticate with')
    parser.add_argument('-sw', '--server-password',
                        help='SSH password for use with authentication')
    parser.add_argument('-sk', '--server-privkey',
                        help='SSH private key for use with authentication '
                             '(recommended)')
    from common.hooks.h_intreport import h_execute_intreport
    h_execute_intreport(parser, intreport_action_args)

    
def s_dnresxlang(dnresxlang_action_args):
    parser = argparse.ArgumentParser(
        prog='adt dnresxlang',
        description='.NET .resx tools for localizations - '
                    'Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure#standalone-actions'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    parser.add_argument('json_path',
                        help='Specifies a full path to localization JSON ' +
                             'files')
    parser.add_argument('-ac', '--add-culture',
                        action="store_true",
                        help='Adds a new culture')
    parser.add_argument('-ai', '--add-loc',
                        action="store_true",
                        help='Adds a new localization ID')
    parser.add_argument('-al', '--add-lang',
                        action="store_true",
                        help='Adds a new language')
    parser.add_argument('-c', '--cultures',
                        action="append",
                        help='Specifes the cultures for new language')
    parser.add_argument('-dc', '--delete-culture',
                        action="store_true",
                        help='Deletes a culture from language')
    parser.add_argument('-di', '--delete-loc',
                        action="store_true",
                        help='Deletes a localization ID from language')
    parser.add_argument('-dl', '--delete-lang',
                        action="store_true",
                        help='Deletes a language')
    parser.add_argument('-ec', '--edit-culture',
                        action="store_true",
                        help='Edits a culture')
    parser.add_argument('-ei', '--edit-loc',
                        action="store_true",
                        help='Edits a localization')
    parser.add_argument('-i', '--localization',
                        action="append",
                        help='Specifies a list of localizations')
    parser.add_argument('-is', '--localization-strs',
                        action="append",
                        nargs=2,
                        help='Specifies a list of localizations and their ' +
                             'strings')
    parser.add_argument('-l', '--language',
                        help='Specifies a language')
    parser.add_argument('-r', '--report',
                        action="store_true",
                        help='Report info for a language. If -l is not ' +
                             'specified, a report will be done for all ' +
                             'languages.')
    parser.add_argument('-rp', '--resx-path',
                        help='Specifies an output path for generated .resx ' +
                             'files')
    parser.add_argument('-s', '--save',
                        action="store_true",
                        help='Saves JSON language files as .resx files')
    from common.hooks.h_dnresxlang import h_execute_dnresxlang
    h_execute_dnresxlang(parser, dnresxlang_action_args)
