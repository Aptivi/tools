import os
import argparse
import subprocess


def vnd_pushbin(extra_args):
    solution = os.path.dirname(os.path.abspath(__file__ + '/../'))

    # Get extra arguments to parse for username and password
    parser = argparse.ArgumentParser(prog='adt pushbin',
                                     add_help=False)
    parser.add_argument('-u', '--username', default='__token__')
    parser.add_argument('-p', '--password')
    parsed = parser.parse_args(extra_args)

    # Push packages
    username = parsed.username
    password = parsed.password
    command = f'python3 -m twine upload --verbose ' + \
              f'--username "{username}" ' + \
              f'--password "{password}" ' + \
              f'"{solution}/dist/*"'
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        raise Exception("Push failed with code %i" % (result.returncode))
