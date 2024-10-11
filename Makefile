#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = wuai
ENV_NAME = wuai-beta
PYTHON_VERSION = 3.11
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Install Python Dependencies
.PHONY: requirements
requirements:
	conda env update --name $(ENV_NAME) --file environment.yml --prune


# conda activate $(PROJECT_NAME)
# python -m pip install -e .
#	conda env update --name $(PROJECT_NAME) --file environment.yml --prune -v

#conda env export —from-history > environment.yml --no-builds 		
#	# from history makes it cross platform
#To automate a backup of the current environment run:
#	# conda env export > environment.yml



## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


## Lint using flake8 and black (use `make format` to do formatting)
.PHONY: lint
lint:
	flake8 $(MODULE_NAME)
	isort --check --diff --profile black $(MODULE_NAME)
	black --check --config pyproject.toml $(MODULE_NAME)


## Format source code with black
.PHONY: format
format:
	black --config pyproject.toml $(MODULE_NAME)



## Set up python interpreter environment
.PHONY: create_environment
create_environment:
	conda env create --name $(ENV_NAME) -f environment.yml
	
	@echo ">>> conda env created. Activate with:\nconda activate $(ENV_NAME)"
	



#################################################################################
# PROJECT RULES                                                                 #
#################################################################################


## Make Dataset
.PHONY: data
data: requirements
	$(PYTHON_INTERPRETER) confcpt/dataset.py


#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
