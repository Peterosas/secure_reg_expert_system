# SecureRegExpertSystem

**SecureRegExpertSystem** is a Flask-based application that evaluates user data against predefined rules to classify them into different tiers based on fraud risk.

## Description

This project allows users to register and applies an expert system to classify them as either `Good` or `Fraudster`. Based on the evaluation score, users are assigned a tier (`Tier 1`, `Tier 2`, or `Tier 3`) which reflects their fraud risk level.

---

## Instruction on how to run the applicaiton

### Step 1: Clone the Repository
```bash
git clone https://github.com/Peterosas/secure_reg_expert_system.git
cd secure-reg-expert-system
```

### Step 2: Set Up a Virtual Environment

For Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:
```bash
python -m venv venv
.\\venv\\Scripts\\activate
```

Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```
## Running the Application
### To start the application, use the following command:
```bash
python run.py
```


Once the application is running, open your browser and navigate to:
http://127.0.0.1:5000/
