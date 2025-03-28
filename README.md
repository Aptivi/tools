## Build Tools

This repository contains the extensible build tools used for Aptivi projects.
Those tools are written with Bash for Linux and macOS and with Batch for
Windows to allow cross-platform support and to make building the projects
more flexible due to its extensibility.

The following structure is required for every project that uses this build
toolset:

  * Project directory
    * `tools` (directory, cloned as a git submodule for this repo)
      * `build.cmd` (file, Build script for Windows)
      * `build.sh` (file, Build script for Linux and macOS)
      * `docgen.cmd` (file, Documentation generation script for Windows)
      * `docgen.sh` (file, Documentation generation script for Linux and macOS)
      * `docgen-pack.cmd` (file, Documentation packing script for Windows)
      * `docgen-pack.sh` (file, Documentation packing script for Linux and macOS)
      * `pack.cmd` (file, Artifact packing script for Windows)
      * `pack.sh` (file, Artifact packing script for Linux and macOS)
      * `push.cmd` (file, Artifact pushing script for Windows)
      * `push.sh` (file, Artifact pushing script for Linux and macOS)
    * `vnd` (directory, you'll have to create the below files and this directory yourself)
      * `vendor.sh` (file, vendor script for Linux and macOS)
      * `vendor-build.cmd` (file, list of commands for build for Windows)
      * `vendor-docgen.cmd` (file, list of commands for documentation generation for Windows)
      * `vendor-docpack.cmd` (file, list of commands for documentation packing for Windows)
      * `vendor-pack.cmd` (file, list of commands for artifact packing for Windows)
      * `vendor-push.cmd` (file, list of commands for pushing to package registry for Windows)

For Windows scripts, you can optionally add new files that have a prefix of
either `vendor-pre` or `vendor-post` for all actions, such as
`vendor-prebuild.cmd` for pre-build actions, or `vendor-postpack.cmd` for
post-pack actions.

How the project calls the build scripts is entirely up to the project and not
to a standard Makefile file that makes use of those scripts found in the tools
directory.

## Installing the tools

At the root of a project, you can use the Git submodules to clone this
repository to the `tools` directory, assuming that it doesn't exist:

```shell
$ git submodule add https://github.com/Aptivi/tools
$ git add .
$ git commit -m "message..."
$ git push
```

## Vendor scripts

The following vendor scripts are provided for both Windows and Unix-based
operating systems, such as macOS:

### Windows

For Windows systems, you'll have to create the vendor batch files as mentioned
underneath the `vnd` directory as needed. For example, if you don't want to
push anything to the package registry, you can omit the `vendor-push.cmd` file
and the base push script, `push.cmd`, will not see it.

Inside those batch files, the least you'll need is this:

```bat
@echo off

set ROOTDIR=%~dp0\..

REM Your commands here
```

For example, BassBoom has a vendor script for building the project, called
`vendor-build.cmd`, that is defined like this:

```bat
@echo off

REM This script builds and packs the artifacts.
set releaseconfig=%1
if "%releaseconfig%" == "" set releaseconfig=Release

set buildoptions=%*
call set buildoptions=%%buildoptions:*%1=%%
if "%buildoptions%" == "*=" set buildoptions=

REM Turn off telemetry and logo
set DOTNET_CLI_TELEMETRY_OPTOUT=1
set DOTNET_NOLOGO=1

set ROOTDIR=%~dp0\..

echo Building with configuration %releaseconfig%...
"%ProgramFiles%\dotnet\dotnet.exe" build "%ROOTDIR%\BassBoom.sln" -p:Configuration=%releaseconfig% %buildoptions%
```

You can process the arguments as usual, because the scripts found in the
`tools` directory handle the arguments to customize the build further by the
end developer.

### Linux/macOS

For Linux and macOS systems, you'll have to create a single executable Bash
script, called `vendor.sh` under the `vnd` folder. This is meant to be only
sourced and not to be executed. It contains only the function definitions that
can be omitted:

  - prebuild()
  - build()
  - postbuild()
  - predocgenerate()
  - docgenerate()
  - postdocgenerate()
  - predocpack()
  - docpack()
  - postdocpack()
  - prepackall()
  - packall()
  - postpackall()
  - prepushall()
  - pushall()
  - postpushall()

If a function has been omitted, they will be defined as a void function that
immediately returns `0`, which means success. Those functions, therefore, will
not be executed. Inside them, you can define what commands you can run.

The best practice for making vendor scripts is to follow the below rules:

  - For critical errors, you can use the `checkerror` function directly after
    the command to be executed that may throw such errors, such as
    dependencies.
  - For continuable errors, you can use the `checkvendorerror` function
    directly after the command to be executed that may throw such errors, such
    as download errors.
  - You can use the `$ROOTDIR` variable to get a path to the repository root,
    that is, the parent directory of the vendor script directory, `vnd`.

Afterwards, you can define the functions inside the `vendor.sh` file:

```bash
#!/bin/bash

prebuild() {
    # Your commands here (can be omitted)
}

build() {
    # Your commands here (can be omitted)
}

postbuild() {
    # Your commands here (can be omitted)
}

# ...and so on.
```

For example, BassBoom defines the build function like this:

```bash
#!/bin/bash

build() {
    # Determine the release configuration
    releaseconf=$1
    if [ -z $releaseconf ]; then
	    releaseconf=Release
    fi

    # Now, build.
    echo Building with configuration $releaseconf...
    "$dotnetpath" build "$ROOTDIR/BassBoom.sln" -p:Configuration=$releaseconf ${@:2}
    checkvendorerror $?
}
```

You can process the arguments as usual, because the scripts found in the
`tools` directory handle the arguments to customize the build further by the
end developer. Beware that the vendor script should contain the shebang at the
top of the script.
