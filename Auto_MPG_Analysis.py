#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings

warnings.filterwarnings("ignore")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


# Display Settings
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# Load Dataset
def = pd.read_csv("auto-mpg.csv")

# Display first few rows
def.head()

 # Shape of the DataFrame
print("Shape of the DataFrame:", def.shape)

# Data types of each column
print("Data types:\n", def.dtypes)

# Check for missing values
print("Missing values:\n", def.isnull().sum())

# Handle Missing Values
def['hp'] = def['hp'].replace('?', np.nan)
def['hp'] = def['hp'].astype(float)
def['hp'].fillna(def['hp'].median(), inplace=True)

# Verify changes
print("Data types after cleaning:\n", def.dtypes)

# Transform 'origin' column
def['origin'] = def['origin'].replace({1: 'america', 2: 'europe', 3: 'asia'})

# Verify changes
def.head()

# Histograms
df.hist(figsize=(10, 12))
plt.show()

# Histograms
df.hist(figsize=(10, 12))
plt.show()

# Scatter Plot between Horsepower and MPG
plt.scatter(df['hp'], df['mpg'])
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.show()

# Pair Plot
sns.pairplot(df)
plt.show()

# Boxen Plot
sns.boxenplot(x='origin', y='mpg', data=df)
plt.show()

# FacetGrid Plot
g = sns.FacetGrid(df, col='origin', row='yr')
g.map(sns.scatterplot, 'cyl', 'acc')
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('FacetGrid Plot')
plt.show()

# Save the notebook
df.to_csv('Auto_MPG_Analysis_Completed.csv', index=False)


# In[ ]:




