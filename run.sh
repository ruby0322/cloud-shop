#!/bin/bash

# Add current directory to PYTHONPATH
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}$(pwd)"

# Run the main Python script
python3 src/main.py 