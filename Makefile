# Makefile for the Virtual Twin Ambulance project

# Define the virtual environment directory
VENV_DIR = venv
PYTHON = $(VENV_DIR)/Scripts/python
PIP = $(VENV_DIR)/Scripts/pip
STREAMLIT = $(VENV_DIR)/Scripts/streamlit

# Default target
.DEFAULT_GOAL := help

# Install dependencies into a virtual environment
install: $(VENV_DIR)/pyvenv.cfg

$(VENV_DIR)/pyvenv.cfg: requirements.txt
	@echo "Creating virtual environment..."
	python -m venv $(VENV_DIR)
	@echo "Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run the dashboard
run: install
	@echo "Starting dashboard..."
	$(STREAMLIT) run dashboard.py

# Clean the environment
clean:
	@echo "Cleaning up..."
	@if exist $(VENV_DIR) ( rmdir /s /q $(VENV_DIR) )
	@if exist __pycache__ ( rmdir /s /q __pycache__ )
	@echo "Done."

# Help target to display available commands
help:
	@echo "Available commands:"
	@echo "  install  - Creates a virtual environment and installs dependencies."
	@echo "  run      - Runs the Streamlit dashboard."
	@echo "  clean    - Removes the virtual environment and __pycache__."

.PHONY: install run clean help
