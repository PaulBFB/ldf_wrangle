import os
import pandas as pd
from simpledbf import Dbf5


dbf = Dbf5('Comparison set 1.dbf')
df = dbf.to_dataframe()
print(df.head())

relevant_files = list(filter(lambda x: True if x.startswith('Comparison set') else False, os.listdir('AT_LDF_Perg_Alte_Donau_Strasse_48')))
print(relevant_files)


