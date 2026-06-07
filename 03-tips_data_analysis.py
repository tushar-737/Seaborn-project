import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset('tips')

# Create Tip Percentage Column
tips['tip_percentage'] = (tips['tip'] / tips['total_bill']) * 100

# Set style
sns.set_style('whitegrid')

# Create Dashboard
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# 1. Total Bill Distribution
sns.histplot(data=tips, x='total_bill', bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribution of Total Bill')

# 2. Tip by Gender
sns.boxplot(data=tips, x='sex', y='tip', ax=axes[0, 1])
axes[0, 1].set_title('Tip by Gender')

# 3. Tip by Day
sns.barplot(data=tips, x='day', y='tip', estimator='mean', ax=axes[0, 2])
axes[0, 2].set_title('Average Tip by Day')

# 4. Tip Percentage Distribution
sns.histplot(data=tips, x='tip_percentage', bins=20, kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Tip Percentage Distribution')

# 5. Smoker vs Non-Smoker Comparison
sns.boxplot(data=tips, x='smoker', y='tip', ax=axes[1, 1])
axes[1, 1].set_title('Tip by Smoking Status')

# 6. Relationship Between Bill and Tip
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='smoker', ax=axes[1, 2])
axes[1, 2].set_title('Total Bill vs Tip')

plt.tight_layout()
plt.show()