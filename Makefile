ROOT_DIR := $(shell dirname "$(realpath $(lastword $(MAKEFILE_LIST)))")

.PHONY: all install lite

all:
	pyproject-build

install:
	pip install $(ROOT_DIR)/dist/adt*.whl
