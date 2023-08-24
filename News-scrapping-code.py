#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.get('https://8am.media/eng/11-civilians-killed-by-taliban-in-central-afghanistans-daikundi-province/')
response=requests.get('https://8am.media/eng/11-civilians-killed-by-taliban-in-central-afghanistans-daikundi-province/')
response=response.content
from requests.models import Response
soup=BeautifulSoup(response,'html.parser')

book= []
header=soup.find('h1',class_='single-post-title').text
time=soup.find('span',class_='time').text
ref=soup.find('span',class_='post-author-name').text
content=soup.find('div',class_='entry-content clearfix single-post-content').text

book.append([header,time,ref,content])
df=pd.DataFrame(book,columns=['header','time','ref','content'])
df.to_csv('example8.csv')


# In[2]:


print(df)


# In[ ]:




