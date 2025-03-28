@echo off

set ROOTDIR=%~dp0\..

REM Run any vendor actions before docgen pack
if exist %ROOTDIR%\vnd\vendor-predocpack.cmd (
   call %ROOTDIR%\vnd\vendor-predocpack.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions on docgen pack
if exist %ROOTDIR%\vnd\vendor-build.cmd (
   call %ROOTDIR%\vnd\vendor-build.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions after docgen pack
if exist %ROOTDIR%\vnd\vendor-postdocpack.cmd (
   call %ROOTDIR%\vnd\vendor-postdocpack.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Inform success
echo Pack successful
goto :finished

:failure
exit /B %errorlevel%

:finished
