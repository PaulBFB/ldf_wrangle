#!/usr/bin/env python3
import os


directory = '/home/paul/PycharmProjects/ldf_wrangle/'
to_delete = list(filter(lambda x: x.startswith('auto_output'), os.listdir(directory)))
choice = input('delete all auto_output files? YES/n: ')

if choice == 'YES':
    [os.remove(directory + i) for i in to_delete]
else:
    pass
