#!/bin/bash

# Check if python3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is required but not installed."
    exit 1
fi

# Create necessary directories if they don't exist
mkdir -p src/models src/services tests

# Add current directory to PYTHONPATH
export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}$(pwd)"

# No other build steps needed as this is a Python project
echo "Build completed successfully." 