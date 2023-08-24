#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
GTD=pd.read_csv(r"C:\Users\Mina\Desktop\test\Merge-Data\globalterrorismdb_0522dist.csv")
output= GTD[(GTD.country_txt =='Afghanistan') & (GTD.city == 'Kabul') & (GTD.iyear>2010)  & (GTD.targtype1_txt!='Military')
   &(GTD.targtype1_txt!='Police') &  (GTD.targtype1_txt!='Airports & Aircraft') & (GTD.targtype1_txt!='Government (Diplomatic)') & (GTD.targtype1_txt!='Government (General)')
   & (GTD.targtype1_txt!='Tourists')  & (GTD.targtype3_txt!='Journalists & Media') & (GTD.natlty1_txt!='France') & (GTD.natlty1_txt!='United States')& (GTD.natlty1_txt!='Great Britain')
   &  (GTD.targsubtype1_txt!='Aircraft (not at an airport)')   & (GTD.attacktype1_txt!='Hostage Taking (Kidnapping)')
  &(GTD.targtype1_txt!='Journalists & Media') &(GTD.nkill>2.0)  &(GTD.success!=0)&  (GTD.attacktype1_txt!='Assassination')
  &  (GTD.attacktype1_txt!='Hostage Taking (Barricade Incident)') ]


# In[2]:


output.to_csv=(r'C:\Users\Mina\Desktop\target\final-GTD.csv')


# In[3]:


print(output)


# In[ ]:




