@echo off

set ROOTDIR=%~dp0\..

REM Run any vendor actions before doc generation
if exist %ROOTDIR%\vnd\vendor-predocgen.cmd (
   call %ROOTDIR%\vnd\vendor-predocgen.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions on doc generation
if exist %ROOTDIR%\vnd\vendor-docgen.cmd (
   call %ROOTDIR%\vnd\vendor-docgen.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Run any vendor actions after doc generation
if exist %ROOTDIR%\vnd\vendor-postdocgen.cmd (
   call %ROOTDIR%\vnd\vendor-postdocgen.cmd %*
   if %errorlevel% neq 0 goto :failure
)

REM Inform success
echo Build successful
goto :finished

:failure
exit /B %errorlevel%

:finished
