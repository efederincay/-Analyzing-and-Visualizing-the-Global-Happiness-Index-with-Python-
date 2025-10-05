# -Analyzing-and-Visualizing-the-Global-Happiness-Index-with-Python-
The objective of the project is to analyze and visualize the insights of the Global Happiness Index using Python.  
It combines **data analysis, machine learning, and interactive visualization** to explore the factors that influence happiness worldwide.

---

##  Project Overview

The **World Happiness Report** ranks countries based on several key indicators such as GDP, social support, health, freedom, generosity, and corruption.  
In this project, we performed:
- Data preprocessing and cleaning  
- Statistical and correlation analysis  
- Visualization of global patterns  
- Building **interactive dashboards** using Streamlit and Plotly  

---

## 🧠 Key Insights

- **Freedom** and **Social Support** are the strongest predictors of happiness.  
- While GDP is important, **social and political factors** play a greater role.  
- **Northern Europe** (Finland, Denmark, Iceland) consistently leads global happiness rankings.  
- Visual dashboards make it easier to compare countries and understand year-over-year changes.

---

## 📈 Visualizations and Dashboards

### 1. Global Happiness Dashboard (`dashboard.py`)
Interactive world map and scatter plots:
- 🗺️ Choropleth map showing Happiness Scores by country  
- 📉 GDP vs. Happiness Score scatter plot with trendline  

### 2. Country Profile Dashboard (`country_profile_dashboard.py`)
Explore each country's data:
- 📆 Yearly Happiness Trend (Line Chart)  
- 🕸️ Country Indicator Profile (Radar Chart)  
- 🥇 Rank Over Years (Bar Chart)

---

## 🧰 Technologies Used

| Category | Tools / Libraries |
|-----------|-------------------|
| Data Handling | `pandas`, `numpy` |
| Visualization | `matplotlib`, `seaborn`, `plotly` |
| Machine Learning | `scikit-learn` |
| Dashboard | `streamlit` |
| Others | `pycountry_convert` |

---

## 🚀 How to Run the Dashboard

### 1️⃣ Install the requirements
```bash
pip install pandas numpy plotly streamlit scikit-learn pycountry-convert

**2️⃣ Run the Global Dashboard**
bash
streamlit run dashboard.py

**3️⃣ Run the Country Profile Dashboard**
bash
streamlit run country_profile_dashboard.py


```
**PROJECT STRUCTURE**

📁 Analyzing-and-Visualizing-the-Global-Happiness-Index-with-Python
│
├── dashboard.py                     # Global-level interactive dashboard
├── country_profile_dashboard.py     # Country-level interactive dashboard
├── tempCodeRunnerFile.py            # Test file for dashboard debugging
├── EFE ESREF DERINCAY DSC A WORLD HAPPINESS PROJECT.ipynb  # Main notebook
├── README.md                        # Project documentation
└── df2025_interactive.csv           # Cleaned dataset 


📑 Author

👤 Efe Esref Derincay
📚 MSc Data Science — University of Europe for Applied Sciences



