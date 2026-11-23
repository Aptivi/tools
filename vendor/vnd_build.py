import os
import subprocess


def vnd_build(args, extra_args):
    solution = os.path.dirname(os.path.abspath(__file__ + '/../'))
    command = f"pyproject-build {args if args else ''} \"{solution}\""
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        raise Exception("Build failed with code %i" % (result.returncode))
