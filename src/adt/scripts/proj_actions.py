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
from common.fragments.frag_argbuilder import frag_argbuilder_buildargs
from common.fragments.frag_hookexecutor import frag_hookexecutor_exec


# Functions
def s_build(action_args: list[str]):
    parser = frag_argbuilder_buildargs('Build', 'Build hook')
    parser.add_argument('-b', '--build-args',
                        help='Build arguments to pass to the build system '
                             '(depends on vendor build script)')
    frag_hookexecutor_exec(parser, action_args, True)


def s_clean(action_args: list[str]):
    parser = frag_argbuilder_buildargs('clean', 'Clean hook')
    frag_hookexecutor_exec(parser, action_args, True)


def s_install(action_args: list[str]):
    parser = frag_argbuilder_buildargs('install', 'Install hook')
    frag_hookexecutor_exec(parser, action_args, True)


def s_test(action_args: list[str]):
    parser = frag_argbuilder_buildargs('test', 'Test hook')
    parser.add_argument('-t', '--test-args',
                        help='Test arguments to pass to the test system '
                             '(depends on vendor test script)')
    frag_hookexecutor_exec(parser, action_args, True)


def s_increment(action_args: list[str]):
    parser = frag_argbuilder_buildargs('increment', 'Increment hook')
    parser.add_argument('old_version',
                        help='Old application version to increment from')
    parser.add_argument('new_version',
                        help='New application version to increment to')
    parser.add_argument('api_versions',
                        nargs=argparse.REMAINDER,
                        help='Old and new application API versions to '
                             'increment from to')
    frag_hookexecutor_exec(parser, action_args, True)


def s_vendorize(action_args: list[str]):
    parser = frag_argbuilder_buildargs('vendorize', 'Vendorize hook')
    frag_hookexecutor_exec(parser, action_args, True)


def s_gendocs(action_args: list[str]):
    parser = frag_argbuilder_buildargs('gendocs', 'Docs generator hook')
    frag_hookexecutor_exec(parser, action_args, True)


def s_packdocs(action_args: list[str]):
    parser = frag_argbuilder_buildargs('vendorize', 'Asset vendor hook')
    frag_hookexecutor_exec(parser, action_args, True)


def s_packbin(action_args: list[str]):
    parser = frag_argbuilder_buildargs('packbin', 'Binary pack hook')
    frag_hookexecutor_exec(parser, action_args, True)


def s_pushbin(action_args: list[str]):
    parser = frag_argbuilder_buildargs('pushbin', 'Binary push hook')
    frag_hookexecutor_exec(parser, action_args, True)


def s_liquidize(action_args: list[str]):
    parser = frag_argbuilder_buildargs('liquidize', 'Liquidize hook')
    frag_hookexecutor_exec(parser, action_args, True)


def s_updatedeps(action_args: list[str]):
    parser = frag_argbuilder_buildargs('updatedeps', 'Depedency update hook')
    frag_hookexecutor_exec(parser, action_args, True)


def s_listprojs(action_args: list[str]):
    parser = frag_argbuilder_buildargs('listprojs', 'Project list hook')
    frag_hookexecutor_exec(parser, action_args, True)
