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

# Other imports
from common.fragments.frag_argbuilder import frag_argbuilder_buildargs
from common.fragments.frag_hookexecutor import frag_hookexecutor_exec


# Functions
def s_tags(action_args: list[str]):
    parser = frag_argbuilder_buildargs('tags', 'Tags hook',
                                       '#git-specific-actions')
    frag_hookexecutor_exec(parser, action_args)


def s_branches(action_args: list[str]):
    parser = frag_argbuilder_buildargs('branches', 'Branches hook',
                                       '#git-specific-actions')
    parser.add_argument('-r', '--remotes',
                        action="store_true",
                        help='Whether to list remote branches')
    frag_hookexecutor_exec(parser, action_args)


def s_commits(action_args: list[str]):
    parser = frag_argbuilder_buildargs('commits', 'Commits hook',
                                       '#git-specific-actions')
    frag_hookexecutor_exec(parser, action_args)


def s_status(action_args: list[str]):
    parser = frag_argbuilder_buildargs('status', 'Status hook',
                                       '#git-specific-actions')
    frag_hookexecutor_exec(parser, action_args)


def s_revert(action_args: list[str]):
    parser = frag_argbuilder_buildargs('revert', 'Revert hook',
                                       '#git-specific-actions')
    parser.add_argument('commit',
                        metavar='commit',
                        help='Specifies a commit to revert')
    frag_hookexecutor_exec(parser, action_args)


def s_commit(action_args: list[str]):
    parser = frag_argbuilder_buildargs('commit', 'Commit hook',
                                       '#git-specific-actions')
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
    parser.add_argument('-c', '--backport-commits',
                        help='Backported commit SHA hashes with slashes')
    parser.add_argument('-pn', '--part-number',
                        help='Commit part number (must not exceed the total '
                             'commits number)',
                        default=1)
    parser.add_argument('-pt', '--part-total',
                        help='Commit part total number',
                        default=1)
    parser.add_argument('-d', '--dry',
                        action="store_true",
                        help='Whether to run dryly (no actual commit)')
    parser.add_argument('-p', '--push',
                        action="store_true",
                        help='Whether to push the commit immediately')
    parser.add_argument('-r', '--remote',
                        help='Specifies a remote to use',
                        default="origin")
    frag_hookexecutor_exec(parser, action_args)


def s_push(action_args: list[str]):
    parser = frag_argbuilder_buildargs('push', 'Push hook',
                                       '#git-specific-actions')
    parser.add_argument('-r', '--remote',
                        help='Specifies a remote to use',
                        default="origin")
    frag_hookexecutor_exec(parser, action_args)


def s_fetch(action_args: list[str]):
    parser = frag_argbuilder_buildargs('fetch', 'Fetch hook',
                                       '#git-specific-actions')
    parser.add_argument('-r', '--remote',
                        help='Specifies a remote to use',
                        default="origin")
    frag_hookexecutor_exec(parser, action_args)


def s_pull(action_args: list[str]):
    parser = frag_argbuilder_buildargs('pull', 'Pull hook',
                                       '#git-specific-actions')
    parser.add_argument('-r', '--remote',
                        help='Specifies a remote to use',
                        default="origin")
    frag_hookexecutor_exec(parser, action_args)


def s_reset(action_args: list[str]):
    parser = frag_argbuilder_buildargs('reset', 'Reset hook',
                                       '#git-specific-actions')
    parser.add_argument('commit',
                        metavar='commit',
                        help='Specifies a commit to revert')
    frag_hookexecutor_exec(parser, action_args)


def s_hardclean(action_args: list[str]):
    parser = frag_argbuilder_buildargs('hardclean', 'Hard clean hook',
                                       '#git-specific-actions')
    frag_hookexecutor_exec(parser, action_args)
