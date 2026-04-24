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
import sys
import adt_conf


def frag_pt_getprojectroot(self: bool):
    abs_path = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(abs_path + '/../../' + \
            ('' if self else '../'))
    return project_root


def frag_pt_addvendor():
    adt_conf.vendor_path = adt_conf.project_path + '/vendor/'
    if not (os.path.isdir(adt_conf.vendor_path)):
        print('Vendor directory doesn\'t exist.')
        sys.exit(2)
    sys.path.append(adt_conf.vendor_path)


def frag_pt_checkvendoraction(action):
    if action != adt_conf.action:
        print("Action is inconsistent! ['%s' vs. '%s']" \
            % (action, adt_conf.action))
        sys.exit(4)
    vendor_script_dir = adt_conf.vendor_path + 'vnd_' + action + '.py'
    if not (os.path.isfile(vendor_script_dir)):
        print('%s vendor script doesn\'t exist. Doing nothing...' % (action))
        sys.exit(3)


def frag_pt_preparevendor():
    print('Preparing vendor env config for %s...' % (adt_conf.action))
    frag_pt_addvendor()
    frag_pt_checkvendoraction(adt_conf.action)
