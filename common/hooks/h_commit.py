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

import os
import textwrap

# Git report info class
from common.fragments.frag_gitreport import GitReportInfo


# Commit hook
def h_execute_commit(parser, commit_action_args):
    # Parse arguments
    result = parser.parse_args(commit_action_args)
    if (result.verbose):
        print("%r %r %s %s %s %r %s %s\n\n%s" % (result.verbose,
                                                 result.dry,
                                                 result.summary,
                                                 result.type,
                                                 result.attributes,
                                                 result.assisted,
                                                 result.assistant,
                                                 result.backport_commits,
                                                 result.body))

    # Get the report info
    git_info = GitReportInfo()

    # Untracked files
    submodules = git_info.submodules
    proj_repo_untracked_files = git_info.untracked_files
    if (result.verbose):
        print("untracked_count: %r" % (len(proj_repo_untracked_files)))
    for untracked in proj_repo_untracked_files:
        if any(untracked == sm.module().working_tree_dir
               or untracked.startswith(sm.module().working_tree_dir + os.sep)
               for sm in submodules):
            continue
        if not result.dry:
            git_info.index.add(untracked)

    # Repo index
    proj_repo_index = git_info.index
    changes = proj_repo_index.diff(None)
    for change in changes:
        # Check if we're dealing with submodules
        source_is_submodule = any(
            change.a_path == sm.module().working_tree_dir
            or change.a_path.startswith(sm.module().working_tree_dir + os.sep)
            for sm in submodules
        )
        target_is_submodule = any(
            change.b_path == sm.module().working_tree_dir
            or change.b_path.startswith(sm.module().working_tree_dir + os.sep)
            for sm in submodules
        )

        # Now, handle the changes
        match (change.change_type):
            case "A":
                if not target_is_submodule:
                    if not result.dry:
                        git_info.index.add(change.b_path)
            case "D":
                if not source_is_submodule:
                    if not result.dry:
                        git_info.index.remove(change.a_path)
            case "R":
                if not source_is_submodule:
                    if not result.dry:
                        git_info.index.remove(change.a_path)
                if not target_is_submodule:
                    if not result.dry:
                        git_info.index.add(change.b_path)
            case "M":
                if not target_is_submodule:
                    if not result.dry:
                        git_info.index.add(change.b_path)
            case "T":
                if not target_is_submodule:
                    if not result.dry:
                        git_info.index.add(change.b_path)

    # Make a commit summary
    commit_attrs = list(result.attributes.split("/")) \
        if result.attributes else []
    full_summary = (result.type + ' - ' + commit_attrs.join("|")) \
        if commit_attrs else result.type
    full_summary = full_summary + ' - ' + result.summary
    final_summary = (full_summary[:50] + '...') \
        if len(full_summary) > 50 else full_summary
    remnant_summary = ('...' + full_summary[50:]) \
        if len(full_summary) > 50 else None

    # Wrap the commit body
    final_body = ""
    if (remnant_summary):
        final_body = final_body + "\n" + remnant_summary + "\n\n"
    final_body = final_body + ((result.body + "\n") if result.body else '')
    if (result.backport_commits):
        backported_commits = list(result.backport_commits.split("/"))
        final_body = final_body + "\n---\n\n" + \
            "The following commits or tags are used for this " + \
            "backport:\n"
        for backported_commit in backported_commits:
            final_body = final_body + backported_commit + "\n"
    final_body = final_body + "\n---\n\n" + \
        "Type: " + result.type + "\n" + \
        "Breaking: " + \
        ("Yes" if 'brk' in commit_attrs else "No") + "\n" + \
        "Doc Required: " + \
        ("Yes" if 'doc' in commit_attrs else "No") + "\n" + \
        "Backport Required: " + \
        ("Yes" if 'bkp' in commit_attrs else "No") + "\n" + \
        "AI Assisted: " + \
        (("Yes (assisted by " + result.assistant + ")")
         if result.assisted else "No") + "\n" + \
        "Part: 1/1"
    final_body = '\n'.join(
            ['\n'.join(textwrap.wrap(line,
                                     width=80,
                                     replace_whitespace=False))
             for line in final_body.splitlines()])

    # Make a commit
    final_message = final_summary + "\n\n" + final_body
    if not result.dry:
        git_info.index.commit(final_summary + "\n\n" + final_body)
    else:
        print(final_message)
