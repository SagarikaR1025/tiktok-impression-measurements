from claude_insights import generate_creator_insights

summary = """
The dataset contains 260 TikTok posts.
Average views are 8,866.
Average engagement rate is 6.85%.
The project includes content categories, sound types, posting dates, views, likes, comments, and favorites.
The goal is to identify high-performing content archetypes and generate creator strategy recommendations.
"""

insights = generate_creator_insights(summary)

print(insights)