import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("05-netflix.csv")

sns.set_style("whitegrid")

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# 1. Movies vs TV Shows
sns.countplot(
    data=df,
    x='type',
    ax=axes[0,0]
)
axes[0,0].set_title('Movies vs TV Shows')

# 2. Top 5 Ratings
rating_count = df['rating'].value_counts().head(5)

sns.barplot(
    x=rating_count.index,
    y=rating_count.values,
    ax=axes[0,1]
)
axes[0,1].set_title('Top Ratings')
axes[0,1].tick_params(axis='x', rotation=45)

# 3. Top 5 Countries
country_count = df['country'].value_counts().head(5)

sns.barplot(
    x=country_count.values,
    y=country_count.index,
    ax=axes[0,2]
)
axes[0,2].set_title('Top Countries')

# 4. Release Year Distribution
sns.histplot(
    data=df,
    x='release_year',
    bins=20,
    ax=axes[1,0]
)
axes[1,0].set_title('Release Year Distribution')

# 5. Content Added by Month
month_count = df['date_added'].dropna().str.split().str[0].value_counts()

sns.barplot(
    x=month_count.index,
    y=month_count.values,
    ax=axes[1,1]
)
axes[1,1].set_title('Content Added by Month')
axes[1,1].tick_params(axis='x', rotation=45)

# 6. Content Type Percentage
type_count = df['type'].value_counts()

axes[1,2].pie(
    type_count.values,
    labels=type_count.index,
    autopct='%1.1f%%'
)
axes[1,2].set_title('Content Share')

plt.suptitle('Netflix Data Analysis Dashboard', fontsize=18)
plt.tight_layout()
plt.show()