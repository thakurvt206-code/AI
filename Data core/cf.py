def calculate_score(row):
    score = 0

    # Role Fit
    if any(keyword in row["title"].lower() for keyword in 
           ["toxicology", "safety", "hepatic", "preclinical", "3d"]):
        score += 30

    # Scientific Intent
    if row["recent_publication"] == "yes":
        score += 40

    # Company Funding
    if row["funding_stage"] in ["Series A", "Series B"]:
        score += 20

    # Technographic Signal
    if row["uses_invitro_models"] == "yes":
        score += 15

    # Location Hub
    if row["hq_location"] in ["Boston", "Cambridge", "Bay Area", "Basel", "UK"]:
        score += 10

    return min(score, 100)
