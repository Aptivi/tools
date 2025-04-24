@echo off

set ROOTDIR=%~dp0
call %ROOTDIR%\common.cmd build %*
