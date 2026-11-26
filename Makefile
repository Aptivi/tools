ROOT_DIR := $(shell dirname "$(realpath $(lastword $(MAKEFILE_LIST)))")

.PHONY: all install

all:
	$(MAKE) invoke-build ENVIRONMENT=Release BUILDARGS="$(BUILDARGS)"

build-noadt:
	pyproject-build "$(BUILDARGS)" "$(ROOT_DIR)"

invoke-build:
	adt build -b "$(BUILDARGS)"

clean:
	adt clean

install-pip:
	pipx install "$(ROOT_DIR)"/dist/aptivi_adt*.whl

install:
	python -m installer --destdir="$(DESTDIR)" "$(ROOT_DIR)"/dist/aptivi_adt*.whl
