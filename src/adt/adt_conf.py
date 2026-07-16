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

# [configurable] adt_conf.on_self:
#     Causes ADT to search for .git in ADT repo instead of project repo.
on_self = False

# [automatic]    adt_conf.project_path:
#     Lets ADT operate on a specified project path that is automatically 
#     filled by the tool as soon as the script starts.
project_path = ""

# [automatic]    adt_conf.project_name:
#     Name of the project that is automatically determined by basename().
project_name = ""

# [configurable] adt_conf.action:
#     Specifies the action. Filled when parsing script arguments to determine
#     which action to run.
action = ""

# [configurable] adt_conf.nobanner:
#     If enabled, ADT won't show a banner with version information and some
#     passed arguments.
nobanner = False

# [automatic]    adt_conf.vendor_path:
#     Specifies the vendor path, if it is found.
vendor_path = ""

# [configurable] adt_conf.verbose:
#     If enabled, ADT will show extra messages as the operation goes on.
verbose = False


# Safeguard for those trying to run this script
if __name__ == "__main__":
    print("Hmmm... it's a state machine for ADT. Did you mean to run adt.py?")
