echo Installing the required python libraries.
python -m pip install -r requirements.txt

echo Creating the sql database.
python database.py

echo Setup completed successfully.
