import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("06-sales_data.csv", encoding='latin1')

# Convert Order Date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Year and Month
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()

sns.set_style("whitegrid")

# Create Dashboard
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# 1. Sales by Category
category_sales = df.groupby('Category')['Sales'].sum().sort_values()

sns.barplot(
    x=category_sales.values,
    y=category_sales.index,
    ax=axes[0,0]
)
axes[0,0].set_title("Sales by Category")

# 2. Profit by Category
category_profit = df.groupby('Category')['Profit'].sum().sort_values()

sns.barplot(
    x=category_profit.values,
    y=category_profit.index,
    ax=axes[0,1]
)
axes[0,1].set_title("Profit by Category")

# 3. Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()

sns.barplot(
    x=region_sales.index,
    y=region_sales.values,
    ax=axes[0,2]
)
axes[0,2].set_title("Sales by Region")

# 4. Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum()

sns.lineplot(
    x=monthly_sales.index,
    y=monthly_sales.values,
    marker='o',
    ax=axes[1,0]
)
axes[1,0].set_title("Monthly Sales Trend")
axes[1,0].tick_params(axis='x', rotation=45)

# 5. Top 10 Sub-Categories
sub_sales = (
    df.groupby('Sub-Category')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

sns.barplot(
    x=sub_sales.values,
    y=sub_sales.index,
    ax=axes[1,1]
)
axes[1,1].set_title("Top 10 Sub-Categories")

# 6. Sales Share by Category
sales_share = df.groupby('Category')['Sales'].sum()

axes[1,2].pie(
    sales_share.values,
    labels=sales_share.index,
    autopct='%1.1f%%'
)
axes[1,2].set_title("Sales Share")

plt.suptitle("Sales Data Analysis Dashboard", fontsize=18)
plt.tight_layout()
plt.show()