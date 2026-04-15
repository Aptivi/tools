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

# Load required fragment
from common.fragments.frag_gitprogress import ProgressFragment

# Git report info class
from common.fragments.frag_gitreport import GitReportInfo


# Push hook
def h_execute_push(parser, push_action_args):
    # Parse arguments
    result = parser.parse_args(push_action_args)
    if (result.verbose):
        print("%r %s" % (result.verbose, result.remote))

    # Get the report info
    git_info = GitReportInfo()
    remote = git_info.repo.remote(result.remote)
    remote.push(git_info.active_branch.name, progress=ProgressFragment())
    print("\n\nPush finished. Refer to above output for info.")
