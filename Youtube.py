# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Load dataset
df = pd.read_csv('USvideos.csv')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date columns
df['trending_date'] = pd.to_datetime(df['trending_date'], format='%y.%d.%m')
df['publish_time'] = pd.to_datetime(df['publish_time']).dt.tz_localize(None)
df['publish_day'] = df['publish_time'].dt.day_name()

# Load and map categories
with open('US_category_id.json') as f:
    categories = json.load(f)

cat_map = {int(item['id']): item['snippet']['title'] for item in categories['items']}
df['category_name'] = df['category_id'].map(cat_map)

# Ensure no extra spaces in column names
df.columns = df.columns.str.strip()

# Chart 1: Top 10 Trending Categories
top_categories = df['category_name'].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(
    y=top_categories.index,
    x=top_categories.values,
    hue=top_categories.index,        # FIXED: Avoid future warning
    palette='viridis',
    legend=False
)
plt.title('Top 10 Trending Categories')
plt.xlabel('Number of Trending Videos')
plt.ylabel('Category')
plt.tight_layout()
plt.show()

# Chart 2: Days to Trend vs Views
df['days_to_trend'] = (df['trending_date'] - df['publish_time'].dt.normalize()).dt.days
df = df[df['days_to_trend'] >= 0]  # Remove negative values

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='days_to_trend', y='views')
plt.title('Days to Trend vs Views')
plt.xlabel('Days to Trend')
plt.ylabel('Views')
plt.tight_layout()
plt.show()

# Chart 3: Likes vs Comments (log-log scale)
df_log = df[(df['likes'] > 0) & (df['comment_count'] > 0)]  # Avoid log error

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_log, x='likes', y='comment_count')
plt.xscale('log')
plt.yscale('log')
plt.title('Comments vs Likes (Log Scale)')
plt.xlabel('Likes')
plt.ylabel('Comments')
plt.tight_layout()
plt.show()

# Correlation
corr = df['likes'].corr(df['comment_count'])
print(f"Correlation between likes and comments: {corr:.2f}")

# Chart 4: Do Tags Affect Views?
df['has_tags'] = df['tags'].apply(lambda x: 0 if '[none]' in x.lower() else 1)

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='has_tags', y='views')
plt.xticks([0, 1], ['No Tags', 'Has Tags'])
plt.title('Do Tags Affect Views?')
plt.xlabel('Tags Present')
plt.ylabel('Views')
plt.tight_layout()
plt.show()

# Save cleaned dataset — FIXED: avoid PermissionError
output_filename = "youtube_trending_cleaned_v2.csv"
df.to_csv(output_filename, index=False)
print(f"✅ Cleaned data saved to: {output_filename}")
