import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Superstore.csv")


print(df)
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.duplicated())
print(df.duplicated().sum())
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Sales"] < lower) | (df["Sales"] > upper)]

print("\nNumber of Outliers:")
print(len(outliers))

# Boxplot
plt.figure(figsize=(8,5))
plt.boxplot(df["Sales"])
plt.title("Sales Outliers")
plt.show()

# 8. Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# 9. GroupBy Analysis
print("\nSales by Category")
print(df.groupby("Category")["Sales"].sum())

print("\nProfit by Category")
print(df.groupby("Category")["Profit"].sum())

# 10. Create 5 Charts

# Chart 1
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.show()

# Chart 2
df.groupby("Category")["Profit"].sum().plot(kind="bar")
plt.title("Profit by Category")
plt.show()

# Chart 3
plt.hist(df["Sales"], bins=30)
plt.title("Sales Distribution")
plt.show()

# Chart 4
plt.hist(df["Profit"], bins=30)
plt.title("Profit Distribution")
plt.show()

# Chart 5
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

# 11. Correlation Analysis
numeric_df = df.select_dtypes(include=np.number)

corr_matrix = numeric_df.corr()

print("\nCorrelation Matrix:")
print(corr_matrix)

# Correlation Heatmap using Matplotlib
plt.figure(figsize=(8,6))
plt.imshow(corr_matrix, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.title("Correlation Matrix")
plt.show()