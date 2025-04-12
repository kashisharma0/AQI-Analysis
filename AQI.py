# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 21:58:13 2025

@author: KASHISH
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('D:/Downloads/Air_Quality_Index.csv')
df.describe()
df.info()


# Data Cleaning
print(df.info())
print(df.isnull().sum())

for col in ['pollutant_min', 'pollutant_max', 'pollutant_avg']:
    df[col] = df[col].fillna(df[col].median())

print(df.isnull().sum())


#EDA:
    
#Insight 1: Distribution of Pollutant Averages
plt.figure(figsize=(10, 5))
plt.style.use('dark_background')
sns.histplot(df['pollutant_avg'], kde=True,bins=30, color='grey')
plt.title('Pollutant Average Distribution')
plt.xlabel('Pollutant Average',color='white')
plt.ylabel('Frequency',color='white')
plt.show()
#Most cities have relatively lower average pollution levels, but a few cities stand out with much higher values creating long tail of right skewness


#Insight 2: Top 10 Most Polluted Cities (Based on Average)
top_cities = df.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
plt.style.use('dark_background')
sns.barplot(x=top_cities.values, y=top_cities.index, palette='icefire')
plt.title('Top 10 Most Polluted Cities')
plt.xlabel('Average Pollutant Level')
plt.ylabel('City')
plt.show()
#Insight: These most polluted citie might be industrial areas.


#Insight 3: Boxplot for Outlier Detection in Pollutant Data
plt.style.use('dark_background')
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['pollutant_min', 'pollutant_avg', 'pollutant_max']],flierprops=dict(marker='o', color='red'))
plt.title('Pollution Values with Outliers')
plt.ylabel('Value')
plt.show()
#Insight: All three columns have outliers. Especially pollutant_max has extreme values maybe due to temporary pollution spikes.


# Insight 4: Heatmap of Correlations Between Pollution Metrics
plt.figure(figsize=(6, 4))
plt.style.use('dark_background')
sns.heatmap(df[['pollutant_min', 'pollutant_avg', 'pollutant_max']].corr(), annot=True, cmap='twilight', linewidths=0.5)
plt.title('Correlation Heatmap: Pollutant Levels')
plt.show()
#Insight: Strong positive correlation between all three pollutant values


# Insight 5: Pollution Type Frequency (pollutant_id)
plt.figure(figsize=(10, 6))
plt.style.use('dark_background')
sns.countplot(data=df, x='pollutant_id', order=df['pollutant_id'].value_counts().index, palette='twilight')
plt.title('Frequency of Monitored Pollutants')
plt.xlabel('Pollutant Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
#Insight: Some pollutants are monitored more frequently while others are not.


# Insight 6: Top 10 most polluted states
top_states = df.groupby('state')['pollutant_avg'].mean().sort_values(ascending=False).head(10)

plt.style.use('dark_background')
plt.figure(figsize=(10, 5))
sns.barplot(x=top_states.values, y=top_states.index, palette='rocket')
plt.title('Top 10 Most Polluted States')
plt.xlabel('Avg Pollutant Level')
plt.ylabel('State')
plt.show()
#Insight: Most polluted states are likely due to dense traffic, industrial activities, and limited green cover.



#Insight 7: Least polluted area
least = df[df['pollutant_avg'] == df['pollutant_avg'].min()]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='longitude', y='latitude', hue='pollutant_avg', palette='coolwarm_r', s=60)
plt.scatter(least['longitude'], least['latitude'], color='green', s=120, edgecolors='white', label='Least Polluted')
plt.title('Least Polluted Station Highlighted')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()




