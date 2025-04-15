# VFY - Programming Exercises Verification Tool
# =============================================

NAME = vfy
INSTALL_DIR = /usr/local/bin
PROGRAM_SHARE_DIR = /usr/share/vfy
SUBJECTS_DIR = $(HOME)/.vfy/subjects
PROGRAM_DIR = $(HOME)/.vfy/program
SRC_FILES = src/__init__.py src/vfy.py src/config.py src/colors.py src/commands.py src/utils.py src/progress.py

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

.PHONY: all install uninstall clean help setup user-install

all: help

help:
	@echo "${BOLD}${CYAN}VFY${RESET} - Programming Exercises Verification Tool"
	@echo "${BOLD}===============================================${RESET}"
	@echo ""
	@echo "${BOLD}Usage:${RESET}"
	@echo "  ${YELLOW}make setup${RESET}     - Create necessary directories and example exercises"
	@echo "  ${GREEN}make install${RESET}   - Install vfy and setup exercise structure"
	@echo "  ${RED}make uninstall${RESET} - Uninstall vfy"
	@echo "  ${BLUE}make clean${RESET}     - Remove temporary files"
	@echo ""
	@echo "${BOLD}After installation:${RESET}"
	@echo "  ${CYAN}vfy help${RESET}        - Show program help"
	@echo "  ${CYAN}vfy list${RESET}        - List all available levels"
	@echo "  ${CYAN}vfy get <level>${RESET} - Get a random exercise"
	@echo "  ${CYAN}vfy status${RESET}      - Show status of current exercise"

setup:
	@echo "${YELLOW}Setting up directory structure...${RESET}"
	@mkdir -p subjects/level_1/ex00
	@mkdir -p subjects/level_1/ex01
	@mkdir -p subjects/level_1/ex02
	@mkdir -p subjects/level_2/ex00
	
	@echo "${YELLOW}Creating example exercises...${RESET}"
	
	@printf "Exercise: Hello World\n------------------\n\nWrite a program that prints \"Hello World\" (without quotes) and ends with a newline.\n\nExample output:\nHello World" > subjects/level_1/ex00/subject.txt
	@printf "Hello World" > subjects/level_1/ex00/expected_output.txt
	@printf "#include <stdio.h>\n\nint main(void) {\n    // Your code here\n    \n    return 0;\n}" > subjects/level_1/ex00/template.c
	
	@printf "Exercise: Sum Two Numbers\n------------------\n\nWrite a program that adds two integers (42 and 27) and prints the result.\n\nExample output:\n69" > subjects/level_1/ex01/subject.txt
	@printf "69" > subjects/level_1/ex01/expected_output.txt
	@printf "#include <stdio.h>\n\nint main(void) {\n    // Add the numbers 42 and 27\n    // Print the result\n    \n    return 0;\n}" > subjects/level_1/ex01/template.c
	
	@printf "Exercise: Print 1 to 10\n------------------\n\nWrite a program that prints numbers from 1 to 10, each on a new line.\n\nExample output:\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10" > subjects/level_1/ex02/subject.txt
	@printf "1\n2\n3\n4\n5\n6\n7\n8\n9\n10" > subjects/level_1/ex02/expected_output.txt
	@printf "#include <stdio.h>\n\nint main(void) {\n    // Use a loop to print numbers 1 to 10\n    \n    return 0;\n}" > subjects/level_1/ex02/template.c
	
	@printf "Exercise: FizzBuzz\n------------------\n\nWrite a program that prints the numbers from 1 to 15.\nFor multiples of 3, print \"Fizz\" instead of the number.\nFor multiples of 5, print \"Buzz\" instead of the number.\nFor multiples of both 3 and 5, print \"FizzBuzz\".\n\nExample output:\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz" > subjects/level_2/ex00/subject.txt
	@printf "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz" > subjects/level_2/ex00/expected_output.txt
	@printf "#include <stdio.h>\n\nint main(void) {\n    // Loop from 1 to 15\n    // If multiple of 3, print \"Fizz\"\n    // If multiple of 5, print \"Buzz\"\n    // If multiple of both, print \"FizzBuzz\"\n    // Otherwise print the number\n    \n    return 0;\n}" > subjects/level_2/ex00/template.c
	
	@echo "${GREEN}Setup complete!${RESET}"

