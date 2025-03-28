@echo off

set ROOTDIR=%~dp0\..

REM Run any vendor actions before pack
if exist %ROOTDIR%\vnd\vendor-prepack.cmd (
   call %ROOTDIR%\vnd\vendor-prepack.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions on pack
if exist %ROOTDIR%\vnd\vendor-pack.cmd (
   call %ROOTDIR%\vnd\vendor-pack.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions after pack
if exist %ROOTDIR%\vnd\vendor-postpack.cmd (
   call %ROOTDIR%\vnd\vendor-postpack.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Inform success
echo Pack successful
goto :finished

:failure
exit /B %errorlevel%

:finished
