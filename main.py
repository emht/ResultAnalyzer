#! /usr/bin/python3
# Reading the argument from the argv_list.py file to facilitate the utility of program
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os


pd.set_option('display.float_format', lambda x: '%.0f' % x)

cse_data = pd.read_csv("CSE.csv", index_col=0)
# print(cse_data)

no_of_subjects = cse_data.iloc[0, 4:].count()
print("Number of Subjects: {0}".format(no_of_subjects))
total_marks = cse_data.iloc[:, 4:].sum(axis=1)
cse_data['Total Marks'] = total_marks

aggregate_percent = total_marks.astype(int) / no_of_subjects
cse_data['Aggregate Percent'] = aggregate_percent
print(cse_data)