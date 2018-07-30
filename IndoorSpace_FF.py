
#******************************************************************************************************
# Human traffice pattern recognition from INFINITY
# Courtesy of innerspace.io and Mr. Matt MacGillivray

# *****************************************************************************************************
# Created by Babak khamsehi (BK), July 8th, 2018
# Modified by BK, July 9th, 2018

#*********************************************************************************************************************

# ********************************************************************************************************************
# Reading in the Traffic data 
# In[38]:


import pandas as pd
df= pd.read_csv('C:/Google Drive/IndoorSpace/visits_160_excluded.csv') # Please adjust the address based on the location of data in your computer
df.columns


# ### Mapping source_hex as unique_person_id 
# 

# In[39]:


df2=df.copy()
df2.sort_values(by=['source_hex'], inplace=True)     # df2 is based on the sex_hex, person id 
u_p_id = pd.DataFrame(df['source_hex'].unique(),columns=['unique_person_id'])  # Unique person id (source_hex)
unique_person_id= u_p_id['unique_person_id']

human_id_mapping = {
       '30ec7160e0a2f83a9003b7e75129e850':  'p1',  
       '2b5b3bf5c1d17b44f6246d340b5121c2':  'p2', 
       'c0dceed99f5bad2f4635cb7628e838c6':  'p3',
       '050cd64aac3715ecb6df0dd943e747f3':  'p4',
       'b9c098f661d01e326ee651cbdbb11761':  'p5',
       'f2526dc79ef822ca10b6e28fedbd86ce':  'p6', 
       'ee150fcc48152a6e20a08e3b51180868':  'p7',
       '46dcd1e3c5ae5a2a53bb06765dcc6a55':  'p8',
       '17418357da33c40de30e1879e546e21e':  'p9',
       '4160c923a7a6b2a0ffc1e5db5c36989f': 'p10',
       
       '1f262ea09f9d9302a03e14c8a2281f97':  'p11',  
       '42dc2796e28ced02bfcb6d0de120ddb9':  'p12', 
       'baa4beaf52e8ba7409d4a68b6ad5ad1e':  'p13',
       '4d4a79e891fe4dde52a734e1795cc27a':  'p14',
       '31e42715b2e804ada500701a879f3d8d':  'p15',
       '69d0c57d0863626cfb5c94fbda6beb52':  'p16', 
       '9c4e2855ab0f25230b1a0733fd948a32':  'p17',
       '0d16158751e6fa0566388bef8946e9f1':  'p18',
       '6bb88b3cf8c1bf99092eb4ad58e95bea':  'p19',
       'fe601403b23ddf94efe00414ae1a98a6':  'p20',
       
       '79643e9b836f51793ac4f63556d843fe':  'p21',  
       '3ec8442719c03a6124f473fa6e3c6503':  'p22', 
       '2f45d480a34f8e0738bdbd7b4e83040a':  'p23',
       '553f8bd78eb06826bc7bb006dfbad588':  'p24',
       '2fc02212836aa8d68f349a968c68f2ec':  'p25',
       'aa4c554571ae5a3852f52963fc0b42e4':  'p26', 
       '6cc94272b7ed56a2b9b14549db3e8719':  'p27',
       '1d6749bc1b670feb5b9df8f30b8f3006':  'p28',
       '16d72e3a64ae073a5eca28ce65190846':  'p29',
       '7b39d9caa1979eeacdd8cc8d5cdc72f6':  'p30',
       
       'ed82dacd0cf11dd22a675d425cdcb6e9':  'p31',  
       '104239211470ec86044140dfdd90b256':  'p32', 
       'c0fd9784441d00890126c2f49f5777e6':  'p33',
       'f2282a0223d491bf99a0bfe281809f8f':  'p34',
       'e55a2709e445ea8e9d1b25c9223c2abe':  'p35',
       '38332e5384f871fdc2c5fcd996372076':  'p36', 
       'e874d06ce48f095455d84517d6c93cc0':  'p37',
       '6fe34098733d888d13f2ff23fe097516':  'p38',
       '8baeeea3e72eb5b5013fe4f5a4620436':  'p39',
       '2ae4df228b51f6f5f2d5298447f50889':  'p40',
       
       '61d8c302e13cccbcf1f5b5f1f59f0414':  'p41',  
       '9123d49899177a02119586c126aee7f9':  'p42', 
       '853c2335dfb3e91909ef29d5cb681f76':  'p43',
       '0561cd167a6e1e619deaeb92ad9d80eb':  'p44',
       '85e81d9effa95bed02a31547e175525a':  'p45',
       '4e45267cc992c902f01e92c81a8a5c69':  'p46', 
       'fad4589318efc5463df9131abf7750e1':  'p47',
       'e0495ef1dc969766517cf87cf0fd468c':  'p48',
       '2833a06c6bda053e9b5e3690a9ca2023':  'p49',
       '9abc0835cd9464b7b2a775082f13b34c':  'p50',
       
       '1cc1543a17b21a3dcc1a69266759432f':  'p51',  
       '72d07be60dfb5bb324651819a15d328c':  'p52', 
       '03c2b11cd50834418b24afc39ded0690':  'p53',
       '9014cceee8fa33b6ca6c4957ed6b06d2':  'p54',
       '50d429a3c5b185a0b49dfce51a9f1d82':  'p55',
       '7dbb67231b7358f390bb86ee22b756d1':  'p56', 
       'f62800f7da139f0cbd1d92f6a9a3eabd':  'p57',
       '1eec3b347c7d2d9df4db4e78ae6fa17f':  'p58'}

