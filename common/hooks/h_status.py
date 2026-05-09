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

# Git report info class
from common.fragments.frag_gitreport import GitReportInfo

# Configuration module
import adt_conf


# Status hook
def h_execute_status(arguments: tuple[Namespace, list[str]]):
    # Get the report info
    git_info = GitReportInfo()

    # Dirty repo
    proj_repo_dirty = git_info.repo.is_dirty()
    print("Dirty: %r" % proj_repo_dirty)

    # Untracked files
    proj_repo_untracked_files = git_info.untracked_files
    if (adt_conf.verbose):
        print("untracked_count: %r" % (len(proj_repo_untracked_files)))
    for untracked in proj_repo_untracked_files:
        print("Untracked file or directory: %s" % untracked)
    print("Untracked objects: %i" % len(proj_repo_untracked_files))

    # Repo index
    proj_repo_index = git_info.index
    changes = proj_repo_index.diff(None)
    for change in changes:
        print("Change [%s]: %s" % (change.change_type, change.a_path))
    print("Changes made: %i" % len(changes))
