@echo off
REM VIA Build Script for Windows
REM Copyright (c) 2025 BEP Venture UG

set BUILD_TYPE=Release
if "%~1"=="install" goto install

if not exist cmake-build-%BUILD_TYPE% (
    echo Error: Build directory not found. Run configure.bat first.
    exit /b 1
)

cd cmake-build-%BUILD_TYPE%
cmake --build . --config %BUILD_TYPE%
cd ..
goto end

:install
cd cmake-build-%BUILD_TYPE%
cmake --install . --config %BUILD_TYPE%
cd ..

:end
