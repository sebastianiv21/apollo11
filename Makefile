# Makefile

# Variables
FLAKE8 := flake8
AUTOPEP8 := autopep8

# Directorios
SRC_DIR := src
TESTS_DIR := tests

# Archivos a verificar
PY_FILES := $(wildcard $(SRC_DIR)/*.py) $(wildcard $(TESTS_DIR)/*.py)

.PHONY: lint format

lint:
	$(FLAKE8) $(PY_FILES)

format:
	$(AUTOPEP8) --in-place --recursive $(SRC_DIR) $(TESTS_DIR)

# Agrega más reglas según sea necesario para tu proyecto
