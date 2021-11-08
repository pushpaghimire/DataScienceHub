import sys
import os
import pandas as pd
import ssl
from tabulate import tabulate_formats
# display(df_consigne_errors)

pd.set_option('display.max_columns', 30)
# print(pd.get_option('display.max_columns'))
pd.set_option('expand_frame_repr', True)

ssl._create_default_https_context = ssl._create_unverified_context


file_root_path = 'https://raw.githubusercontent.com/researchdatascience/DataScienceHub/main/'

deliveries = pd.read_csv(file_root_path + 'deliveries.csv')
matches = pd.read_csv(file_root_path +  'matches.csv')

print(deliveries.head())

matches