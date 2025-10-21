@echo off
REM VIA Configuration Script for Windows
REM Copyright (c) 2025 BEP Venture UG

set BUILD_TYPE=Release

:parse_args
if "%~1"=="" goto end_parse
if "%~1"=="--build-type=Release" set BUILD_TYPE=Release
if "%~1"=="--build-type=Debug" set BUILD_TYPE=Debug
if "%~1"=="--build-type=RelWithDebInfo" set BUILD_TYPE=RelWithDebInfo
if "%~1"=="--build-type=MinSizeRel" set BUILD_TYPE=MinSizeRel
shift
goto parse_args

:end_parse
echo Configuring VIA with build type: %BUILD_TYPE%
if not exist cmake-build-%BUILD_TYPE% mkdir cmake-build-%BUILD_TYPE%
cd cmake-build-%BUILD_TYPE%
cmake -DCMAKE_BUILD_TYPE=%BUILD_TYPE% ..
cd ..
