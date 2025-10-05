

import pandas as pd
import streamlit as st
import plotly.express as px


filepath = r"d:\UE\DATA_VISUALISATION\PROJECT\df2025_interactive.csv"
df2025i = pd.read_csv(filepath)


st.title("Global Happiness Dashboard")


# Year Selector
years = sorted(df2025i["year"].unique())
default_year = max(years)
year = st.slider("Select Year", min_value=min(years), max_value=max(years), value=default_year, step=1)

# data for chosen year
df_year = df2025i[df2025i["year"] == year]

st.header(f"{year} World Map: Happines Scores")
fig_map = px.choropleth(
    df_year,
    locations="country",
    locationmode="country names",
    color="score",
    color_continuous_scale="RdYlGn",
    title=f"Happiness Scores by Country ({year})",
    labels={"score": "Happiness Score"},
    hover_name="country"
)
fig_map.update_geos(showcoastlines=True, showland=True, landcolor="white", projection_type="natural earth")
fig_map.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
st.plotly_chart(fig_map, use_container_width=True)


st.header("GDP vs. Happiness Score (Scatter Plot)")

# Scatter plot for the selected year
fig_scatter = px.scatter(
    df_year,  # Filtered DataFrame for the selected year
    x="gdp",
    y="score",
    color="score",
    hover_name="country",
    color_continuous_scale="RdYlGn",
    trendline="ols",  # Adds regression/trend line
    title=f"GDP per Capita vs. Happiness Score ({year})",
    labels={"gdp": "GDP per Capita", "score": "Happiness Score"}
)
st.plotly_chart(fig_scatter, use_container_width=True)