import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("07-ipl_data.csv")

sns.set_style("whitegrid")

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# 1. Matches Won by Teams
team_wins = df['winner'].value_counts().head(10)

sns.barplot(
    x=team_wins.values,
    y=team_wins.index,
    ax=axes[0,0]
)
axes[0,0].set_title("Matches Won by Teams")

# 2. Toss Winners
toss_wins = df['toss_winner'].value_counts().head(10)

sns.barplot(
    x=toss_wins.values,
    y=toss_wins.index,
    ax=axes[0,1]
)
axes[0,1].set_title("Toss Winners")

# 3. Top Venues
venues = df['venue'].value_counts().head(10)

sns.barplot(
    x=venues.values,
    y=venues.index,
    ax=axes[0,2]
)
axes[0,2].set_title("Top IPL Venues")

# 4. Matches Per Season
season_matches = df['season'].value_counts().sort_index()

sns.lineplot(
    x=season_matches.index,
    y=season_matches.values,
    marker='o',
    ax=axes[1,0]
)
axes[1,0].set_title("Matches Per Season")

# 5. Toss Decision
sns.countplot(
    data=df,
    x='toss_decision',
    ax=axes[1,1]
)
axes[1,1].set_title("Toss Decisions")

# 6. Win Type
win_type = pd.Series({
    'By Runs': df['win_by_runs'].gt(0).sum(),
    'By Wickets': df['win_by_wickets'].gt(0).sum()
})

axes[1,2].pie(
    win_type.values,
    labels=win_type.index,
    autopct='%1.1f%%'
)
axes[1,2].set_title("Match Win Type")

plt.suptitle("IPL Data Analysis Dashboard", fontsize=18)
plt.tight_layout()
plt.show()