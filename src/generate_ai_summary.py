import pandas as pd
from claude_insights import generate_creator_insights

# Load clustered dataset
df = pd.read_csv("outputs/clustered_tiktok_data.csv")

# Overall metrics
total_posts = len(df)
avg_views = round(df["total_views"].mean(), 2)
avg_engagement = round(df["engagement_rate_pct"].mean(), 2)

# Top categories by engagement
top_categories = (
    df.groupby("category")["engagement_rate_pct"]
    .mean()
    .sort_values(ascending=False)
    .head(5)
)

# Cluster performance
cluster_performance = (
    df.groupby("cluster_label")
    .agg(
        post_count=("video", "count"),
        avg_views=("total_views", "mean"),
        avg_engagement_rate_pct=("engagement_rate_pct", "mean")
    )
    .sort_values(by="avg_engagement_rate_pct", ascending=False)
)

# Build summary text
summary_text = f"""
TikTok Creator Analytics Summary:

Total posts analyzed: {total_posts}
Average views: {avg_views}
Average engagement rate: {avg_engagement}%

Top categories by engagement:
{top_categories.to_string()}

Content archetype performance:
{cluster_performance.to_string()}

Please interpret these results from a creator strategy and growth analytics perspective.
"""

# Generate Claude insights
insights = generate_creator_insights(summary_text)

print(insights)

# Save insights to output file
with open("outputs/claude_creator_insights.txt", "w") as f:
    f.write(insights)