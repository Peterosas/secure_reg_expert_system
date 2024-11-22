class SecureRegExpertSystem:
    def __init__(self):
        self.rules = []
        self.tier_mapping = {
            "low": "Tier 3",
            "medium": "Tier 2",
            "high": "Tier 1",
        }

    def add_rule(self, rule):
        """Add a rule to the expert system."""
        self.rules.append(rule)

    def evaluate(self, user_data):
        """Evaluate user data against the rules."""
        fraud_score = 0
        for rule in self.rules:
            fraud_score += rule(user_data)

        classification = "Good"
        if fraud_score > 50:
            classification = "Fraudster"

        tier = self.determine_tier(fraud_score)
        return {"classification": classification, "tier": tier}

    def determine_tier(self, fraud_score):
        """Determine tier based on fraud score."""
        if fraud_score <= 20:
            return self.tier_mapping["low"]
        elif 20 < fraud_score <= 50:
            return self.tier_mapping["medium"]
        else:
            return self.tier_mapping["high"]


# Define rules
def rule_email_domain(user_data):
    """Check for suspicious email domains."""
    suspicious_domains = ["fraud.com", "fakeemail.com"]
    if user_data["email"].split("@")[-1] in suspicious_domains:
        return 30
    return 0


def rule_age(user_data):
    """Assign a score based on age."""
    if user_data["age"] < 18 or user_data["age"] > 60:
        return 20
    return 0


def rule_country(user_data):
    """Check if the country is high-risk."""
    high_risk_countries = ["CountryX", "CountryY"]
    if user_data["country"] in high_risk_countries:
        return 40
    return 0


def rule_income(user_data):
    """Check if the income is unusually high."""
    if user_data["income"] > 1_000_000:
        return 10
    return 0


# Initialize expert system
expert_system = SecureRegExpertSystem()

# Add rules to the system
expert_system.add_rule(rule_email_domain)
expert_system.add_rule(rule_age)
expert_system.add_rule(rule_country)
expert_system.add_rule(rule_income)

# Sample user data
user_data = {
    "email": "user@fraud.com",
    "age": 15,
    "country": "CountryZ",
    "income": 1_200_000,
}

# Evaluate user data
result = expert_system.evaluate(user_data)
print("Classification:", result["classification"])
print("Tier:", result["tier"])
