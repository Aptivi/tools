@echo off

set ROOTDIR=%~dp0\..

REM Run any vendor actions before push
if exist %ROOTDIR%\vnd\vendor-prepush.cmd (
   call %ROOTDIR%\vnd\vendor-prepush.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions on push
if exist %ROOTDIR%\vnd\vendor-push.cmd (
   call %ROOTDIR%\vnd\vendor-push.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions after push
if exist %ROOTDIR%\vnd\vendor-postpush.cmd (
   call %ROOTDIR%\vnd\vendor-postpush.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Inform success
echo Push successful
goto :finished

:failure
exit /B %errorlevel%

:finished
