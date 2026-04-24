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

from datetime import datetime
import os

# Get project root
from git import Repo
import adt_conf


# Class that contains Git info for a project
class GitReportInfo():
    def generate_report(self):
        # Get current date and time
        current_time = datetime.now()

        # Generate the report file name
        filename = 'apt-dev-report-' + \
            self.project_name + '-' + \
            current_time.strftime('%Y-%m%d-%H%M%S%f') + '.txt'

        # Generate the report header
        report = f"Git report for {self.project_name}\n" + \
                 f"Generated on {current_time}\n\n" + \
                 "------------\n\n"
        
        # Generate the report
        report = report + "General information\n\n"
        report_dict = {
            'Active branch:': self.active_branch,
            'Head commit:': self.head.commit.hexsha,
            'Head commit message:': self.head.commit.summary,
            'Index version:': self.index.version,
            'Index entries:': len(self.index.entries),
            'Branches count:': len(self.branches),
            'Tags count:': len(self.tags),
            'Commits count:': len(self.commits),
            'Untracked files count:': len(self.untracked_files),
        }
        stringified_dict = [f'{key:24} {value}'
                            for key, value in report_dict.items()]
        report = report + '\n'.join(stringified_dict)
        report = report + "\n\n"

        if (len(self.branches) > 0):
            # Generate the branches list
            report = report + "Branches list\n\n"
            for branch in self.branches:
                report = report + f'{branch.name:32}   ' + \
                                f'[{branch.commit.hexsha} ' + \
                                f'{branch.commit.summary}]\n'
            report = report + "\n\n"

        if (len(self.tags) > 0):
            # Generate the tags list
            report = report + "Tags list\n\n"
            for tag in self.tags:
                report = report + f'{tag.name:32}   ' + \
                                f'[{tag.commit.hexsha} ' + \
                                f'{tag.commit.summary}]\n'
            report = report + "\n\n"

        if (len(self.commits) > 0):
            # Generate the commits list
            report = report + f"Commits list for {self.active_branch}\n\n"
            for commit in self.commits:
                report = report + f'{commit.hexsha} {commit.summary}\n'
            report = report + "\n\n"

        # Check if repo is dirty
        dirty = self.repo.is_dirty()
        report = report + "Dirty: %r" % (dirty)
        report = report + "\n\n"
        if (dirty):
            if (len(self.untracked_files) > 0):
                # Generate the untracked files list
                report = report + "Untracked files list\n\n"
                for untracked_file in self.untracked_files:
                    report = report + f'{untracked_file}'
                report = report + "\n\n"

            # Generate the changes list
            report = report + "Changes list\n\n"
            for diff in self.index.diff(None):
                report = report + f'[{diff.change_type}] ' + \
                                  f'A: {diff.a_path}, ' + \
                                  f'B: {diff.b_path}'
        
        # Return the report
        return {'filename': filename, 'report': report}

    def __init__(self):
        self.repo = Repo(adt_conf.project_path)
        self.branches = self.repo.branches
        self.tags = self.repo.tags
        self.commits = list(self.repo.iter_commits())
        self.untracked_files = self.repo.untracked_files
        self.index = self.repo.index
        self.head = self.repo.head
        self.active_branch = self.repo.active_branch
        self.submodules = self.repo.submodules
        self.project_name = adt_conf.project_name
