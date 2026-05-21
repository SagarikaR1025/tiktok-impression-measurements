import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="TikTok Creator Intelligence Dashboard",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("outputs/clean_tiktok_data.csv")
# Load Claude-generated insights
with open("outputs/claude_creator_insights.txt", "r") as f:
    claude_insights = f.read()
# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df["category"].unique(),
    default=df["category"].unique()
)

filtered_df = df[df["category"].isin(selected_category)]

# -----------------------------
# TITLE
# -----------------------------
st.title("TikTok Creator Intelligence Dashboard")

st.markdown(
    "Analyze creator performance, engagement trends, and content strategy insights."
)

# -----------------------------
# KPI METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Posts",
    f"{len(df):,}"
)

col2.metric(
    "Average Views",
    f"{round(df['total_views'].mean(), 0):,.0f}"
)

col3.metric(
    "Average Engagement Rate",
    f"{round(df['engagement_rate_pct'].mean(), 2)}%"
)

st.divider()

st.markdown("## Performance Analytics")
# -----------------------------
# CATEGORY ENGAGEMENT
# -----------------------------
category_engagement = (
    filtered_df.groupby("category")["engagement_rate_pct"]
    .mean()
    .reset_index()
    .sort_values(by="engagement_rate_pct", ascending=False)
)

fig = px.bar(
    category_engagement,
    x="category",
    y="engagement_rate_pct",
    title="Average Engagement Rate by Category"
)

st.plotly_chart(fig, use_container_width=True)

##Views by Day 
views_by_day = (
    filtered_df.groupby("day_of_week")["total_views"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    views_by_day,
    x="day_of_week",
    y="total_views",
    title="Average Views by Day"
)

st.plotly_chart(fig2, use_container_width=True)

## Sound Type 
sound_performance = (
    filtered_df.groupby("tiktok_stat")["engagement_rate_pct"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    sound_performance,
    x="tiktok_stat",
    y="engagement_rate_pct",
    title="Engagement Rate by Sound Type"
)
## Top Performing Videos 

st.plotly_chart(fig3, use_container_width=True)

st.markdown("## Top Performing Videos")

top_videos = filtered_df.sort_values(
    by="total_views",
    ascending=False
)[["video", "category", "total_views", "engagement_rate_pct"]]

st.dataframe(top_videos.head(10))

## Engagement Trend Over Time

daily_engagement = (
    filtered_df.groupby("date")["engagement_rate_pct"]
    .mean()
    .reset_index()
)

fig4 = px.line(
    daily_engagement,
    x="date",
    y="engagement_rate_pct",
    title="Engagement Trend Over Time"
)

st.plotly_chart(fig4, use_container_width=True)
st.markdown("## AI-Powered Creator Insights")

st.write(claude_insights)
st.divider()

st.markdown("## Top Performing Content")
top_videos

## Top Videos Table
st.divider()

st.markdown("## Top Performing Content")

top_videos = filtered_df.sort_values(
    by="engagement_rate_pct",
    ascending=False
)[[
    "video",
    "category",
    "total_views",
    "engagement_rate_pct"
]]

st.dataframe(top_videos.head(10))

##Engagement Trend Line
st.divider()

st.markdown("## Engagement Trends Over Time")

daily_engagement = (
    filtered_df.groupby("date")["engagement_rate_pct"]
    .mean()
    .reset_index()
)

fig4 = px.line(
    daily_engagement,
    x="date",
    y="engagement_rate_pct",
    title="Daily Engagement Trend"
)

st.plotly_chart(fig4, use_container_width=True)

## Content Archetype Section 
st.divider()

st.markdown("## Content Archetype Performance")
cluster_df = pd.read_csv("outputs/clustered_tiktok_data.csv")
cluster_summary = (
    cluster_df.groupby("cluster_label")
    .agg(
        avg_engagement=("engagement_rate_pct", "mean"),
        avg_views=("total_views", "mean")
    )
    .reset_index()
)
fig5 = px.bar(
    cluster_summary,
    x="cluster_label",
    y="avg_engagement",
    title="Engagement Rate by Content Archetype"


)

st.plotly_chart(fig5, use_container_width=True)

st.divider()

st.markdown("## AI-Powered Creator Strategy Insights")
st.info(claude_insights)


