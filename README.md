# Find Pi to the Nth Decimal Place
This is a Python implementation for a program that takes the number of decimal places from the user as input (where the number of decimal places should not exceed 15) and outputs the value of pi (π) up to the number of decimal places provided. The number of decimal places can either be entered in numerals or words. User input is validated, which avoids Python's `ValueError` no matter what is supplied as input.

This program requires Python 3 which can be installed from [here](https://www.python.org/downloads/).

First, a virtual environment can be created and activated using the following commands:

```bash
python3 -m venv env
source env/bin/activate
```

Then, the required Python packages need to be installed which are listed in the `requirements.txt` file using the command below:
```bash
pip install -r requirements.txt
```

To start the program, run the following command:
```bash
python3 main.py
```
The project idea was obtained from [karan/Projects#numbers](https://github.com/karan/Projects#numbers).
