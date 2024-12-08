import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


data = pd.read_csv("../data/solar_data.csv")

# to Summary Statistics
print("Summary Statistics:")
summary = data.describe()
print(summary)

#  for Data Quality Check
print("\nMissing Values:")
missing_values = data.isnull().sum()
print(missing_values)

# Handle Missing Values
data['GHI'] = data['GHI'].fillna(data['GHI'].mean())

# Time Series Analysis
print("\nTime Series Visualization:")
data['Date'] = pd.to_datetime(data['Date'])
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['GHI'], label="Global Horizontal Irradiance (GHI)")
plt.xlabel('Date')
plt.ylabel('GHI')
plt.title('GHI Trends Over Time')
plt.legend()
plt.show()


# Correlation Analysis
print("\nCorrelation Heatmap:")
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Wind and Temperature Analysis
print("\nRadial Plot of Wind Speed and Direction:")
fig = px.scatter_polar(data, r='WS', theta='WD', title="Wind Speed vs. Wind Direction")
fig.show()

# Data Cleaning
print("\nCleaning Data: Removing invalid GHI values")
data = data[data['GHI'] > 0]

# Advanced Visualization: Bubble Chart
print("\nBubble Chart Visualization:")
plt.figure(figsize=(8, 6))
plt.scatter(data['GHI'], data['Tamb'], s=data['RH'] * 10, alpha=0.5, label="Relative Humidity Bubble Size")
plt.xlabel('GHI')
plt.ylabel('Ambient Temperature (Tamb)')
plt.title('Bubble Chart: GHI vs. Tamb with RH')
plt.legend()
plt.show()