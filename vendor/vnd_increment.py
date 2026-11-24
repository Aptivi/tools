import os
import datetime


class VersionInfo():
    def __init__(self, old_version, new_version):
        # Nitrocid version
        self.old_version = old_version
        self.new_version = new_version
        self.old_version_split = self.old_version.split('.')
        self.new_version_split = self.new_version.split('.')
        self.old_major = \
            f'{self.old_version_split[0]}.' \
            f'{self.old_version_split[1]}.' \
            f'{self.old_version_split[2]}'
        self.new_major = \
            f'{self.new_version_split[0]}.' \
            f'{self.new_version_split[1]}.' \
            f'{self.new_version_split[2]}'


def vnd_increment(old_version, new_version, api_versions):
    time = datetime.datetime.now()
    solution = os.path.dirname(os.path.abspath(__file__ + '/../'))

    # Get old and new API versions and split them
    version = VersionInfo(old_version, new_version)

    # Replace the version in the CHANGES.TITLE file
    changes_title_file = f"{solution}/CHANGES.TITLE"
    changes_title_lines = []
    with open(changes_title_file) as changes_title_stream:
        changes_title_lines = changes_title_stream.readlines()
    changes_title_lines[0] = changes_title_lines[0].replace(old_version,
                                                            new_version)
    with open(changes_title_file, 'w') as changes_title_stream:
        changes_title_stream.writelines(changes_title_lines)

    # Replace the version in several files
    main_code_files = {
        f"{solution}/src/adt/adt_conf.py",
        f"{solution}/pyproject.toml",
        f"{solution}/pyproject-olderpy.toml",
    }
    for main_code_file in main_code_files:
        main_code_lines = []
        with open(main_code_file) as main_code_stream:
            main_code_lines = main_code_stream.readlines()
        main_code_lines = process_main_code_lines(main_code_lines, version)
        with open(main_code_file, 'w') as main_code_stream:
            main_code_stream.writelines(main_code_lines)
    
    # Replace the versions in the GitHub Actions workflows
    workflows = {
        f"{solution}/.github/workflows/build-ppa-package-with-lintian.yml",
        f"{solution}/.github/workflows/build-ppa-package.yml",
        f"{solution}/.github/workflows/build-ppa.yml",
        f"{solution}/.github/workflows/pushamend.yml",
        f"{solution}/.github/workflows/pushppa.yml",
    }
    for workflow in workflows:
        workflow_lines = []
        with open(workflow) as workflow_stream:
            workflow_lines = workflow_stream.readlines()
        workflow_lines = process_misc_lines(workflow_lines, version)
        with open(workflow, 'w') as workflow_stream:
            workflow_stream.writelines(workflow_lines)
    
    # Add a Debian changelog entry
    debian_changes_file = f"{solution}/debian/changelog"
    debian_changes_time = time.strftime("%a, %d %b %Y %H:%M:%S") + ' ' + \
        time.now(datetime.timezone.utc).astimezone().strftime("%z")
    debian_changes_entry = f"""adt ({version.new_version}-1) noble; urgency=medium

  * Please populate changelogs here

 -- Aptivi CEO <ceo@aptivi.anonaddy.com>  {debian_changes_time}
"""
    with open(debian_changes_file, 'r') as debian_changes_stream:
        debian_changes_entry = debian_changes_entry + "\n" + \
            debian_changes_stream.read()
    with open(debian_changes_file, 'w') as debian_changes_stream:
        debian_changes_stream.write(debian_changes_entry)


def process_misc_lines(lines, version: VersionInfo):
    for num in range(0, len(lines)):
        is_oldver = version.old_version in lines[num]
        if is_oldver:
            lines[num] = \
                lines[num].replace(version.old_version,
                                   version.new_version)
    return lines


def process_main_code_lines(lines, version: VersionInfo):
    for num in range(0, len(lines)):
        is_oldver = "version = '" + version.old_version + "'" in lines[num]
        is_oldver_dq = 'version = "' + version.old_version + '"' in lines[num]
        if is_oldver or is_oldver_dq:
            lines[num] = \
                lines[num].replace(version.old_version,
                                   version.new_version)
    return lines
