# Variables
base_list = 'List_1' # this is the base list, each item in this list is checked for a match in the other
list_2 = 'List_2' # List_2 is the name of the list in the excel file
xlfile = 'DATA_IN.xlsx'

# Importing Libs
import pandas as pd
import numpy as np

# Smart Stuff
df_0 = pd.read_excel(xlfile, dtype=str)
#rename columns
df_0.rename(columns={base_list: "base_list", list_2: "list_2"}
    , inplace=True)
df = pd.DataFrame()
#create new df
df['base_list'] = df_0['base_list']
# create new columns
df['Exact Matches'] = ''
df['Words Matched'] = ''
# unique list of words in list 2
list_2_words = ' '.join([i for i in df_0['list_2']]).split()
list_2_words = list(dict.fromkeys(list_2_words))

# loop though keys
for index, row in df.iterrows():
    current_key = row['base_list']
    current_key = str(current_key)
    count = (df_0.list_2 == current_key).sum()
    row['Exact Matches']= count
    current_key_list = current_key.split(' ')
    for item in current_key_list:
        if item in list_2_words:
            row['Words Matched'] = row['Words Matched'] + '|' + item
        
# Dump Excel Sheet
df.to_excel('DATA_OUT.xlsx')
