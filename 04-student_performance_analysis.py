import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("04-student_performance.csv")

# Create Total Marks column
df["Total_Marks"] = df["Math"] + df["Science"] + df["English"]

# Style
sns.set_style("whitegrid")

# Create Dashboard
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# 1. Average Marks by Subject
subject_avg = df[["Math", "Science", "English"]].mean()
sns.barplot(
    x=subject_avg.index,
    y=subject_avg.values,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Average Marks by Subject")
axes[0, 0].set_ylabel("Average Score")

# 2. Gender-wise Total Marks
sns.boxplot(
    data=df,
    x="Gender",
    y="Total_Marks",
    ax=axes[0, 1]
)
axes[0, 1].set_title("Gender-wise Performance")

# 3. Attendance vs Total Marks
sns.scatterplot(
    data=df,
    x="Attendance",
    y="Total_Marks",
    hue="Gender",
    ax=axes[0, 2]
)
axes[0, 2].set_title("Attendance vs Total Marks")

# 4. Total Marks Distribution
sns.histplot(
    data=df,
    x="Total_Marks",
    bins=10,
    kde=True,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Distribution of Total Marks")

# 5. Correlation Heatmap
numeric_df = df[["Math", "Science", "English", "Attendance", "Total_Marks"]]
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    ax=axes[1, 1]
)
axes[1, 1].set_title("Correlation Heatmap")

# 6. Top 10 Students
top10 = df.nlargest(10, "Total_Marks")

sns.barplot(
    data=top10,
    x="Student_ID",
    y="Total_Marks",
    ax=axes[1, 2]
)
axes[1, 2].set_title("Top 10 Students")
axes[1, 2].set_xlabel("Student ID")

plt.tight_layout()
plt.show()

# ---------------------------
# Pairplot (Separate Figure)
# ---------------------------

sns.pairplot(
    df[["Math", "Science", "English", "Attendance"]],
    diag_kind="hist"
)

plt.show()