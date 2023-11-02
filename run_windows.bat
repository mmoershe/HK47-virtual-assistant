@echo activating the virtual environment 
@call myenv/Scripts/activate
echo.
@echo pip freeze:
@pip freeze
echo.
@echo starting main.py...
python main.py
pause