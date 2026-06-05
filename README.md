# Gurgaon Real Estate Market Analysis (EDA) 🏠

A data-driven exploration of the Gurgaon real estate market using Python. This project analyzes pricing dynamics, locality-based premiums, and the impact of RERA regulations on over 19,000 property listings.

## 📌 Project Overview
The goal of this project is to uncover the key factors that drive property prices in a rapidly developing urban market. By cleaning and analyzing raw listing data, we identify which factors (Area, BHK, Status, RERA) most significantly impact the "Rate per Sqft."

## 📊 Key Insights & Results
- **The Most Expensive Property:** Identified a luxury 6 BHK apartment in **DLF Camellias (Sector 42)** valued at **₹122.6 Cr**.
- **Premium Localities:** **Sector 42** emerged as the most premium zone with an average rate of **₹55,989 per sqft**.
- **Status Premium:** Ready-to-move properties command a price premium of approximately **5%** over under-construction projects.
- **RERA Paradox:** Data suggests that many ultra-luxury legacy properties (non-RERA) still hold higher average values than newer RERA-approved mid-market segments.
- **Top Asset Class:** **Villas** were found to be the costliest property type per square foot compared to apartments and floors.

## 🛠️ Technical Workflow
1. **Data Cleaning:** - Handled currency formatting by removing commas and converting strings to `float`.
   - Standardized categorical values (Status, RERA, Flat Type).
   - Removed duplicate records to ensure data integrity.
2. **Analysis:** - Grouped data by Locality and Company to find average market rates.
   - Performed conditional analysis on RERA and Construction Status.
3. **Visualization:** - Created scatter plots to visualize the correlation between Property Area and Total Price.
   - Identified market outliers using price-per-sqft metrics.

## 📈 Visualizations


## 📁 Repository Structure
- `Real_Estate_DATA.csv`: The raw dataset used for analysis.
- `Real_Estate_Analysis.ipynb`: The Python notebook containing cleaning and EDA logic.
