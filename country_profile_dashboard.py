import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


filepath = r"d:\UE\DATA_VISUALISATION\PROJECT\df2025_interactive.csv"
df2025i = pd.read_csv(filepath)


st.header("Country Happiness Profile")

# Dropdown selector for country
country = st.selectbox("Select a country:", df2025i["country"].unique())

# Filter for the selected country
df_country = df2025i[df2025i["country"] == country].sort_values("year")

# 1. Line Chart: Happiness Score Trend over Years
fig_line = px.line(
    df_country,
    x="year",
    y="score",
    markers=True,
    title=f"{country}: Happiness Score Trend"
)
st.plotly_chart(fig_line, use_container_width=True)

# 2. Radar Chart: Latest Year Indicators
features = ["gdp", "social_support", "health", "freedom", "generosity", "corruption"]
latest_year = df_country["year"].max()
latest = df_country[df_country["year"] == latest_year].iloc[0]

radar_values = [latest[feature] for feature in features]
fig_radar = go.Figure()
fig_radar.add_trace(go.Scatterpolar(
    r=radar_values,
    theta=features,
    fill='toself',
    name=country
))
fig_radar.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, max(df2025i[features].max())])),
    showlegend=False,
    title=f"{country} Indicator Profile ({int(latest_year)})"
)
st.plotly_chart(fig_radar, use_container_width=True)

# 3. Bar Chart: Rank Over Years
# Calculate rank for each year
df_yearly = df2025i.copy()
df_yearly["rank"] = df_yearly.groupby("year")["score"].rank(ascending=False, method="min")
country_rank = df_yearly[df_yearly["country"] == country].sort_values("year")

fig_bar = px.bar(
    country_rank,
    x="year",
    y="rank",
    text="rank",
    title=f"{country}: Happiness Rank by Year",
    labels={"rank": "Rank", "year": "Year"}
)
fig_bar.update_yaxes(autorange="reversed")  # 1 is best rank
st.plotly_chart(fig_bar, use_container_width=True)
