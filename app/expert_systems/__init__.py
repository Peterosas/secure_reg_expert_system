# Import the expert system class
from .secure_reg_expert_system import SecureRegExpertSystem

# Import the individual rules
from .rules import rule_email_domain, rule_age, rule_country, rule_income

# Initialize the expert system and add the rules
def create_expert_system():
    expert_system = SecureRegExpertSystem()
    expert_system.add_rule(rule_email_domain)
    expert_system.add_rule(rule_age)
    expert_system.add_rule(rule_country)
    expert_system.add_rule(rule_income)
    return expert_system
