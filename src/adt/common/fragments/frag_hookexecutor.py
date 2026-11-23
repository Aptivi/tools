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

# Configuration module
import sys

import adt_conf

# Processing the arguments
import argparse
import importlib
from common.fragments.frag_projecttools import frag_pt_preparevendor


def frag_hookexecutor_exec(parser: argparse.ArgumentParser,
                           action_args: list[str],
                           prepare_vendor: bool = False):
    vnd_module = importlib.import_module(f'common.hooks.h_{adt_conf.action}')
    arguments = parser.parse_known_args(action_args)
    if (prepare_vendor):
        frag_pt_preparevendor()
    vnd_module.h_execute(arguments)


def frag_hookexecutor_execcustom(action_args: list[str]):
    frag_pt_preparevendor()
    vnd_module = importlib.import_module(f'vnd_{adt_conf.action}')
    vnd_module.vnd_action(action_args)
