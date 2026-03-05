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

# Import necessary components
import os
from common.fragments.frag_dnresxlang import \
    drl_add_culture, drl_add_loc, drl_add_lang, \
    drl_delete_culture, drl_delete_loc, drl_delete_lang, \
    drl_edit_culture, drl_edit_loc, \
    drl_report, \
    drl_save


# .NET .resx langauge tools hook
def h_execute_dnresxlang(parser, dnresxlang_action_args):
    # Parse arguments
    result = parser.parse_args(dnresxlang_action_args)
    if (result.verbose):
        print("%r %s "
              "(A: %r %r %r) "
              "(C: %s) "
              "(D: %r %r %r) "
              "(E: %r %r) "
              "(Lo: %s) "
              "(Los: %s) "
              "(La: %s) "
              "(Rep: %r) "
              "(Res: %s) "
              "(S: %r)" %
              (result.verbose,
               result.json_path,
               result.add_culture, result.add_loc, result.add_lang,
               f'[{', '.join(result.cultures or [])}]',
               result.delete_culture, result.delete_loc, result.delete_lang,
               result.edit_culture, result.edit_loc,
               f'[{', '.join(result.localization or [])}]',
               result.localization_strs,
               result.language,
               result.report,
               result.resx_path,
               result.save))
 
    # Check the JSON path
    if not os.path.isdir(result.json_path):
        raise NotADirectoryError(f"JSON path {result.json_path} "
                                  "is not a directory")
    
    # Specify the action by variables
    if (result.add_culture):
        drl_add_culture(result.json_path,
                        result.language, result.cultures)
    elif (result.add_loc):
        drl_add_loc(result.json_path,
                    result.language, result.localization_strs)
    elif (result.add_lang):
        drl_add_lang(result.json_path,
                     result.language, result.cultures)
    elif (result.delete_culture):
        drl_delete_culture(result.json_path,
                           result.language, result.cultures)
    elif (result.delete_loc):
        drl_delete_loc(result.json_path,
                       result.language, result.localization)
    elif (result.delete_lang):
        drl_delete_lang(result.json_path,
                        result.language, result.cultures)
    elif (result.edit_culture):
        drl_edit_culture(result.json_path,
                         result.language, result.cultures)
    elif (result.edit_loc):
        drl_edit_loc(result.json_path,
                     result.language, result.localization_strs)
    elif (result.report):
        drl_report(result.json_path,
                   result.language)
    elif (result.save):
        drl_save(result.json_path,
                 result.resx_path)
