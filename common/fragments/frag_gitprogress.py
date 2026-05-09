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

from git import RemoteProgress

operation_mapping = {
    RemoteProgress.CHECKING_OUT: "Checking out files",
    RemoteProgress.COMPRESSING: "Compressing Git objects",
    RemoteProgress.COUNTING: "Counting Git objects",
    RemoteProgress.FINDING_SOURCES: "Finding sources",
    RemoteProgress.RECEIVING: "Downloading Git objects from remote",
    RemoteProgress.RESOLVING: "Resolving deltas",
    RemoteProgress.WRITING: "Uploading Git objects to remote",
}


class CodeMapper():
    def get_opcode_string(self):
        # Get both the stage number and the operation number
        operation = self.op_code & RemoteProgress.OP_MASK
        stage = self.op_code & RemoteProgress.STAGE_MASK

        # Resolve operation code to name
        operation_name = operation_mapping.get(operation, f"Loading...")
        stage_name = \
            "started" if stage & RemoteProgress.BEGIN else \
            "finished" if stage & RemoteProgress.END else \
            "in progress"
        
        # Return the final mapping
        return f"{operation_name} - {stage_name}"
    
    def __init__(self, op_code: int):
        self.op_code = op_code


class ProgressFragment(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=""):
        mapper = CodeMapper(op_code)
        print("\r%s - %i of %i - %i%%%s\x1b[K"
              % (mapper.get_opcode_string(),
                 cur_count, max_count,
                 cur_count / (max_count or 100.0),
                 (" - " + message) if message else ""), end="")
