import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "StudentsPerformance.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Load data
df = pd.read_csv(DATA_FILE)

print("\n=== STUDENT PERFORMANCE ANALYTICS ===")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# 2. Standardize column names
df.columns = [
    c.strip().lower().replace("/", "_").replace(" ", "_")
    for c in df.columns
]

# 3. Data quality checks
print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATES ===")
print(df.duplicated().sum())

# 4. Remove duplicate rows if any
df = df.drop_duplicates().copy()

# 5. Feature engineering
score_cols = ["math_score", "reading_score", "writing_score"]
df["total_score"] = df[score_cols].sum(axis=1)
df["average_score"] = df[score_cols].mean(axis=1)

def performance_level(score):
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Average"
    return "Needs Improvement"

df["performance_level"] = df["average_score"].apply(performance_level)

# 6. Descriptive statistics
print("\n=== SCORE SUMMARY ===")
print(df[score_cols + ["total_score", "average_score"]].describe().round(2))

print("\n=== PERFORMANCE LEVEL ===")
print(df["performance_level"].value_counts())

# 7. Group analysis
print("\n=== AVERAGE SCORE BY GENDER ===")
print(df.groupby("gender")[score_cols + ["average_score"]].mean().round(2))

print("\n=== TEST PREPARATION IMPACT ===")
print(df.groupby("test_preparation_course")[score_cols + ["average_score"]].mean().round(2))

print("\n=== PARENTAL EDUCATION ===")
parental = (
    df.groupby("parental_level_of_education")["average_score"]
    .mean()
    .sort_values(ascending=False)
)
print(parental.round(2))

print("\n=== LUNCH TYPE ===")
print(df.groupby("lunch")["average_score"].mean().round(2))

# 8. Save cleaned dataset
df.to_csv(OUTPUT_DIR / "cleaned_student_performance.csv", index=False)

# 9. Visualizations
plt.figure(figsize=(8, 5))
sns.histplot(df["average_score"], bins=20, kde=True)
plt.title("Distribution of Average Student Scores")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "01_average_score_distribution.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="gender", y="average_score", errorbar=None)
plt.title("Average Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "02_gender_average_score.png", dpi=150)
plt.close()

prep_avg = df.groupby("test_preparation_course", as_index=False)["average_score"].mean()
plt.figure(figsize=(8, 5))
sns.barplot(data=prep_avg, x="test_preparation_course", y="average_score", errorbar=None)
plt.title("Average Score by Test Preparation Course")
plt.xlabel("Test Preparation Course")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "03_test_preparation_impact.png", dpi=150)
plt.close()

plt.figure(figsize=(10, 5))
sns.barplot(
    data=df,
    x="parental_level_of_education",
    y="average_score",
    errorbar=None
)
plt.title("Average Score by Parental Education")
plt.xlabel("Parental Level of Education")
plt.ylabel("Average Score")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "04_parental_education.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="gender", y="average_score")
plt.title("Average Score Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "05_score_distribution_gender.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="reading_score", y="writing_score", hue="gender", alpha=0.65)
plt.title("Reading Score vs Writing Score")
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "06_reading_vs_writing.png", dpi=150)
plt.close()

plt.figure(figsize=(7, 5))
corr = df[score_cols + ["average_score"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f")
plt.title("Score Correlation Heatmap")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "07_correlation_heatmap.png", dpi=150)
plt.close()

# 10. Final insights
best_prep = df.groupby("test_preparation_course")["average_score"].mean()
prep_gap = best_prep.max() - best_prep.min()

best_parent_group = parental.index[0]
best_parent_score = parental.iloc[0]

print("\n=== KEY INSIGHTS ===")
print(f"Overall average score: {df['average_score'].mean():.2f}")
print(f"Highest average subject score: {df[score_cols].mean().idxmax()}")
print(f"Test-preparation average-score gap: {prep_gap:.2f} points")
print(f"Highest parental-education group average: {best_parent_group} ({best_parent_score:.2f})")
print(f"Excellent performers (average >= 80): {(df['average_score'] >= 80).sum()}")

print(f"\nAnalysis complete. Files saved in: {OUTPUT_DIR}")
