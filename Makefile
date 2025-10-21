# VIA Makefile for Linux/macOS
# Copyright (c) 2025 BEP Venture UG

BUILD_TYPE ?= Release
BUILD_DIR = cmake-build-$(shell echo $(BUILD_TYPE) | tr A-Z a-z)

.PHONY: all configure build install clean

all: configure build

configure:
	@mkdir -p $(BUILD_DIR)
	@cd $(BUILD_DIR) && cmake -DCMAKE_BUILD_TYPE=$(BUILD_TYPE) ..

build:
	@cd $(BUILD_DIR) && cmake --build . --config $(BUILD_TYPE)

install:
	@cd $(BUILD_DIR) && cmake --install . --config $(BUILD_TYPE)

clean:
	@rm -rf $(BUILD_DIR)
