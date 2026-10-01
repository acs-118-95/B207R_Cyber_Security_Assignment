# Phishing Email Detection System
In this project a system is developed, which can be used to identify a phishing email and a safe email. It uses TF-IDF vectorization for converting textual value to numerical value and uses logistic regression model. A database has also been created to store the prediction result and its respective email text.

## Project Files
- **datacheck.py** - using this file the dataset is checked to identify its structure, missing values, label counts, and duplicates in email text.
- **database.py** - this file creates an SQLite database, which stores the prediction results, and its respective email text.
- **training.py** - in this file the dataset is cleaned, and prepared, and then trains the machine learning model using that data, test new emails, and save the result into the database created by *database.py*.
- **requirements.txt** - this file contains list of needed python libraries to run this project.
- **setup.bat** - this file sets up the project on windows.
- **setup.sh** - this file sets up the project on mac, linux.

## Required Libraries
The libraries used in this project are: **pandas**, **scikit-learn**.

These libraries are listed in the requirements.txt file, so while running the setup file, these libraries will be installed automatically.

## Setup
The setup file must be run before running the *training.py* file, because this setup file installs the required libraries and creates the SQLite database.

For Windows: `.\setup.bat`

For Others: `bash setup.sh`

## Run *training.py*
Once the setup is run, and the library installation and database creation has been completed successfully, run `python training.py`.

The program will then train the model, show the evaluation results, and at the end ask the user to enter an email. It will then predict whether the email is safe or phishing, and then save the prediction result and the email into the database.

## Dataset
A phishing email dataset has been used in this project which is stored in the *data* folder as *emails.csv*. Dataset source is `https://huggingface.co/datasets/zefang-liu/phishing-email-dataset/blob/main/Phishing_Email.csv`.