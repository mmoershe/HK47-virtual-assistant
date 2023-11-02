#!/bin/bash

VENV_NAME = "HK-venv"

echo "Checking if the venv already exists"
if [ -d "$VENV_NAME" ]; then 
    echo "the venv already exists"
else    
    echo "Venv doesnt exist yet. Creating it..."
    python3 -m venv "$VENV_NAME"
    echo "venv has been created!"
fi

source "$VENV_NAME"/bin/activate