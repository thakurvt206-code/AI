# Web Agent Demo – Lead Identification & Ranking

**Candidate:** Vikas Thakur  
**Email:** vikasthakur0745@gmail.com  

A prototype web-agent system to **identify, enrich, and rank high-probability leads** for 3D in-vitro models in drug discovery and safety assessment.

---

## **Overview**
- **Identification:** Target profiles from LinkedIn, PubMed, and conference lists.  
- **Enrichment:** Adds business email, location, HQ, funding stage, and tech usage.  
- **Ranking:** Propensity-to-Buy score (0–100) using weighted signals:

| Signal                  | Weight |
|-------------------------|--------|
| Role Fit (Toxicology, Safety, Hepatic, Preclinical) | +30 |
| Scientific Intent (Recent publication)             | +40 |
| Company Funding (Series A/B)                       | +20 |
| Technographic Fit (Uses 3D models)                | +15 |
| Location Hub (Boston/Cambridge/Basel/Bay Area)    | +10 |

---

## **Demo Architecture**

Data Sources (LinkedIn, PubMed, Conferences)
│
▼
Data Ingestion (CSV / JSON)
│
▼
Enrichment Layer
│
▼
Scoring Engine
│
▼
Streamlit Dashboard (Searchable & Exportable)

## **Run**
streamlit run app.py
