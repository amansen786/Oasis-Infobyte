import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv("creditcard.csv")
print(df.head)
print(df.shape)
print(df.isnull().sum())
print(df.drop_duplicates(inplace=True))
print(df.columns)
print(df.nunique())


#Check fraud and valid case
fraud = df [df['Class'] == 1]
valid = df[df['Class'] == 0]
outlierfraction = len(fraud)/float(len(valid ))
print(outlierfraction)

print('Fraud Cases: {}'.format(len(df[df['Class'] == 1])))
print('Valid Transactions: {}'.format(len(df[df['Class'] == 0])))

#Check statical summary
fraud.Amount.describe()

#Class distribution

plt.figure(figsize=(6, 4))
sns.countplot(x='Class', data=df)
plt.title('Class Distribution')
plt.show()

#Separate x & y


X = df.drop(columns=['Class'])
y = df['Class']