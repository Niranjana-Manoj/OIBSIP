# -*- coding: utf-8 -*-
"""Copy of Sales Prediction using Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YkxNBcnd40f0Z8PDijxJiEhhe26uoCvU

**IMPORT LIBRARIES**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("/content/Advertising.csv")

data.head(10)

data.drop('Unnamed: 0', axis=1, inplace=True)

data.info()

data.isnull().sum





data.describe()

"""**EDA**

Distribution of sales
"""

plt.figure(figsize=(10, 6))
sns.histplot(data['Sales'], bins=30, kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

"""Relationship betwen numerical features"""

sns.pairplot(data, vars=['TV', 'Radio', 'Newspaper', 'Sales'])
plt.title('Pairplot of Numerical Features ')
plt.show()

"""Correlation Heatmap"""

plt.figure(figsize=(8, 6))
correlation_matrix = data[['TV', 'Radio', 'Newspaper', 'Sales']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

"""**MODELING**

Split the data
"""

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data[["TV"]], data[["Sales"]], test_size=0.3, random_state=42)

"""LINEAR REGRESSION MODEL"""

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train)

"""**MODEL EVALUATION**"""

predictions = model.predict(x_test)

plt.figure(figsize=(8, 6))
plt.scatter(x_test, y_test, color='blue', label='Actual Sales')
plt.plot(x_test, predictions, color='red', linewidth=2, label='Predicted Sales')
plt.title('Linear Regression - TV Advertising vs. Sales')
plt.xlabel('TV Advertising Budget')
plt.ylabel('Sales')
plt.legend()
plt.show()