install: setup
	@echo "${GREEN}Installing ${BOLD}$(NAME)${RESET}${GREEN}...${RESET}"
	@mkdir -p $(PROGRAM_SHARE_DIR)
	@mkdir -p $(PROGRAM_SHARE_DIR)/src
	
	# Copy program files to shared location
	@cp $(SRC_FILES) $(PROGRAM_SHARE_DIR)/src/
	
	# Create wrapper script
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
	@echo "# Copy exercise subjects if they don't exist" >> $(INSTALL_DIR)/$(NAME)
	@echo "if [ ! -d \$$HOME/.vfy/subjects/level_1 ]; then" >> $(INSTALL_DIR)/$(NAME)
	@echo "  cp -r subjects/* \$$HOME/.vfy/subjects/ 2>/dev/null || :" >> $(INSTALL_DIR)/$(NAME)
	@echo "fi" >> $(INSTALL_DIR)/$(NAME)
	@echo "" >> $(INSTALL_DIR)/$(NAME)
	@echo "python3 \$$HOME/.vfy/program/vfy.py \"\$$@\"" >> $(INSTALL_DIR)/$(NAME)
	@chmod +x $(INSTALL_DIR)/$(NAME)
	
	# Copy example exercises to system-wide location
	@mkdir -p $(PROGRAM_SHARE_DIR)/subjects
	@cp -r subjects/* $(PROGRAM_SHARE_DIR)/subjects/
	
	@echo "${GREEN}Installation completed! ${BOLD}You can now use the '$(NAME)' command.${RESET}"
	@echo ""
	@echo "${CYAN}Try:${RESET}"
	@echo "  ${BOLD}$(NAME) help${RESET}    - Show help"
	@echo "  ${BOLD}$(NAME) list${RESET}    - List available levels"
	@echo "  ${BOLD}$(NAME) get 1${RESET}   - Get a random exercise from level 1"

user-install:
	@echo "${GREEN}Installing ${BOLD}$(NAME)${RESET}${GREEN} for current user...${RESET}"
	@mkdir -p $(SUBJECTS_DIR)
	@mkdir -p $(PROGRAM_DIR)
	@cp -r subjects/* $(SUBJECTS_DIR)
	@cp $(SRC_FILES) $(PROGRAM_DIR)/
	@mkdir -p $(HOME)/bin
	@echo "#!/bin/bash" > $(HOME)/bin/$(NAME)
	@echo "python3 $(PROGRAM_DIR)/vfy.py \"\$$@\"" >> $(HOME)/bin/$(NAME)
	@chmod +x $(HOME)/bin/$(NAME)
	@echo "${GREEN}Installation completed! ${BOLD}You can now use the '$(NAME)' command.${RESET}"
	@echo "${YELLOW}Make sure $(HOME)/bin is in your PATH.${RESET}"
	@echo "You may need to add this line to your .bashrc or .zshrc:"
	@echo "  ${BOLD}export PATH=\"\$$HOME/bin:\$$PATH\"${RESET}"
	@echo ""
	@echo "${CYAN}Try:${RESET}"
	@echo "  ${BOLD}$(NAME) help${RESET}    - Show help"
	@echo "  ${BOLD}$(NAME) list${RESET}    - List available levels"
	@echo "  ${BOLD}$(NAME) get 1${RESET}   - Get a random exercise from level 1"

uninstall:
	@echo "${RED}Uninstalling ${BOLD}$(NAME)${RESET}${RED}...${RESET}"
	@rm -f $(INSTALL_DIR)/$(NAME)
	@rm -f $(HOME)/bin/$(NAME)
	@rm -rf $(PROGRAM_SHARE_DIR)
	@echo "${YELLOW}Do you want to remove the exercises too? (y/n)${RESET}"
	@read resp; \
	if [ "$$resp" = "y" ] || [ "$$resp" = "Y" ]; then \
		rm -rf $(SUBJECTS_DIR); \
		rm -rf $(PROGRAM_DIR); \
		rm -rf $(HOME)/.vfy; \
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
	@echo "${GREEN}Cleanup completed.${RESET}" 