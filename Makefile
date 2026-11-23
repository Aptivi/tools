ROOT_DIR := $(shell dirname "$(realpath $(lastword $(MAKEFILE_LIST)))")

.PHONY: all install

all:
	$(MAKE) invoke-build ENVIRONMENT=Release BUILDARGS="$(BUILDARGS)"

invoke-build:
	adt build -b "$(BUILDARGS)"

install:
	pip install $(ROOT_DIR)/dist/aptivi-adt*.whl
