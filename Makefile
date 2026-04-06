PYTHON = python3
MAIN = a_maze_ing.py
CONFIG = config.txt

install:
	@echo "No dependencies to install"

debug:
	$(PYTHON) -m pdb $(MAIN)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
run :
	$(PYTHON) $(MAIN) $(CONFIG)