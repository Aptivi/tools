@echo off
setlocal enabledelayedexpansion

set ROOTDIR=%~dp0
set "ARGUMENTS="
for %%A in (%*) do set "ARGUMENTS=!ARGUMENTS! %%A"
call %ROOTDIR%\common.cmd docpack !ARGUMENTS!
