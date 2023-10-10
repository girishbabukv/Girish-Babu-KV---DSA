#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# # Installing xlrd library to read data and formating function from Excel files

# In[2]:


pip install xlrd


# # Reading Data Set

# In[5]:


var_name=pd.read_excel('/Users/girishbabukv/Downloads/iris.xls')
df=pd.read_excel('/Users/girishbabukv/Downloads/iris.xls')


# # Displaying Headings (Not part of the assignment)

# In[6]:


df.head()


# # Displaying Columns 

# In[9]:


df.columns


# # Displaying mean for all columns 

# In[10]:


df.mean()


# # Displaying Null Values 

# In[18]:


df.isnull()


# # Meaningful Visualisations 

# In[ ]:


# A count plot for SL with classification


# In[61]:


sns.countplot(x='SL',data=df,hue='Classification')


# In[ ]:


# A Scatter plot with SW and PW in x and y axes, and their classification


# In[34]:


sns.scatterplot(x='SW', y='PW',hue= 'Classification',data=df)


# In[ ]:


# Printing Column heads for reference to plot other manps


# In[27]:


print (df.columns)


# In[ ]:


# A Boxplot with SL and PL in x and y axes, and their classification


# In[36]:


sns.boxplot(x='SL', y='PL',hue= 'Classification',data=df)


# In[ ]:


A Displot with a count of all columns, and  their classification


# In[44]:


sns.displot(df,bins=20,color='r')


# In[ ]:


A Jointplot showing the frequency of all Classifications with PW and SW in x and y axes


# In[55]:


sns.jointplot(x='PW',y='SW',hue='Classification',data=df)


# In[ ]:




