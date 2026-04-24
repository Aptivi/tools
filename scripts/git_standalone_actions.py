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
def s_tags(tags_action_args):
    parser = argparse.ArgumentParser(
            prog='adt tags',
            description='Tags hook - Aptivi Development Kit (ADT)',
            epilog=frag_manual_genlink(\
                'build-system/structure#git-specific-actions'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_tags import h_execute_tags
    arguments = parser.parse_known_args(tags_action_args)
    h_execute_tags(arguments)


def s_branches(branches_action_args):
    parser = argparse.ArgumentParser(
            prog='adt branches',
            description='Branches hook - Aptivi Development Kit (ADT)',
            epilog=frag_manual_genlink(\
                'build-system/structure#git-specific-actions'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_branches import h_execute_branches
    arguments = parser.parse_known_args(branches_action_args)
    h_execute_branches(arguments)


def s_commits(commits_action_args):
    parser = argparse.ArgumentParser(
            prog='adt commits',
            description='Commits hook - Aptivi Development Kit (ADT)',
            epilog=frag_manual_genlink(\
                'build-system/structure#git-specific-actions'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_commits import h_execute_commits
    arguments = parser.parse_known_args(commits_action_args)
    h_execute_commits(arguments)


def s_status(status_action_args):
    parser = argparse.ArgumentParser(
            prog='adt status',
            description='Status hook - Aptivi Development Kit (ADT)',
            epilog=frag_manual_genlink(\
                'build-system/structure#git-specific-actions'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_status import h_execute_status
    arguments = parser.parse_known_args(status_action_args)
    h_execute_status(arguments)


def s_revert(revert_action_args):
    parser = argparse.ArgumentParser(
            prog='adt revert',
            description='Revert hook - Aptivi Development Kit (ADT)',
            epilog=frag_manual_genlink(\
                'build-system/structure#git-specific-actions'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    parser.add_argument('commit',
                        metavar='commit',
                        help='Specifies a commit to revert')
    from common.hooks.h_revert import h_execute_revert
    arguments = parser.parse_known_args(revert_action_args)
    h_execute_revert(arguments)


def s_commit(commit_action_args):
    parser = argparse.ArgumentParser(
            prog='adt commit',
            description='Commit hook - Aptivi Development Kit (ADT)',
            epilog=frag_manual_genlink(\
                'build-system/structure#git-specific-actions'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    parser.add_argument('-s', '--summary',
                        help='Summary of the commit',
                        required=True)
    parser.add_argument('-b', '--body',
                        help='Body message of the commit')
    parser.add_argument('-t', '--type',
                        help='Type of the commit',
                        required=True,
                        choices=["add", "fix", "rem", "imp", "ref", "upd",
                                 "doc", "dev", "dcp", "fin", "chg", "int",
                                 "bkp", "prj", "pkg", "und"])
    parser.add_argument('-a', '--attributes',
                        help='Commit attributes, where they are grouped with '
                             'slashes (one of brk, sec, prf, reg, doc, ptp, '
                             'prt, bkp)')
    parser.add_argument('-i', '--assisted',
                        action="store_true",
                        help='Whether this commit is AI assisted or not')
    parser.add_argument('--assistant',
                        help='Specifies the AI assistant(s)')
    parser.add_argument('-c', '--backport-commits',
                        help='Backported commit SHA hashes with slashes')
    parser.add_argument('-d', '--dry',
                        action="store_true",
                        help='Whether to run dryly (no actual commit)')
    from common.hooks.h_commit import h_execute_commit
    arguments = parser.parse_known_args(commit_action_args)
    h_execute_commit(arguments)


def s_push(push_action_args):
    parser = argparse.ArgumentParser(
            prog='adt push',
            description='Push hook - Aptivi Development Kit (ADT)',
            epilog=frag_manual_genlink(\
                'build-system/structure#git-specific-actions'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    parser.add_argument('-r', '--remote',
                        help='Specifies a remote to use',
                        default="origin")
    from common.hooks.h_push import h_execute_push
    arguments = parser.parse_known_args(push_action_args)
    h_execute_push(arguments)


def s_reset(reset_action_args):
    parser = argparse.ArgumentParser(
            prog='adt reset',
            description='Reset hook - Aptivi Development Kit (ADT)',
            epilog=frag_manual_genlink(\
                'build-system/structure#git-specific-actions'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    parser.add_argument('commit',
                        metavar='commit',
                        help='Specifies a commit to revert')
    from common.hooks.h_reset import h_execute_reset
    arguments = parser.parse_known_args(reset_action_args)
    h_execute_reset(arguments)


def s_hardclean(hardclean_action_args):
    parser = argparse.ArgumentParser(
            prog='adt hardclean',
            description='Hard clean hook - Aptivi Development Kit (ADT)',
            epilog=frag_manual_genlink(\
                'build-system/structure#git-specific-actions'))
    parser.add_argument('-v', '--verbose',
                        action="store_true",
                        help='Shows debug output for variables, command '
                             'inputs, and other actions')
    from common.hooks.h_hardclean import h_execute_hardclean
    arguments = parser.parse_known_args(hardclean_action_args)
    h_execute_hardclean(arguments)
