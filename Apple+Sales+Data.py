
# coding: utf-8

# In[35]:


# Import our libraries

# This is for numerical processing
import numpy as np
# This is the library most commonly used for plotting in Python.
# Notice how we import it 'as' plt, this enables us to type plt
# rather than the full string every time.
import matplotlib.pyplot as plt


# In[37]:


start = '2012-01-01'
end = '2013-01-01'
data = get_pricing(['AAPL'], fields='price', start_date=start, end_date=end)
data.columns = [e.symbol for e in data.columns]

plt.hist(data['AAPL'], bins=20)
plt.xlabel('Prices')
plt.ylabel('Number of Days Observed')
plt.title('Frequency Distribution of MSFT Prices, 2012');
data.head()


# In[38]:


start = '2013-01-01'
end = '2014-01-01'
data = get_pricing(['AAPL'], fields='price', start_date=start, end_date=end)
data.columns = [e.symbol for e in data.columns]

plt.hist(data['AAPL'], bins=20)
plt.xlabel('Prices')
plt.ylabel('Number of Days Observed')
plt.title('Frequency Distribution of MSFT Prices, 2013');
data.head()


# In[39]:


start = '2014-01-01'
end = '2015-01-01'
data = get_pricing(['AAPL'], fields='price', start_date=start, end_date=end)
data.columns = [e.symbol for e in data.columns]

plt.hist(data['AAPL'], bins=20)
plt.xlabel('Prices')
plt.ylabel('Number of Days Observed')
plt.title('Frequency Distribution of MSFT Prices, 2014');
data.head()


# In[40]:


start = '2015-01-01'
end = '2016-01-01'
data = get_pricing(['AAPL'], fields='price', start_date=start, end_date=end)
data.columns = [e.symbol for e in data.columns]

plt.hist(data['AAPL'], bins=20)
plt.xlabel('Prices')
plt.ylabel('Number of Days Observed')
plt.title('Frequency Distribution of MSFT Prices, 2015');
data.head()


# In[41]:


start = '2016-01-01'
end = '2017-01-01'
data = get_pricing(['AAPL'], fields='price', start_date=start, end_date=end)
data.columns = [e.symbol for e in data.columns]

plt.hist(data['AAPL'], bins=20)
plt.xlabel('Prices')
plt.ylabel('Number of Days Observed')
plt.title('Frequency Distribution of MSFT Prices, 2016');
data.head()


# In[42]:


start = '2017-01-01'
end = '2018-01-01'
data = get_pricing(['AAPL'], fields='price', start_date=start, end_date=end)
data.columns = [e.symbol for e in data.columns]

plt.hist(data['AAPL'], bins=20)
plt.xlabel('Prices')
plt.ylabel('Number of Days Observed')
plt.title('Frequency Distribution of MSFT Prices, 2017');
data.head()

