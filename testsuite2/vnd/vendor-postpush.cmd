@echo off

set ROOTDIR=%~dp0\..

set VENDOROPTIONS=%*
echo Post-push action executed from %ROOTDIR% with options %VENDOROPTIONS%
