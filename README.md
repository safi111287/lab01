# lab01 
# Input Validation and Decision Programs

This command-line program contains four small tools that read user input, validate the entered values, and return different results based on the user's input

The available tools are:
- Shipping Cost Calculator
- Grade Classifier
- Loan Affordability Check
- BMI Category Reporter

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python lab01.py
```

## Example

```text
Choose one option:
1. Calculate shipping cost
2. Classify grade
3. Check loan affordability
4. Report BMI category

Enter your choice (1-4): 1
Enter package weight in kg (greater than 0 and up to 50 kg): 4.5
Enter destination zone (1, 2, or 3): 2

Shipping cost for a 4.5 kg package in the Standard rate band to Zone 2 is $40.50.
```

## Known Limitations

The program uses predefined shipping rates, destination zone multipliers, grade ranges, loan affordability thresholds, and BMI categories.  
These values are fixed in the current version and could be made configurable in a future version.