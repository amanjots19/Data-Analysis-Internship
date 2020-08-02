
# coding: utf-8

# In[1]:


import pandas as pd
df= pd.read_csv(r"C:\Users\Gurkirat Singh\Documents\avocado-prices\avocado.csv")
df.head()


# In[2]:


albany_df=df[df['region']=="Albany"]


# In[3]:


albany_df.set_index("Date")


# In[4]:


albany_df=albany_df.set_index("Date")


# In[5]:


albany_df['AveragePrice'].plot()

