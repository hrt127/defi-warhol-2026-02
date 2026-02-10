# DeFi Warhol Airdrop Farm Makefile

PYTHON = python3
SCRIPTS_DIR = scripts
DATA_DIR = data
LOGS_DIR = $(DATA_DIR)/logs

.PHONY: init rank log summary clean log-wallet by-wallet add-protocol

# Initialize the project
init:
	mkdir -p $(DATA_DIR) $(LOGS_DIR) $(SCRIPTS_DIR) docs/protocols config prompts outputs
	@echo "Project initialized. Data and log directories created."

# Rank all projects based on the scoring script
rank:
	$(PYTHON) $(SCRIPTS_DIR)/score_projects.py

# Primary automation execution (Alias for rank in this project)
run-all: rank

# Log a farm action (Classic)
# Usage: make log protocol="Moca Network" action="Completed verification" tx="" size="0"
log:
	$(PYTHON) $(SCRIPTS_DIR)/farm_log.py add "$(protocol)" "$(action)" "" "$(tx)" "$(size)"

# Log with wallet tracking
# Usage: make log-wallet protocol="Moca Network" action="Claimed points" wallet="0x123" tx="0xabc" size="0"
log-wallet:
	$(PYTHON) $(SCRIPTS_DIR)/farm_log.py add "$(protocol)" "$(action)" "$(wallet)" "$(tx)" "$(size)"

# View actions by wallet
by-wallet:
	$(PYTHON) $(SCRIPTS_DIR)/farm_log.py by-wallet

# Check farm summary
summary:
	$(PYTHON) $(SCRIPTS_DIR)/farm_log.py summary

# Add new protocol (interactive)
add-protocol:
	@echo "Creating protocol from template..."
	@read -p "Protocol name: " name; \
	echo "Creating docs/protocols/$$name.md"; \
	sed "s/PROTOCOL_NAME/$$name/g" prompts/protocol_template.md > docs/protocols/$$name.md

# Clean temporary files (none currently, but standard for Dojo)
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "Cleaned up pycache."
