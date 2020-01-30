@echo off
color f2

G:
cd ../

echo start...
for /r ./ %%i in (*.7z) do (
7z -e -pwww.hrka.cc %%i
del %%i
echo %%i rar success!
)
pause>nul