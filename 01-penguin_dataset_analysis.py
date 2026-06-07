import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
penguins = sns.load_dataset('penguins')

# Basic Information
print("Dataset Shape:", penguins.shape)
print("\nDataset Info:")
print(penguins.info())

print("\nMissing Values:")
print(penguins.isnull().sum())

print("\nStatistical Summary:")
print(penguins.describe())

# Set style
sns.set_style("whitegrid")

# 1. Species Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=penguins, x='species', hue='species', palette='pastel', legend=False)
plt.title('Distribution of Penguin Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()

# 2. Island-wise Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=penguins, x='island', hue='species', palette='Set2')
plt.title('Penguin Species by Island')
plt.xlabel('Island')
plt.ylabel('Count')
plt.show()

# 3. Body Mass Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=penguins, x='body_mass_g',kde=True, bins=20)
plt.title('Distribution of Body Mass')
plt.xlabel('Body Mass (g)')
plt.ylabel('Frequency')
plt.show()

# 4. Flipper Length Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=penguins, x='flipper_length_mm', kde=True, bins=20)
plt.title('Distribution of Flipper Length')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Frequency')
plt.show()

# 5. Body Mass by Species
plt.figure(figsize=(8, 5))
sns.boxplot(data=penguins, x='species', y='body_mass_g', palette='Set3')
plt.title('Body Mass by Species')
plt.xlabel('Species')
plt.ylabel('Body Mass (g)')
plt.show()

# 6. Flipper Length by Species
plt.figure(figsize=(8, 5))
sns.boxplot(data=penguins, x='species', y='flipper_length_mm', palette='coolwarm')
plt.title('Flipper Length by Species')
plt.xlabel('Species')
plt.ylabel('Flipper Length (mm)')
plt.show()

# 7. Bill Length vs Bill Depth
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=penguins,
    x='bill_length_mm',
    y='bill_depth_mm',
    hue='species',
    s=80
)
plt.title('Bill Length vs Bill Depth')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.show()

# 8. Flipper Length vs Body Mass
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=penguins,
    x='flipper_length_mm',
    y='body_mass_g',
    hue='species',
    s=80
)
plt.title('Flipper Length vs Body Mass')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.show()

# 9. Gender Comparison
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=penguins,
    x='sex',
    y='body_mass_g',
    palette='pastel'
)
plt.title('Body Mass by Gender')
plt.xlabel('Sex')
plt.ylabel('Body Mass (g)')
plt.show()

# 10. Correlation Heatmap
numeric_data = penguins.select_dtypes(include='number')

plt.figure(figsize=(8, 6))
sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)
plt.title('Correlation Heatmap')
plt.show()

# 11. Pairplot
sns.pairplot(
    penguins,
    hue='species',
    diag_kind='hist'
)
plt.show()