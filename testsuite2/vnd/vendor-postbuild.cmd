@echo off

set ROOTDIR=%~dp0\..

set VENDOROPTIONS=%*
echo Post-build action executed from %ROOTDIR% with options %VENDOROPTIONS%
