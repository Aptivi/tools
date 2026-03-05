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

# Import time
import time

# Git report info class
from common.fragments.frag_gitreport import GitReportInfo


# Commits hook
def h_execute_commits(parser, commits_action_args):
    # Parse arguments
    result = parser.parse_args(commits_action_args)
    if (result.verbose):
        print("%r" % (result.verbose))

    # Import git
    git_info = GitReportInfo()
    proj_repo_commits = git_info.commits
    if (result.verbose):
        print("Count is [%i]" % (len(proj_repo_commits)))
    for commit in proj_repo_commits:
        commit_sha = commit.hexsha[:9]
        commit_datetime = time.strftime("%Y/%m/%d %H:%M:%S",
                                        time.gmtime(commit.committed_date))
        commit_authorname = commit.author.name or "Unknown"
        commit_committername = commit.committer.name or "Unknown"
        commit_renderedauthor = \
            commit_authorname \
            if commit_authorname == commit_committername \
            else commit_authorname + ' | ' + commit_committername
        commit_summary = commit.summary
        print("%s | %s | %s | %s" %
              (commit_sha,
               commit_datetime,
               commit_renderedauthor,
               commit_summary))
