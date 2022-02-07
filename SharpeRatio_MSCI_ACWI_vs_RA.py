#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)


# In[4]:


#Portfoliorendite
#Daten aus 'Broker-Vergleich'

dfr = pd.read_csv('Roboadvisor_returns.csv', index_col = 0)
dfr 


# In[5]:


# read etf closing prices
# Daten aus der Seite entnommen (https://de.investing.com/etfs/spdr-msci-acwi-imi-de-historical-data)

dfe = pd.read_csv('MSCI_ACWI_closingPrices.csv', index_col = 0)
dfe


# In[6]:


# calculate returns from MSCI ACWI 

returns = dfe.pct_change().dropna()
returns = returns * 100
returns


# In[7]:


#monthly return of the 3 RA and MSCI ACWI

mtl_return = pd.read_csv('mtl_return_MSCI_ACWI_RA.csv', index_col = 0)
mtl_return = mtl_return * 100
mtl_return


# In[9]:


((mtl_return/100)+1).cumprod().plot()


# In[7]:


# Daten wurden aus der folgenden Website entnommen
#https://de.investing.com/rates-bonds/usa-government-bonds?maturity_from=40&maturity_to=40
#Stand: 23.Dezember 2021 (in dem Zeitraum betrug der Wert 0.0355, (ca. 0,03))

rfr = 0.0355 


# In[8]:


#calculate excess return 

excess_return = mtl_return - rfr
excess_return


# In[9]:


#Mittelwert vom excess return

excess_return.mean()


# In[10]:


#Standardabweichung vom excess return

excess_return.std()


# In[11]:


#Berechnung Sharpe-Ratio

sharpe_ratio = excess_return.mean()/ excess_return.std()
sharpe_ratio


# In[ ]:




