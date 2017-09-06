import csv
import pandas as pd
import numpy as np
# Entries to be added in the file

# Entries for student table
student_table = ['S No.', 'Name', 'Enrollment No.', 'Field']

# Marks table
Marks_table = ['Enrollment No.', 'Subject1', 'Subject2', 'Subject3', 'Subject4', 'Subject5', 'Subject6', 'Lab1', 'Lab2', 'Lab3', 'Lab4', 'Lab5']

sno = [num for num in range(1,51)]
names = []
for name in range(0, 51):
    names.append('name' + str(name));
enrollment = []
for roll in range(0, 51):
	enrollment.append("0" + str(roll + 1) + "14802715");

# Generating the marks for all the subjects
Subject1 = []
for marks in range(0, 51):
	Subject1.append(np.random.randint(35, 100));



print(sno)
print(names)
print(enrollment)
print(Subject1)


#with open(r'test.csv', 'a') as f:
#    writer = csv.writer(f)
#    writer.writerow(df)
