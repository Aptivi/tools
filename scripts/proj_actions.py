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
from common.fragments.frag_projecttools import frag_pt_preparevendor

# Other imports
from common.fragments.frag_manual import frag_manual_genlink


# Functions
def s_build(build_action_args):
    parser = argparse.ArgumentParser(
        prog='adt build',
        description='Build hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    parser.add_argument('-b', '--build-args',
                        help='Build arguments to pass to the build system '
                             '(depends on vendor build script)')
    from common.hooks.h_build import h_execute_build
    frag_pt_preparevendor()
    h_execute_build(parser, build_action_args)


def s_clean(clean_action_args):
    parser = argparse.ArgumentParser(
        prog='adt clean',
        description='Clean hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_clean import h_execute_clean
    frag_pt_preparevendor()
    h_execute_clean(parser, clean_action_args)


def s_test(test_action_args):
    parser = argparse.ArgumentParser(
        prog='adt test',
        description='Test hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    parser.add_argument('-t', '--test-args',
                        help='Test arguments to pass to the test system '
                             '(depends on vendor test script)')
    from common.hooks.h_test import h_execute_test
    frag_pt_preparevendor()
    h_execute_test(parser, test_action_args)


def s_increment(increment_action_args):
    parser = argparse.ArgumentParser(
        prog='adt increment',
        description='Increment hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    parser.add_argument('old_version',
                        help='Old application version to increment from')
    parser.add_argument('new_version',
                        help='New application version to increment to')
    parser.add_argument('api_versions',
                        nargs=argparse.REMAINDER,
                        help='Old and new application API versions to '
                             'increment from to')
    from common.hooks.h_increment import h_execute_increment
    frag_pt_preparevendor()
    h_execute_increment(parser, increment_action_args)


def s_vendorize(vendorize_action_args):
    parser = argparse.ArgumentParser(
        prog='adt vendorize',
        description='Vendorize hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_vendorize import h_execute_vendorize
    frag_pt_preparevendor()
    h_execute_vendorize(parser, vendorize_action_args)


def s_gendocs(gendocs_action_args):
    parser = argparse.ArgumentParser(
        prog='adt gendocs',
        description='Docs generator hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_gendocs import h_execute_gendocs
    frag_pt_preparevendor()
    h_execute_gendocs(parser, gendocs_action_args)


def s_packdocs(packdocs_action_args):
    parser = argparse.ArgumentParser(
        prog='adt vendorize',
        description='Docs packing hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_packdocs import h_execute_packdocs
    frag_pt_preparevendor()
    h_execute_packdocs(parser, packdocs_action_args)


def s_packbin(packbin_action_args):
    parser = argparse.ArgumentParser(
        prog='adt packbin',
        description='Binary packing hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_packbin import h_execute_packbin
    frag_pt_preparevendor()
    h_execute_packbin(parser, packbin_action_args)


def s_pushbin(pushbin_action_args):
    parser = argparse.ArgumentParser(
        prog='adt pushbin',
        description='Binary pushing hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_pushbin import h_execute_pushbin
    frag_pt_preparevendor()
    h_execute_pushbin(parser, pushbin_action_args)


def s_liquidize(liquidize_action_args):
    parser = argparse.ArgumentParser(
        prog='adt liquidize',
        description='Liquidize hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_liquidize import h_execute_liquidize
    frag_pt_preparevendor()
    h_execute_liquidize(parser, liquidize_action_args)


def s_updatedeps(updatedeps_action_args):
    parser = argparse.ArgumentParser(
        prog='adt updatedeps',
        description='Depedency update hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_updatedeps import h_execute_updatedeps
    frag_pt_preparevendor()
    h_execute_updatedeps(parser, updatedeps_action_args)


def s_listprojs(listprojs_action_args):
    parser = argparse.ArgumentParser(
        prog='adt listprojs',
        description='Project list hook - Aptivi Development Kit (ADT)',
        epilog=frag_manual_genlink(\
            'build-system/structure'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_listprojs import h_execute_listprojs
    frag_pt_preparevendor()
    h_execute_listprojs(parser, listprojs_action_args)
