# Makefile for CeleraOne Base Application

SHELL := /bin/bash
export PYTHONUNBUFFERED := 1
export BASE := $(shell /bin/pwd)

PY_VERSION := 3
PYTHON := $(shell /usr/bin/which python$(PY_VERSION))
VENV_BIN := $(BASE)/../.venv/bin
VPYTHON := $(VENV_BIN)/python
VIRTUALENV := $(PYTHON) -m virtualenv
PIP := $(VENV_BIN)/pip
APP_VERSION := $(shell cat $(BASE)/VERSION)
PROTO_OUT := $(BASE)/grpc_proto

.DEFAULT_GOAL := build

.PHONY: build
build: var
	$(VIRTUALENV) $(BASE)/../.venv
	$(PIP) \
		--isolated \
		--disable-pip-version-check \
		--no-cache-dir \
		install -r requirements.txt

.PHONY: var
var:
	mkdir -p "$(BASE)/var/log/webapp" "$(BASE)/var/run/webapp"

.PHONY: clean
clean:
	rm -rf "$(BASE)/../.venv"
	rm -rf "$(BASE)/../var"

.PHONY: protbuf.generate
protobuf.generate:
	cd $(PROTO_OUT) && $(VPYTHON) codegen.py

.PHONY: server.run
server.run:
	$(VENV_BIN)/grpc-server

.PHONY: client.run
client.run:
	$(VENV_BIN)/grpc-client

.PHONY: requirements.txt
requirements.txt:
	$(PIP) freeze > requirements.txt
