@echo off
setlocal enabledelayedexpansion

set ROOTDIR=%~dp0
set "ARGUMENTS=%*"

call "%ROOTDIR%\common.cmd" clean !ARGUMENTS!
