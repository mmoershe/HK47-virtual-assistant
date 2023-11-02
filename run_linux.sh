#!/bin/bash

# Define absolute paths
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
VENV_NAME="$SCRIPT_DIR/HK-venv"

echo "Performing a git pull..."; echo ""
git -C "$SCRIPT_DIR" pull

echo "Checking if the venv already exists..."; echo ""
if [ -d "$VENV_NAME" ]; then 
    echo "The venv already exists!"; echo ""
else    
    echo "Venv doesn't exist yet. Creating it..."; echo ""
    python3 -m venv "$VENV_NAME"
    echo "Venv has been created!"; echo ""
fi

echo "Activating venv..."; echo ""
source "$VENV_NAME"/bin/activate

echo "Installing all the dependencies..."; echo ""
pip install -r "$SCRIPT_DIR/requirements.txt"

echo "List of dependencies:"; echo ""
pip freeze

echo ""; echo "Done!"; echo ""

echo "Running the main script now..."; echo ""
python "$SCRIPT_DIR/main.py"
