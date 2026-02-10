# DeFi Warhol Airdrop Farm Makefile

PYTHON = python3
SCRIPTS_DIR = scripts
DATA_DIR = data
LOGS_DIR = $(DATA_DIR)/logs

.PHONY: init rank log summary clean

# Initialize the project
init:
	mkdir -p $(DATA_DIR) $(LOGS_DIR) $(SCRIPTS_DIR) docs/protocols config prompts outputs
	@echo "Project initialized. Data and log directories created."

# Rank all projects based on the scoring script
rank:
	$(PYTHON) $(SCRIPTS_DIR)/score_projects.py

# Primary automation execution (Alias for rank in this project)
run-all: rank

# Log a farm action
# Usage: make log protocol="Moca Network" action="Completed verification" tx="" size="0"
log:
	$(PYTHON) $(SCRIPTS_DIR)/farm_log.py add "$(protocol)" "$(action)" "$(tx)" "$(size)"

# Check farm summary
summary:
	$(PYTHON) $(SCRIPTS_DIR)/farm_log.py summary

# Clean temporary files (none currently, but standard for Dojo)
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "Cleaned up pycache."
