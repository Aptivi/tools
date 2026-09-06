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
from common.fragments.frag_gitactions import gitaction_pushtoremote
import os
import textwrap

# Configuration module
import adt_conf

# Git report info class
from common.fragments.frag_gitreport import GitReportInfo

# Valid attributes and types
valid_types = ['add', 'fix', 'rem', 'imp', 'ref', 'upd', 'doc', 'dev', 'dcp',
               'fin', 'chg', 'int', 'bkp', 'prj', 'pkg', 'und']
valid_attrs = ['brk', 'sec', 'prf', 'reg', 'doc', 'ptp', 'prt', 'bkp']


# Commit hook
def h_execute_commit(arguments: tuple[Namespace, list[str]]):
    result = arguments[0]
    if (adt_conf.verbose):
        print("%r %s %s %s %r %s %s %i %i %r %s\n\n%s" % \
            (result.dry,
             result.summary,
             result.type,
             result.attributes,
             result.assisted,
             result.assistant,
             result.backport_commits,
             result.part_number,
             result.part_total,
             result.push,
             result.remote,
             result.body))

    # Get the report info
    git_info = GitReportInfo()

    # Add remaining changes
    if not result.dry:
        git_info.repo.git.add(A=True)
    
    # Check for attribute and type validity
    commit_attrs = list(result.attributes.split("/")) \
        if result.attributes else []
    if not result.type in valid_types:
        raise TypeError("Invalid type %s" % result.type)
    if any(not attr in valid_attrs for attr in commit_attrs):
        raise TypeError("Invalid attrs %s" % commit_attrs)
    
    # Check for attribute compatibility
    if (adt_conf.verbose):
        print("attrs: %s" % (commit_attrs))
    if ('bkp' in commit_attrs):
        # bkp is incompatible with rem, dev, dcp, and fin types
        if (result.type == 'rem' or \
            result.type == 'dev' or \
            result.type == 'dcp' or \
            result.type == 'fin'):
            raise TypeError("bkp is incompatible with type %s" % result.type)
        
        # bkp is incompatible with ptp and brk attributes
        if ('ptp' in commit_attrs or \
            'brk' in commit_attrs):
            raise TypeError("bkp is incompatible with attr %s" % commit_attrs)
    
    # Check for description requirement
    if (result.type == 'add' or \
        result.type == 'fix' or \
        result.type == 'rem' or \
        result.type == 'imp' or \
        result.type == 'doc' or \
        result.type == 'bkp'):
        if (not result.body):
            raise ValueError("Body not provided for %s" % result.type)
    
    # Parse part numbers and check it
    part_num = int(result.part_number)
    part_total = int(result.part_total)
    if (part_num > part_total) or (part_num < 1) or (part_num < 1):
        raise ValueError("Part number is invalid or exceeds total: %i %i" % \
                         (part_num, part_total))

    # Make a commit summary
    full_summary = (result.type + ' - ' + "|".join(commit_attrs)) \
        if commit_attrs else result.type
    full_summary = full_summary + ' - ' + result.summary
    final_summary = (full_summary[:50] + '...') \
        if len(full_summary) > 50 else full_summary
    remnant_summary = ('...' + full_summary[50:]) \
        if len(full_summary) > 50 else None

    # Wrap the commit body
    final_body = ""
    if (remnant_summary):
        final_body = final_body + remnant_summary + "\n\n"
    final_body = final_body + \
        (("---\n\n" + result.body + "\n\n") if result.body else '')

    # Check to see if there are backported commits
    if (result.backport_commits):
        backported_commits = list(result.backport_commits.split("/"))
        final_body = final_body + "---\n\n" + \
            "The following commits or tags are used for this " + \
            "backport:\n"
        for backported_commit in backported_commits:
            final_body = final_body + "  - " + backported_commit + "\n"
        final_body = final_body + "\n"
    
    # Add the footer
    final_body = final_body + "---\n\n" + \
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
        ("Part: %i/%i" % (part_num, part_total))

    # Wrap the lines
    final_body = '\n'.join(
            ['\n'.join(textwrap.wrap(line,
                                     width=80,
                                     replace_whitespace=False))
             for line in final_body.splitlines()])

    # Make a commit
    final_message = final_summary + "\n\n" + final_body
    if not result.dry:
        if (adt_conf.verbose):
            print(final_message)
        git_info.index.commit(final_summary + "\n\n" + final_body)
    else:
        print(final_message)

    # Push if necessary
    if result.push:
        if not result.dry:
            gitaction_pushtoremote(result)
        else:
            print('\nWould push this commit')
