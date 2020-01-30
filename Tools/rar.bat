@echo off
color f2
set /p disk=input disk symbol:
%disk%
set /p path=input file path:
cd %path%
echo start...
for /r ./ %%i in (*.7z) do (
D:\WinRAR\WinRAR -pwww.hrka.cc %%i
del %%i
echo %%i rar success!
)
pause>nul