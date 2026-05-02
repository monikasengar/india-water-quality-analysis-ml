#!/usr/bin/env python
# coding: utf-8

# # 1. Rivers

# In[ ]:


import pandas as pd
df = pd.read_csv(r'C:\Users\monik\Downloads\for_cleaning_1\rivers_cl1.csv')
print(df.head())


# In[ ]:


df


# In[ ]:


df.info()


# # visualization

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\monik\Downloads\for_cleaning_1\python_cleaning\rivers_python_cleaned.csv')

def plot_river_data(df, parameter, y_label):
    plt.figure(figsize=(25, 6))
    for river in df['river'].unique():
        river_data = df[df['river'] == river]
        plt.plot(river_data.index, river_data[parameter], label=river)
    plt.xlabel('Sample Index')
    plt.ylabel(y_label)
    plt.title(f'{y_label} Across Different Rivers')
    plt.legend()
    plt.show()
# Plotting the data
plot_river_data(df, 'Minimum temperature for river water', 'Minimum Temperature')
plot_river_data(df, 'Maximum temperature for river water', 'Maximum Temperature')
plot_river_data(df, 'Minimum value of dissolved oxygen', 'Minimum Dissolved Oxygen')
plot_river_data(df, 'Maximum value of dissolved oxygen', 'Maximum Dissolved Oxygen')
plot_river_data(df, 'Minimum potential of Hydrogen value in river water', 'Minimum pH')
plot_river_data(df, 'Maximum potential of Hydrogen value in river water', 'Maximum pH')
plot_river_data(df, 'Minimum Conductivity Level', 'Minimum Conductivity')
plot_river_data(df, 'Maximum Conductivity Level', 'Maximum Conductivity')
plot_river_data(df, 'Minimum Biochemical oxygen demand', 'Minimum Biochemical Oxygen Demand')
plot_river_data(df, 'Maximum Biochemical oxygen demand', 'Maximum Biochemical Oxygen Demand')
plot_river_data(df, 'Minimum of Nitrate N + Nitrite N required ', 'Minimum Nitrate + Nitrite')
plot_river_data(df, 'Maximum of Nitrate N + Nitrite N required ', 'Maximum Nitrate + Nitrite')
plot_river_data(df, 'Minimum of Faecal Coliforms required for river water', 'Minimum Faecal Coliforms')
plot_river_data(df, 'Maximum  of Faecal Coliforms required for river water', 'Maximum Faecal Coliforms')
plot_river_data(df, 'Minimum coliform required for river water', 'Minimum Coliform')
plot_river_data(df, 'Maximum coliform required for river water', 'Maximum Coliform')


# # 2. Medium minor rivers

# In[ ]:


import pandas as pd
df2 = pd.read_csv(r'C:\Users\monik\Downloads\for_cleaning_1\medium_minor_rivers_cl1.csv')
#print(df.head())


# In[ ]:


df2


# In[ ]:


df2.info()


# In[ ]:


df2["Station name"].str.split(',', expand = True)


# In[ ]:


df2[["river", "state", "city", "3", "4"]] = df2["Station name"].str.split(',', expand = True)


# In[ ]:


df2


# In[ ]:


df2.to_csv(r'C:\Users\monik\Downloads\for_cleaning_1\cleaned\cleaned_mediumminor_river.csv')


# In[ ]:





# # visualization

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\monik\Downloads\for_cleaning_1\python_cleaning\medium_minor_rivers_fl - Copy.csv')

def plot_RIVER_data(df, parameter, y_label):
    plt.figure(figsize=(30, 6))
    for RIVER in df['RIVER'].unique():
        RIVER_data = df[df['RIVER'] == RIVER]
        plt.plot(RIVER_data.index, RIVER_data[parameter], label=RIVER)
    plt.xlabel('Sample Index')
    plt.ylabel(y_label)
    plt.title(f'{y_label} Across Different Rivers')
    plt.legend()
    plt.show()
# Plotting the data
plot_RIVER_data(df, 'Minimum temperature for medium and minor rivers', 'Minimum Temperature')
plot_RIVER_data(df, 'Maximum temperature for medium and minor rivers', 'Maximum Temperature')
plot_RIVER_data(df, 'Minimum value of dissolved oxygen', 'Minimum Dissolved Oxygen')
plot_RIVER_data(df, 'Maximum value of dissolved oxygen', 'Maximum Dissolved Oxygen')
plot_RIVER_data(df, 'Minimum potential of Hydrogen value in water', 'Minimum pH')
plot_RIVER_data(df, 'Maximum potential of Hydrogen value in water', 'Maximum pH')
plot_RIVER_data(df, 'Minimum Conductivity Level', 'Minimum Conductivity')
plot_RIVER_data(df, 'Maximum Conductivity Level', 'Maximum Conductivity')
plot_RIVER_data(df, 'Minimum Biochemical oxygen demand', 'Minimum Biochemical Oxygen Demand')
plot_RIVER_data(df, 'Maximum Biochemical oxygen demand', 'Maximum Biochemical Oxygen Demand')
plot_RIVER_data(df, 'Minimum  of Nitrate N + Nitrite N required ', 'Minimum Nitrate + Nitrite')
plot_RIVER_data(df, 'Maximum  of Nitrate N + Nitrite N required ', 'Maximum Nitrate + Nitrite')
plot_RIVER_data(df, 'Minimum  of Faecal Coliforms for medium and minor rivers', 'Minimum Faecal Coliforms')
plot_RIVER_data(df, 'Maximum   of Faecal Coliforms for medium and minor rivers', 'Maximum Faecal Coliforms')
plot_RIVER_data(df, 'Minimum  of total coliform for medium and minor rivers', 'Minimum Coliform')
plot_RIVER_data(df, 'Maximum  of total coliform for medium and minor rivers', 'Maximum Coliform')


# # 3. Lakes, ponds, tanks

# In[ ]:


import pandas as pd
df3 = pd.read_csv(r'C:\Users\monik\Downloads\for_cleaning_1\lakes_ponds_tanks_cl1.csv')
print(df.head())


# In[ ]:


df3


# In[ ]:


df3.info()


# # visualizations

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\monik\Downloads\for_cleaning_1\python_cleaning\lakes_ponds_tanks_fl.csv')

def plot_waterbody_data(df, parameter, y_label):
    plt.figure(figsize=(25, 6))
    for waterbody in df['waterbody'].unique():
        waterbody_data = df[df['waterbody'] == waterbody]
        plt.plot(waterbody_data.index, waterbody_data[parameter], label=waterbody)
    plt.xlabel('Sample Index')
    plt.ylabel(y_label)
    plt.title(f'{y_label} Across Different Waterbodies')
    plt.legend()
    plt.show()
# Plotting the data
plot_waterbody_data(df, 'Minimum temperature of water', 'Minimum Temperature')
plot_waterbody_data(df, 'Maximum temperature of water', 'Maximum Temperature')
plot_waterbody_data(df, 'Minimum dissolved oxygen.', 'Minimum Dissolved Oxygen')
plot_waterbody_data(df, 'Maximum dissolved oxygen.', 'Maximum Dissolved Oxygen')
plot_waterbody_data(df, 'Minimum potential of Hydrogen(Ph) values.', 'Minimum pH')
plot_waterbody_data(df, 'Maximum potential of Hydrogen(Ph) values.', 'Maximum pH')
plot_waterbody_data(df, 'Minimum conductivity required for water quality', 'Minimum Conductivity')
plot_waterbody_data(df, 'Maximum conductivity required for water quality', 'Maximum Conductivity')
plot_waterbody_data(df, 'Minimum biochemical oxygen demand (BOD) required for water quality', 'Minimum Biochemical Oxygen Demand')
plot_waterbody_data(df, 'Maximum biochemical oxygen demand (BOD) required for water quality', 'Maximum Biochemical Oxygen Demand')
plot_waterbody_data(df, 'Minimum  of Nitrate N + Nitrite N required', 'Minimum Nitrate + Nitrite')
plot_waterbody_data(df, 'Maximum  of Nitrate N + Nitrite N required', 'Maximum Nitrate + Nitrite')
plot_waterbody_data(df, 'Minimum  of Faecal Coliforms(coliform bacteria is associated with faecal matter) .', 'Minimum Faecal Coliforms')
plot_waterbody_data(df, 'Maximum   of Faecal Coliforms(coliform bacteria is associated with faecal matter) .', 'Maximum Faecal Coliforms')
plot_waterbody_data(df, 'Minimum coliform required for different water bodies', 'Minimum Coliform')
plot_waterbody_data(df, 'Maximum coliform required for different water bodies', 'Maximum Coliform')


# In[ ]:





# # 4. Ground water

# In[ ]:


import pandas as pd
df4 = pd.read_csv(r'C:\Users\monik\Downloads\for_cleaning_1\ground_water_cl1.csv')
print(df.head())


# In[ ]:


df4


# In[ ]:


df4.info()


# # visualization

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\monik\Downloads\for_cleaning_1\python_cleaning\ground_water_fl.csv')

def plot_srcStateName_data(df, parameter, y_label):
    plt.figure(figsize=(35, 6))
    for srcStateName in df['srcStateName'].unique():
        srcStateName_data = df[df['srcStateName'] == srcStateName]
        plt.plot(srcStateName_data.index, srcStateName_data[parameter], label = srcStateName)
    plt.xlabel('Sample Index')
    plt.ylabel(y_label)
    plt.title(f'{y_label} Across Different states')
    plt.legend()
    plt.show()
