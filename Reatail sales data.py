# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt


# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory



# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
data = pd.read_csv('retail_sales_dataset.csv')
print(data.head())
print(data.describe())
print(data.isnull().sum())
print(data.dtypes)

data.select_dtypes(include=['object'])
for col in data.select_dtypes(include=['object']):
    print(data[col].value_counts())
# cleaning
data['Age'].fillna(data['Age'].mean(), inplace=True)
data['Date'] = pd.to_datetime(data['Date'])
data['Product Category'] = data['Product Category'].str.strip()
data.drop_duplicates(inplace=True)

data.set_index('Date', inplace=True)

# Plot time series data
data['Total Amount'].plot(figsize=(12, 6))  # Replace 'sales' with your sales column name
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()


# Calculate 7-day moving average
data['moving_average_7'] = data['Total Amount'].rolling(window=7).mean()

# Plot original sales with moving average
data[['Total Amount', 'moving_average_7']].plot(figsize=(12, 6))
plt.title('Sales vs. 7-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()


# Describe customer demographics 
customer_demographics = data[['Customer ID', 'Age', 'Gender']]
print(customer_demographics.describe(include='all'))  # Summary statistics

# Group by demographics and analyze purchase behavior (average spend, frequent items)
grouped_by_age = data.groupby('Age').agg({'Total Amount': 'mean', 'Quantity': 'nunique'})  

print(grouped_by_age)

# Visualize demographics (histograms, boxplots)
customer_demographics.hist(figsize=(10, 6))  # Histogram of age
plt.show()

# Total sales
total_sales = data['Total Amount'].sum()
print(f"Total sales: ${total_sales:.2f}")

# Sales by product category
category_sales = data.groupby('Product Category')['Total Amount'].sum()
print(f"\nTop 3 selling categories:")
print(category_sales.sort_values(ascending=False).head(3))

# Customer purchase frequency
customer_frequency = data.groupby('Customer ID')['Transaction ID'].count()
print(f"\nAverage purchase frequency per customer: {customer_frequency.mean():.2f}")

# Total Sales
total_sales = data['Total Amount'].sum()
print(f"Total Sales: ${total_sales:.2f}")

# Sales by Product Category
category_sales = data.groupby('Product Category')['Total Amount'].sum()

# Plot Top 5 Selling Categories (Bar Chart)
top_5_categories = category_sales.sort_values(ascending=False).head(5)
plt.figure(figsize=(10, 6))
top_5_categories.plot(kind='bar', color='skyblue')
plt.title('Top Selling Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')  # Rotate category labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Customer Purchase Frequency
customer_frequency = data.groupby('Customer ID')['Transaction ID'].count()

# Distribution of Purchase Frequency (Histogram)
plt.figure(figsize=(8, 6))
customer_frequency.plot.hist(bins=10, edgecolor='black')  # Adjust 'bins' for desired granularity
plt.title('Distribution of Customer Purchase Frequency')
plt.xlabel('Number of Purchases')
plt.ylabel('Number of Customers')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Average Purchase Value per Customer
avg_purchase_value = data.groupby('Customer ID')['Total Amount'].mean()


# Analyze by Gender:

# Average purchase value by gender
avg_purchase_value_gender = data.groupby('Gender')['Total Amount'].mean()
print(f"\nAverage purchase value by gender:")
print(avg_purchase_value_gender)

# Purchase frequency by gender
purchase_frequency_gender = data.groupby('Gender')['Transaction ID'].count()
print(f"\nPurchase frequency by gender:")
print(purchase_frequency_gender)

# ... (similar analysis for other metrics like total spending per gender)

# Analyze by Age Group:

# Bin age into groups (replace with your desired age ranges)
data['Age Group'] = pd.cut(data['Age'], bins=[18, 25, 35, 45, 65, 100])

# Average spending per age group
avg_spend_age_group = data.groupby('Age Group')['Total Amount'].mean()
print(f"\nAverage spending per age group:")
print(avg_spend_age_group)


customer_frequency = data.groupby('Customer ID')['Transaction ID'].count()
plt.figure(figsize=(5, 3))
plt.scatter(data['Age'], customer_frequency)
plt.title('Purchase Frequency vs. Age')
plt.xlabel('Age')
plt.ylabel('Purchase Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()





















































