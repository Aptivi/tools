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
import sys
import os
import traceback

# Get the project root
from common.fragments.frag_gitreport import GitReportInfo


# Report make hook
def h_execute_intreport(arguments):
    result = arguments[0]
    if (result.verbose):
        print("%r | %r %s | %r %s (%s %i %s %s %s)" %
              (result.verbose,
               result.local, result.local_path,
               result.remote, result.remote_path,
               result.server_host, result.server_port,
               result.server_username, result.server_password,
               result.server_privkey))
 
    # Get the report info
    git_info = GitReportInfo()

    # Return the report
    git_report = git_info.generate_report()
    if (result.verbose):
        print(git_report)
        print("\n\nReport size: %i bytes" % (len(git_report)))

    # Check the upload type
    is_local = result.local
    is_remote = result.remote
    if (result.verbose):
        print("Local: %r, Remote: %r" % (result.local, result.remote))
    if (not (is_local | is_remote) | (is_local & is_remote)):
        print('Specify either -l (local upload) or -r (remote upload)')
        sys.exit(1)
    
    # Determine how to upload the report
    if (is_local):
        # Local upload. Check the local path directory
        local_path = result.local_path
        if local_path is None:
            local_path = \
                f"{os.environ["LOCALAPPDATA"]}\\Aptivi\\ADT\\Reports" \
                if os.name == 'nt' else "/usr/local/share/aptdev"
        if not (os.path.isdir(local_path)):
            if (result.verbose):
                print('Creating local path %s.' % local_path)
            os.makedirs(local_path)
        
        # Upload the report
        report_file_path = os.path.abspath(
            local_path + '/' + git_report['filename'])
        if (result.verbose):
            print('Opening report file %s.' % report_file_path)
        with open(report_file_path, "w") as report_file:
            print('Writing report to %s...' % report_file_path)
            report_file.write(git_report['report'])
        print('Written report to %s!' % report_file_path)
    elif (is_remote):
        # Remote upload. Attempt to connect to server
        import paramiko
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if (result.verbose):
            print('Private key auth: %s' % result.server_privkey)
        try:
            if result.server_privkey is not None:
                ssh_client.connect(result.server_host,
                                   port=result.server_port,
                                   username=result.server_username,
                                   key_filename=result.server_privkey)
            else:
                ssh_client.connect(result.server_host,
                                   port=result.server_port,
                                   username=result.server_username,
                                   password=result.server_password)
            
            # Open SFTP
            if (result.verbose):
                print('Opening SFTP to %s@%s:%s' % (result.server_username,
                                                    result.server_host,
                                                    result.server_port))
            sftp_client = ssh_client.open_sftp()

            # Upload the report
            report_path = result.remote_path + '/' + git_report['filename']
            if (result.verbose):
                print('Opening report file %s.' % report_path)
            with sftp_client.open(report_path, 'w') as report_file:
                print('Writing report to %s...' % report_path)
                report_file.write(git_report['report'])
            print('Written report to %s!' % report_path)
        except Exception as exc:
            print('Failed to upload report')
            traceback.print_exception(exc)
        finally:
            ssh_client.close()
