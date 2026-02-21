import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('marksheet.csv')
print(df.head())
print(df.isnull().sum())
print(df.describe())
df['Total']=df['Maths'] + df['Science'] + df['English'] + df['History']
df['Percentage'] = (df['Total']/400)*100
df['Status'] = np.where(df['Percentage'] >= 33, 'Pass','Fail')
print(df[['Total', 'Percentage' , 'Status']].head())
def assign_grade(pct):
    if pct >= 90: return 'A+'
    elif pct >= 80: return 'A'
    elif pct >= 70: return 'B'
    elif pct >= 60: return 'C'
    else: return 'D/F'

df['Grade'] = df['Percentage'].apply(assign_grade)
sns.countplot(x='Grade', data=df, palette='viridis')
plt.title('Distribution of student grades')
plt.show()

plt.scatter(df['Maths'], df['Science'], color='blue')
plt.xlabel('Maths Marks')
plt.ylabel('Maths vs Science performace')
st.pyplot()
print(f"Average Percentage of Class: {df['Percentage'].mean():.2f}%")
print(f"Highest Marks Obtained: {df['Total'].max()}")
print(f"Number of Students Passed: {df[df['Status'] == 'Pass'].shape[0]}")