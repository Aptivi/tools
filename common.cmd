@echo off

set ROOTDIR=%~dp0\..

REM Try to get the action name from the arguments
set ACTION=%1
if "%ACTION%" == "" set ACTION=build

set "OPTIONS=%*"
set "OPTIONS=!OPTIONS:*%1=!"

REM Run any vendor actions before %ACTION%
if exist %ROOTDIR%\vnd\vendor-pre%ACTION%.cmd (
   call %ROOTDIR%\vnd\vendor-pre%ACTION%.cmd %OPTIONS%
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions on %ACTION%
if exist %ROOTDIR%\vnd\vendor-%ACTION%.cmd (
   call %ROOTDIR%\vnd\vendor-%ACTION%.cmd %OPTIONS%
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions after %ACTION%
if exist %ROOTDIR%\vnd\vendor-post%ACTION%.cmd (
   call %ROOTDIR%\vnd\vendor-post%ACTION%.cmd %OPTIONS%
   if %errorlevel% neq 0 goto :failure
)

REM Inform success
echo Action %ACTION% successful
goto :finished

:failure
echo Action %ACTION% failed
exit /B %errorlevel%

:finished
