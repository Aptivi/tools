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
import sys
import adt_conf


def t_verify_version(minimum_major: int,
                     minimum_minor: int,
                     minimum_rev: int,
                     minimum_patch: int):
    actual_version_components = adt_conf.version.split('.')
    actual_major = int(actual_version_components[0])
    actual_minor = int(actual_version_components[1])
    actual_rev = int(actual_version_components[2])
    actual_patch = int(actual_version_components[3])
    actual_version_code =  (actual_major  << 48) | (actual_minor  << 32) | (actual_rev  << 16) | actual_patch
    minimum_version_code = (minimum_major << 48) | (minimum_minor << 32) | (minimum_rev << 16) | minimum_patch
    if (actual_version_code < minimum_version_code):
        print('This vendor script requires at least ADT version ' +
              f'{minimum_major}.{minimum_minor}.{minimum_rev}.{minimum_patch}' +
              ', but you have ' +
              f'{actual_major}.{actual_minor}.{actual_rev}.{actual_patch}. ' +
              "ADT can't continue.")
        sys.exit(5)