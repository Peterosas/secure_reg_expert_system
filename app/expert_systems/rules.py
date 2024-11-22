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
    high_risk_countries = ["Ghana", "Uganda"]
    if user_data["country"] in high_risk_countries:
        return 40
    return 0


def rule_income(user_data):
    """Check if the income is unusually high."""
    if user_data["income"] > 1000000:
        return 10
    return 0

