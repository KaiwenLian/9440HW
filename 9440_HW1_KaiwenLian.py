#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import pandas as pd
from io import StringIO


# ## Deliverables #1

# In[ ]:


import requests
import pandas as pd
from io import StringIO

def extract(url):
    response = requests.get(url)
    response.raise_for_status() 
    data = StringIO(response.text)
    df = pd.read_csv(data)
    return df

#Electric Vehicle Population Data
url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'

# Extract the data into pandas dataframe
df = extract(url)
print(dataframe.head())  # Display the first few rows of the dataframe


# In[14]:


import pandas as pd

# Example loading a DataFrame
# dataframe = pd.read_csv('path_to_your_csv_file.csv')

# Function to create a data dictionary
def create_data_dictionary(df):
    data_dict = pd.DataFrame(columns=['Column Name', 'Data Type', 'Sample Data'])
    for column in df.columns:
        data_dict = data_dict.append({
            'Column Name': column,
            'Data Type': df[column].dtype,
            'Sample Data': df[column].dropna().unique()[:5]  # Show up to 5 unique values
        }, ignore_index=True)
    return data_dict

# Create data dictionary
dictionary = create_data_dictionary(df)

# Export data dictionary to csv
file_name = "data_dictionary.xlsx"
dictionary.to_excel(file_name, index=False)
print(f'Data dictionary exported to {file_name}')


# In[ ]:




