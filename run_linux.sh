#!/bin/bash

VENV_NAME="HK-venv"

echo "Checking if the venv already exists"; echo ""
if [ -d "$VENV_NAME" ]; then 
    echo "The venv already exists!"; echo ""
else    
    echo "Venv doesnt exist yet. Creating it..."; echo ""
    python3 -m venv "$VENV_NAME"
    echo "Venv has been created!"; echo ""
fi

echo Activating venv; echo ""
source "$VENV_NAME"/bin/activate

echo Installing all the dependencies; echo ""
pip install -r requirements.txt

echo List of dependencies:; echo ""
pip freeze

echo ""; echo "Done!"