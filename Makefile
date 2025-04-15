# VFY - Programming Exercises Verification Tool
# =============================================

NAME = vfy
INSTALL_DIR = /usr/local/bin
PROGRAM_SHARE_DIR = /usr/share/vfy
SUBJECTS_DIR = $(HOME)/.vfy/subjects
PROGRAM_DIR = $(HOME)/.vfy/program
SRC_FILES = src/__init__.py src/vfy.py src/config.py src/colors.py src/commands.py src/utils.py src/progress.py
SUBJECTS_REPO = git@github.com:mgrl39/vfydb.git

# Colors and formatting
RED    = \033[0;31m
GREEN  = \033[0;32m
YELLOW = \033[0;33m
BLUE   = \033[0;34m
PURPLE = \033[0;35m
CYAN   = \033[0;36m
WHITE  = \033[0;37m
BOLD   = \033[1m
RESET  = \033[0m

.PHONY: all install uninstall clean help setup get-subjects update-subjects

all: help

help:
	@echo "${BOLD}${CYAN}VFY${RESET} - Programming Exercises Verification Tool"
	@echo "${BOLD}===============================================${RESET}"
	@echo ""
	@echo "${BOLD}Usage:${RESET}"
	@echo "  ${YELLOW}make setup${RESET}         - Create necessary directories"
	@echo "  ${GREEN}make install${RESET}        - Install vfy system-wide"
	@echo "  ${YELLOW}make get-subjects${RESET}  - Download exercises from the subjects repository"
	@echo "  ${YELLOW}make update-subjects${RESET} - Update exercises from the subjects repository"
	@echo "  ${RED}make uninstall${RESET}      - Uninstall vfy"
	@echo "  ${BLUE}make clean${RESET}          - Remove temporary files"
	@echo ""
	@echo "${BOLD}After installation:${RESET}"
	@echo "  ${CYAN}vfy help${RESET}        - Show program help"
	@echo "  ${CYAN}vfy list${RESET}        - List all available levels"
	@echo "  ${CYAN}vfy get <level>${RESET} - Get a random exercise"
	@echo "  ${CYAN}vfy status${RESET}      - Show status of current exercise"

setup:
	@echo "${YELLOW}Setting up directory structure...${RESET}"
	@mkdir -p $(HOME)/.vfy
	@mkdir -p $(HOME)/vfy_exercises
	@echo "${GREEN}Setup complete!${RESET}"

get-subjects:
	@echo "${YELLOW}Downloading exercises from repository...${RESET}"
	@mkdir -p $(SUBJECTS_DIR)
	@if [ -d "$(SUBJECTS_DIR)/.git" ]; then \
		echo "${BLUE}Subjects repository already exists. Use 'make update-subjects' to update.${RESET}"; \
	else \
		git clone $(SUBJECTS_REPO) $(SUBJECTS_DIR); \
		echo "${GREEN}Exercises downloaded successfully to $(SUBJECTS_DIR)${RESET}"; \
	fi

update-subjects:
	@echo "${YELLOW}Updating exercises from repository...${RESET}"
	@if [ -d "$(SUBJECTS_DIR)/.git" ]; then \
		cd $(SUBJECTS_DIR) && git pull; \
		echo "${GREEN}Exercises updated successfully${RESET}"; \
	else \
		echo "${RED}Subjects repository not found. Use 'make get-subjects' first.${RESET}"; \
	fi

install: setup
	@echo "${GREEN}Installing ${BOLD}$(NAME)${RESET}${GREEN}...${RESET}"
	@mkdir -p $(PROGRAM_SHARE_DIR)
	@mkdir -p $(PROGRAM_SHARE_DIR)/src
	
	# Copy program files to shared location
	@cp $(SRC_FILES) $(PROGRAM_SHARE_DIR)/src/
	
	# Create wrapper script with clean environment
	@echo "#!/bin/bash" > $(INSTALL_DIR)/$(NAME)
	@echo "# Create user's .vfy directory if it doesn't exist" >> $(INSTALL_DIR)/$(NAME)
	@echo "mkdir -p \$$HOME/.vfy/subjects" >> $(INSTALL_DIR)/$(NAME)
	@echo "mkdir -p \$$HOME/.vfy/program" >> $(INSTALL_DIR)/$(NAME)
	@echo "" >> $(INSTALL_DIR)/$(NAME)
	@echo "# Copy program files to user directory if they don't exist" >> $(INSTALL_DIR)/$(NAME)
	@echo "if [ ! -f \$$HOME/.vfy/program/vfy.py ]; then" >> $(INSTALL_DIR)/$(NAME)
	@echo "  cp $(PROGRAM_SHARE_DIR)/src/* \$$HOME/.vfy/program/" >> $(INSTALL_DIR)/$(NAME)
	@echo "fi" >> $(INSTALL_DIR)/$(NAME)
	@echo "" >> $(INSTALL_DIR)/$(NAME)
	@echo "# Run with clean environment to avoid Python conflicts" >> $(INSTALL_DIR)/$(NAME)
	@echo "env -i HOME=\$$HOME PATH=/usr/bin:/bin:/usr/local/bin LANG=\$$LANG python3 \$$HOME/.vfy/program/vfy.py \"\$$@\"" >> $(INSTALL_DIR)/$(NAME)
	@chmod +x $(INSTALL_DIR)/$(NAME)
	
	@echo "${GREEN}Installation completed! ${BOLD}You can now use the '$(NAME)' command.${RESET}"
	@echo ""
	@echo "${YELLOW}Note: You need to download exercises with 'make get-subjects'${RESET}"
	@echo ""
	@echo "${CYAN}Try:${RESET}"
	@echo "  ${BOLD}$(NAME) help${RESET}    - Show help"
	@echo "  ${BOLD}$(NAME) list${RESET}    - List available levels"
	@echo "  ${BOLD}$(NAME) get 1${RESET}   - Get a random exercise from level 1"

uninstall:
	@echo "${RED}Uninstalling ${BOLD}$(NAME)${RESET}${RED}...${RESET}"
	@rm -f $(INSTALL_DIR)/$(NAME)
	@rm -rf $(PROGRAM_SHARE_DIR)
	@echo "${YELLOW}Do you want to remove the exercises too? (y/n)${RESET}"
	@read resp; \
	if [ "$$resp" = "y" ] || [ "$$resp" = "Y" ]; then \
		rm -rf $(SUBJECTS_DIR); \
		rm -rf $(PROGRAM_DIR); \
		rm -rf $(HOME)/.vfy; \
		rm -rf $(HOME)/vfy_exercises; \
		echo "${RED}Exercises removed.${RESET}"; \
	else \
		echo "${GREEN}Exercises remain in $(SUBJECTS_DIR)${RESET}"; \
	fi
	@echo "${GREEN}Uninstallation completed.${RESET}"

clean:
	@echo "${BLUE}Cleaning temporary files...${RESET}"
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -delete
	@find . -name ".last_exercise" -delete
	@rm -rf build/ dist/ *.egg-info/
	@echo "${GREEN}Cleanup completed.${RESET}" 