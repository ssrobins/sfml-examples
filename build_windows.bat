@echo off
setlocal

set build_dir=build_windows

cd /d %~dp0
if not exist %build_dir% mkdir %build_dir%
cd %build_dir%

conan install .. -s arch=x86 -s compiler.runtime=MT || goto :error
cmake .. || goto :error
cmake --build . --config Release --target PACKAGE -- /m || goto :error

:error
exit /b %errorlevel%