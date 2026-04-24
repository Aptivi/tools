#!/usr/bin/env python3

# [configurable] adt_conf.on_self:
#     Causes ADT to search for .git in ADT repo instead of project repo.
on_self = False

# [automatic]    adt_conf.project_path:
#     Lets ADT operate on a specified project path that is automatically 
#     filled by the tool as soon as the script starts.
project_path = ""

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


# Safeguard for those trying to run this script
if __name__ == "__main__":
    print("Hmmm... it's a state machine for ADT. Did you mean to run adt.py?")
