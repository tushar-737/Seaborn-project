import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
titanic = sns.load_dataset('titanic')

# Create dashboard
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# 1. Survival Count
sns.countplot(data=titanic, x='survived', ax=axes[0, 0])
axes[0, 0].set_title('Survival Count')

# 2. Survival by Gender
sns.countplot(data=titanic, x='sex', hue='survived', ax=axes[0, 1])
axes[0, 1].set_title('Survival by Gender')

# 3. Survival by Passenger Class
sns.countplot(data=titanic, x='class', hue='survived', ax=axes[0, 2])
axes[0, 2].set_title('Survival by Passenger Class')

# 4. Age Distribution
sns.histplot(data=titanic, x='age', bins=20, kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Age Distribution')

# 5. Fare Distribution
sns.histplot(data=titanic, x='fare', bins=20, kde=True, ax=axes[1, 1])
axes[1, 1].set_title('Fare Distribution')

# 6. Correlation Heatmap
numeric_data = titanic.select_dtypes(include='number')
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', ax=axes[1, 2])
axes[1, 2].set_title('Correlation Heatmap')

plt.tight_layout()
plt.show()