@echo off

set ROOTDIR=%~dp0\..

REM Run any vendor actions before localization
if exist %ROOTDIR%\vnd\vendor-prelocalize.cmd (
   call %ROOTDIR%\vnd\vendor-prelocalize.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions on localization
if exist %ROOTDIR%\vnd\vendor-localize.cmd (
   call %ROOTDIR%\vnd\vendor-localize.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions after localization
if exist %ROOTDIR%\vnd\vendor-postlocalize.cmd (
   call %ROOTDIR%\vnd\vendor-postlocalize.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Inform success
echo Localization successful
goto :finished

:failure
exit /B %errorlevel%

:finished
