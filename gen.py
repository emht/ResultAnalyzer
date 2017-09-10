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

enrollment = ["{0:03}10403615".format(i) for i in range(51)]
# for roll in range(0, 51):
# 	enrollment.append("0" + str(roll + 1) + "14802715");

# Generating the marks for all the subjects
Subjects = []
for marks in range(0, 500):
	Subjects.append(np.random.randint(35, 100));
Subjects = np.array(Subjects).reshape(10, 50);
sub = pd.DataFrame(data=Subjects[:,:],)
# sub.to_csv('Subjects.csv', index=False, encoding='utf-8')
column_names = ['Sno', 'Name', 'Enrollment No.', 'Subject1', 'Subject2', 'Subject3', 'Subject4', 'Subject5', 'Lab1', 'Lab2', 'Lab3', 'Lab4', 'Lab5']
# data = names + enrollment + Subjects

df = pd.DataFrame(
	{'Enrollment': enrollment},)
	#  data = Subjects, index="sno", columns="column_names")
print(df)

# with open(r'Subject.csv', 'a') as f:
#    writer = csv.writer(f)
#    writer.writerow(Subjects)
