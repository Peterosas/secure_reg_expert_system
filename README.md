# Re-define the content of the README file after code execution reset
readme_content = """
# SecureRegExpertSystem

**SecureRegExpertSystem** is a Flask-based application that evaluates user data against predefined rules to classify them into different tiers based on fraud risk.

## Description

This project allows users to register and applies an expert system to classify them as either `Good` or `Fraudster`. Based on the evaluation score, users are assigned a tier (`Tier 1`, `Tier 2`, or `Tier 3`) which reflects their fraud risk level.

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/secure-reg-expert-system.git


cd secure-reg-expert-system


python3 -m venv venv
source venv/bin/activate


python -m venv venv
.\\venv\\Scripts\\activate


pip install -r requirements.txt


python run.py


http://127.0.0.1:5000/
