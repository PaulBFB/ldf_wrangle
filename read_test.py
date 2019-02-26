#!~/PycharmProjects/ldf_wrangle/venv/bin/python3
import os
import pandas as pd
from simpledbf import Dbf5
import datetime as dt
from weekday_count import weekday_count


start_date = dt.date(2018, 10, 1)
end_date = dt.date(2018, 12, 31)

prompt = input('set start/end date? y/n')



w_count = weekday_count(start_date=start_date, end_date=end_date)

set_dict = {'Base Set.dbf': [0, 1, 2, 3],
            'Comparison set 1.dbf': [0, 1, 2, 3],
            'Comparison set 2.dbf': [0, 1, 2, 3],
            'Comparison set 3.dbf': [4],
            'Comparison set 4.dbf': [4],
            'Comparison set 5.dbf': [4],
            'Comparison set 6.dbf': [5],
            'Comparison set 7.dbf': [5],
            'Comparison set 8.dbf': [5]}

files = list(filter(lambda x: x in set_dict.keys(), os.listdir()))
files.sort()

for i in set_dict.keys():
    print(i)
    dbf_file = Dbf5(i)
    set_dataframe = dbf_file.to_dataframe()
    divisor = sum([w_count.get(j) for j in set_dict.get(i)])
    set_dataframe['Original'] = set_dataframe['count'] / divisor
    print('division successfull - outputting as xslx')
    print(set_dataframe.head())
    print(type(set_dataframe))
    set_dataframe.to_excel('auto_output {}.xls'.format(i[:-4]), index=False, columns=['Id', 'Original'])
    print('success')

print('printed {n_files} successfully. exiting.'.format(n_files=len(files)))
