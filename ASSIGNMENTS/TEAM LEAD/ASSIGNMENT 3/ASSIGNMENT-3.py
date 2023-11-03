#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[31]:


#Load the dataset
Hou=pd.read_csv(r"C:\Users\semil\OneDrive\Desktop\ASSIGNMENT\House Price India.csv")


# In[32]:


print(Hou.shape)
Hou.head()


# In[35]:


#Univariate Analysis
sns.histplot(Hou, x='Price', kde=True)
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Histogram of Price')
plt.show()


# In[36]:


sns.histplot(Hou, x='number of bedrooms', kde=True)
plt.xlabel('number of bedrooms')
plt.ylabel('Frequency')
plt.title('Histogram of Price')
plt.show()


# In[37]:


sns.countplot(data=Hou, x='number of bathrooms')
plt.title('Count of Number of Bathrooms')
plt.show()


# In[38]:


#Bi-Variate Analysis
sns.barplot(data=Hou, x='waterfront present', y='Price')
plt.title('Waterfront Present vs. Price')
plt.show()


# In[39]:


sns.scatterplot(data=Hou, x='living area', y='Price')
plt.title('Living Area vs. Price')
plt.show()


# In[40]:


#Multi-Variate Analysis
corr_matrix = Hou.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# In[44]:


sns.pairplot(Hou[['living area', 'lot area', 'number of floors', 'Price']])
plt.title('Pairplot of Selected Variables')
plt.show()


# In[53]:


#descriptive statistics
Hou.describe()


# In[51]:


#Handle the Missing values
missing_values = Hou.isna().sum()
print(missing_values)


# In[ ]:




