# import pyspark as spark
# from pyspark.sql.functions import *
# import pyspark.pandas as pd
# import os
import numpy as np
import pandas as pd
import ssl; 


ssl._create_default_https_context = ssl._create_stdlib_context
column_name = ['play_id','game_id','home_team']

f_nfl = 'https://github.com/ryurko/nflscrapR-data/tree/master/play_by_play_data/regular_season/reg_pbp_2009.csv'

df = pd.read_csv(f_nfl, delimiter =',', names = column_name,)

df.head()