u_p_id['unique_person_id'] = u_p_id['unique_person_id'].map(human_id_mapping)
df2['source_hex'] =df2['source_hex'].map(human_id_mapping)
df2=df2.drop(['id', 'visit_count'],axis=1)                      # Given by Matt
df2=df2.drop(['site_id'],axis=1)                                # Site_id does not change. Therefore, it will not influence our analysis and results
df2= df2.rename(columns={'source_hex': 'unique_person_id'})     # Renaming source_hex
df2.head(10)


# ### Extracting start_date  from date_time_start

# In[40]:


df2.dtypes 
# ^^ date_time_start  are both objects (rather than pandas date_time ^^  
df2['date_start']=pd.to_datetime(df2['date_time_start'])     # converting to date_time

df2.dtypes

df2['date_start']= df2.date_start.dt.date
               
# extracting start_date  from date_time_start
df2.dtypes 
# ^^ date_time_start  are both objects (rather than pandas date_time ^^  

df2['date_end']=pd.to_datetime(df2['date_time_end'])  # converting to date_time
df2.dtypes

df2['date_end']= df2.date_end.dt.date                 # extrating just the date_start
df2.head(10)


# In[41]:


df2.to_csv('C:/Google Drive/IndoorSpace/df2.csv')
df2= pd.read_csv('C:/Google Drive/IndoorSpace/df2.csv')


# In[42]:


df2= df2.rename(columns={'duration_mins': 'duration_mins_hh:mm'})     # Renaming duration_mins to match its format
df2['duration_mm']= (pd.to_datetime(df2['date_time_end'])-pd.to_datetime(df2['date_time_start']))

df2.dtypes


# ### Converting duration_mm to timedelta64 which is float64(we will use it sum up in the following sections)

# In[43]:


df2['duration_mm']= df2['duration_mm'].astype('timedelta64[m]')
df2.dtypes


# ## Investigating traffic in  all zones :
# ### Total time in minutes in all zones for unique persons
# 

# ### Total time in minutes in all zones for 58 unique persons 

# In[44]:


df2['date'] =df2['date_start']
dfp1= df2.groupby('unique_person_id')["duration_mm"].sum().rename("time_all_zone_mins").reset_index()
dfp1.dtypes
dfp1.head(len(dfp1))


# ### Finding the max time and the person associated with it

# In[45]:


max_time_all_zone_mins= dfp1['time_all_zone_mins'].max()
id_max= dfp1['time_all_zone_mins'].idxmax()
t_max= (id_max, max_time_all_zone_mins)
print(t_max)


# #### Max time is 49,377 mins associated with p24 

# In[46]:


min_time_all_zone_mins= dfp1['time_all_zone_mins'].min()
id_min= dfp1['time_all_zone_mins'].idxmin()
t_min= (id_min, min_time_all_zone_mins)
print(t_min)


# #### Min time is 3,859 mins associated with p30 

# ### Total  counts in all zones for 16 unique dates

# In[47]:


## Investigating the total counts in all zones at the existing dates
dfp2= df2.groupby('date')["unique_person_id"].size().rename("count_all_zones")
dfp2 = dfp2.reset_index()
dfp2.dtypes
dfp2['date']=pd.to_datetime(dfp2['date'])  # converting to date_time
dfp2.dtypes
dfp2['weeday_name']= dfp2.date.dt.weekday_name              # extrating weekday name
dfp2.head(len(dfp2))


# In[48]:


max_count_all_zones= dfp2['count_all_zones'].max()
id_max= dfp2['count_all_zones'].idxmax()
t_max= (id_max, max_count_all_zones)
print(t_max)


# #### Max count for all zones  is 2,734 and it happens on Thursday, 2018-02-08 

# In[49]:


min_count_all_zones= dfp2['count_all_zones'].min()
id_min= dfp2['count_all_zones'].idxmin()
t_min= (id_max, min_count_all_zones)
print(t_min)


# #### Min count for all zones  is 1,499 and it happens on Monday, 2018-02-05 

# ## Plotting the time series
# 

# In[50]:


import matplotlib.pyplot as plt
dfp2.dtypes
dfp2['day_of_year']= dfp2['date'].dt.dayofyear
plt.plot(dfp2['day_of_year'],dfp2['count_all_zones'])
plt.xlabel('ordinal day of the year')     # add a label to the x axis
plt.ylabel('Total counts of all zones')   # add a label to the y axis
plt.title('Total counts of all zones over 16 days of the study in 2018') # add a title

plt.show()

dfp2.to_csv('C:/Google Drive/IndoorSpace/dfp2.csv') # A backup copy of the generated dataframe


# # Conclusions:
# 
# ### We presented two measures of total traffic in all the zones: 
# ### measure 1, based on total time spent in all of zones for 58 unique persons
# ### measure 2, based on total counts of persons for the16 unique study dates in 2018
# 
# ### Across the 58 unique humans visting the site: 
# ### We showed that Person24  had the highest  total spent in all zones
# ### We showed that Person30  had the lowest  total spent in all zones
# 
# 
# ### Over the 16 day of study period in 2018:
# ### We showed that Thursday, 2018-02-08 had the highest  traffic counts
# ### We showed that  Monday,   2018-02-05 had the lowest traffic counts
# 

# ## Future possiblities:
# ### With more time, effort, and bigger data sets, we can have a better understanding of trajectories  and overall clusters.
# 
# ### With bigger datasets, with can investigate the effects of some additional features such as day of the week
# 
# ### In addition, we can test additional hypotheses. For instance, we can test, if there would be less traffic, in rainy days, versus sunny days (once merged with weather data)
