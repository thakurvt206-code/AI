import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("leads.csv")

# Scoring Function
def calculate_score(row):
    score = 0
    if any(k in row["Title"].lower() for k in ["toxicology", "safety", "hepatic", "preclinical"]):
        score += 30
    if row["Recent_Publication"] == "Yes":
        score += 40
    if row["Funding_Stage"] in ["Series A", "Series B"]:
        score += 20
    if row["Uses_3D_Models"] == "Yes":
        score += 15
    if row["HQ_Location"] in ["Boston", "Cambridge", "Basel", "Bay Area"]:
        score += 10
    return min(score, 100)

# Apply scoring
df["Probability_Score"] = df.apply(calculate_score, axis=1)
df = df.sort_values(by="Probability_Score", ascending=False)

# UI
st.title("3D In-Vitro Lead Ranking Dashboard")

search = st.text_input("Search by location, company or title")

if search:
    df = df[df.apply(lambda row: search.lower() in row.astype(str).str.lower().to_string(), axis=1)]

st.dataframe(df)

# Export
st.download_button(
    label="Download CSV",
    data=df.to_csv(index=False),
    file_name="ranked_leads.csv",
    mime="text/csv"
)
