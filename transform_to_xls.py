#!~/PycharmProjects/ldf_wrangle/venv/bin/python3
import os
import pandas as pd
from simpledbf import Dbf5
import datetime as dt
from weekday_count import weekday_count


start_date = dt.date(2018, 10, 1)
end_date = dt.date(2018, 12, 31)

prompt = 'X'

while prompt not in ['y', 'Y', 'n', 'N']:
    print('default dates currently set to from:{start} to:{end}'.format(start=start_date, end=end_date))
    prompt = input('change start/end date? y/n: ')

if prompt=='y' or prompt=='Y':
    start_date_year = int(input('enter start date year (INTEGER)'))
    start_date_month = int(input('enter start date month (INTEGER)'))
    start_date_day = int(input('enter start date day (INTEGER)'))
    start_date = dt.date(year=start_date_year, month=start_date_month, day=start_date_day)
    end_date_year = int(input('enter end date year (INTEGER)'))
    end_date_month = int(input('enter end date month (INTEGER)'))
    end_date_day = int(input('enter end date day (INTEGER)'))
    end_date = dt.date(year=end_date_year, month=end_date_month, day=end_date_day)

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
    dbf_file = Dbf5(i)
    set_dataframe = dbf_file.to_dataframe()
    divisor = sum([w_count.get(j) for j in set_dict.get(i)])
    set_dataframe['Original'] = set_dataframe['count'] / divisor
    set_dataframe.to_excel('auto_output - {sourcefile} - {start} - to - {end}.xls'.format(sourcefile=i[:-4],
                                                                                          start=str(start_date),
                                                                                          end=str(end_date)),
                           index=False,
                           columns=['Id', 'Original'])

print('printed {n_files} successfully. exiting.'.format(n_files=len(files)))
