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


