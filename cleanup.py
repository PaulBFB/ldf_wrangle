#!/usr/bin/env python3
import os


to_delete = list(filter(lambda x: x.startswith('auto_output'), os.listdir()))
choice = input('delete all auto_output files? YES/n: ')

if choice == 'YES':
    [os.remove(i) for i in to_delete]
else:
    pass