# Plotting the data
plot_srcStateName_data(df, 'Minimum temperature for ground water in celsius', 'Minimum Temperature')
plot_srcStateName_data(df, 'Maximum temperature for ground water in celsius', 'Maximum Temperature')
#plot_river_data(df, 'Minimum value of dissolved oxygen', 'Minimum Dissolved Oxygen')
#plot_river_data(df, 'Maximum value of dissolved oxygen', 'Maximum Dissolved Oxygen')
plot_srcStateName_data(df, 'Minimum potential of Hydrogen value in water', 'Minimum pH')
plot_srcStateName_data(df, 'Maximum potential of Hydrogen value in water', 'Maximum pH')
plot_srcStateName_data(df, 'Minimum Conductivity Level', 'Minimum Conductivity')
plot_srcStateName_data(df, 'Maximum Conductivity Level', 'Maximum Conductivity')
plot_srcStateName_data(df, 'Minimum Biochemical oxygen demand', 'Minimum Biochemical Oxygen Demand')
plot_srcStateName_data(df, 'Maximum Biochemical oxygen demand', 'Maximum Biochemical Oxygen Demand')
plot_srcStateName_data(df, 'Minimum  of Nitrate N + Nitrite N required required for ground water', 'Minimum Nitrate + Nitrite')
plot_srcStateName_data(df, 'Maximum  of Nitrate N + Nitrite N required required for ground water', 'Maximum Nitrate + Nitrite')
plot_srcStateName_data(df, 'Minimum  of Faecal Coliforms required for ground water', 'Minimum Faecal Coliforms')
plot_srcStateName_data(df, 'Maximum   of Faecal Coliforms required for ground water', 'Maximum Faecal Coliforms')
plot_srcStateName_data(df, 'Minimum  of total coliform required for ground water', 'Minimum Coliform')
plot_srcStateName_data(df, 'Maximum  of total coliform required for ground water', 'Maximum Coliform')


# In[ ]:





# # 5. Canals, seawater, drains

# In[ ]:


import pandas as pd
df5 = pd.read_csv(r'C:\Users\monik\Downloads\for_cleaning_1\canals_seawater_drains_cl1.csv')
print(df.head())


# In[ ]:


df5


# In[ ]:


df5.info()


# In[ ]:





# # visualization

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\monik\Downloads\for_cleaning_1\python_cleaning\canals_seawater_drains_fl.csv')

def plot_waterbody_data(df, parameter, y_label):
    plt.figure(figsize=(25, 6))
    for waterbody in df['waterbody'].unique():
        waterbody_data = df[df['waterbody'] == waterbody]
        plt.plot(waterbody_data.index, waterbody_data[parameter], label = waterbody)
    plt.xlabel('Sample Index')
    plt.ylabel(y_label)
    plt.title(f'{y_label} Across Different water bodies')
    plt.legend()
    plt.show()
# Plotting the data
plot_waterbody_data(df, 'Minimum temperature of water for different water bodies', 'Minimum Temperature')
plot_waterbody_data(df, 'Maximum temperature of water for different water bodies', 'Maximum Temperature')
#plot_river_data(df, 'Minimum value of dissolved oxygen', 'Minimum Dissolved Oxygen')
#plot_river_data(df, 'Maximum value of dissolved oxygen', 'Maximum Dissolved Oxygen')
plot_waterbody_data(df, 'Minimum potential of Hydrogen(Ph) values.', 'Minimum pH')
plot_waterbody_data(df, 'Maximum potential of Hydrogen(Ph) values.', 'Maximum pH')
plot_waterbody_data(df, 'Minimum conductivity required for water quality for different water bodies', 'Minimum Conductivity')
plot_waterbody_data(df, 'Maximum conductivity required for water quality for different water bodies', 'Maximum Conductivity')
plot_waterbody_data(df, 'Minimum biochemical oxygen demand (BOD) required for water quality', 'Minimum Biochemical Oxygen Demand')
plot_waterbody_data(df, 'Maximum biochemical oxygen demand (BOD) required for water quality', 'Maximum Biochemical Oxygen Demand')
plot_waterbody_data(df, 'Minimum  of Nitrate N + Nitrite N required for different water bodies', 'Minimum Nitrate + Nitrite')
plot_waterbody_data(df, 'Maximum  of Nitrate N + Nitrite N required for different water bodies', 'Maximum Nitrate + Nitrite')
plot_waterbody_data(df, 'Minimum  of Faecal Coliforms(coliform bacteria is associated with faecal matter) .', 'Minimum Faecal Coliforms')
plot_waterbody_data(df, 'Maximum   of Faecal Coliforms(coliform bacteria is associated with faecal matter) .', 'Maximum Faecal Coliforms')
plot_waterbody_data(df, 'Minimum  of total coliform required for different water bodies', 'Minimum Coliform')
plot_waterbody_data(df, 'Maximum  of total coliform required for different water bodies', 'Maximum Coliform')


# In[ ]:





# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd

# Loading the dataset
df = pd.read_csv(r'C:\Users\monik\Downloads\canals_seawater_drains_fl.csv')

# Filter the DataFrame based on specific waterbody types
df_1 = df[(df['waterbody'] == 'STP') |
          (df['waterbody'] == 'Water Treatment Plants under NWMP') |
          (df['waterbody'] == 'WATER TREATMENT PLANT(RAW WATER)')]

# Group by 'srcStateName' and count the occurrences
df_grouped = df_1.groupby('srcStateName').size().reset_index(name='counts')

# Plot the pie chart
plt.pie(df_grouped['counts'], labels=df_grouped['srcStateName'], autopct='%1.1f%%')

# Adding title to the plot
plt.title('Water Bodies by State')

plt.show()

