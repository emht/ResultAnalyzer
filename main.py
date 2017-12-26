#! /usr/bin/python3
# Reading the argument from the argv_list.py file to facilitate the utility of program
"""
Usage: ./main.py [Roll no] [roll no]
       ./main.py --compare [roll no1] [roll no2]
       ./main.py --[mean/mini/maxi/all] [roll no]
       ./main.py --bar [roll no]
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# to suppress the descriptive text by pandas dataframe
pd.Series.__unicode__ = pd.Series.to_string

def valid_arguments():
    if len(sys.argv) <= 1:
        print("Please provide correct number of arguments: ");
        print("Usage: ./main.py [Roll no.]");
        return False;
    elif sys.argv[1] == '--compare':
        global enrollment1, enrollment2, compare
        compare = True
        enrollment1 = sys.argv[2];
        enrollment2 = sys.argv[3];
        return True;
    elif sys.argv[1] in ['--mini', '--maxi', '--mean']:
        global mini, maxi, mean
        mini, maxi, mean = None
        if sys.argv[1] == '--mini':
            mini = True
        elif sys.argv[1] == '--mean':
            mean = True
        elif sys.argv[1] == '--maxi':
            maxi = True
    else:
        enrollment1 = sys.argv[1]
        return True;

if __name__ == '__main__':
    if valid_arguments():
        cse_result = pd.read_csv("CSE.csv", index_col=0);
        ece_result = pd.read_csv("ECE.csv", index_col=0);
        eee_result = pd.read_csv("EEE.csv", index_col=0);
        it_result = pd.read_csv("IT.csv", index_col=0);
        mae_result = pd.read_csv("MAE.csv", index_col=0);

        Subjects = ['sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'lab1', 'lab2', 'lab3', 'lab4', 'lab5']
        num_subjects = len(Subjects);

        if (int(enrollment1) in list(cse_result["Enrollment No."])) :
            result1 = cse_result[cse_result['Enrollment No.'] == int(enrollment1)]
        elif (int(enrollment1) in list(ece_result["Enrollment No."])) :
            result1 = ece_result[ece_result['Enrollment No.'] == int(enrollment1)]
        elif (int(enrollment1) in list(eee_result["Enrollment No."])):
            result1 = eee_result[eee_result['Enrollment No.'] == int(enrollment1)]
        elif (int(enrollment1) in list(it_result["Enrollment No."])):
            result1 = it_result[it_result['Enrollment No.'] == int(enrollment1)]
        elif (int(enrollment1) in list(mae_result["Enrollment No."])):
            result1 = mae_result[mae_result['Enrollment No.'] == int(enrollment1)]
        else :
            print("Student entry does not exist");
            exit(1);

        marks_std1 = result1.ix[:, 3:]
        total_marks1 = marks_std1.values.sum()
        aggregate_percent1 = float(total_marks1) / num_subjects;
        marks_std1.apply(tuple, axis=0)
        print(marks_std1)
        print("Total Marks scored: %s\n" % (total_marks1));
        print("Aggregate Percentage: %s" % (aggregate_percent1));

        result1 = cse_result.loc[49][3:];
        marks_std1 = list(result1.values)

        # For second student when compared
        result2 = cse_result.loc[48][3:];
        marks_std2 = list(result2.values)

        Name_std2 = cse_result.loc[48][0];
        Branch_std2 = cse_result.loc[48][1];
        print("Enrollment No. : %s\t Name: %s\t Branch: %s\n" % (enrollment1, Name_std2, Branch_std2));
        print(result2)
        print("\nTotal Marks: %s" % (result2.sum()));


        n_groups = 10
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        Student1 = plt.bar(index, marks_std1, bar_width, alpha=opacity, color='b', label="Student1")
        Student2 = plt.bar(index+bar_width, marks_std2, bar_width, alpha=opacity, color='g', label='Student2')
        plt.bar(index, marks_std1, bar_width)
        plt.xlabel('Subjects')
        plt.ylabel('Marks')
        plt.title('Performance chart of a student')
        # plt.xticks(index, Subjects)
        plt.legend()
        plt.tight_layout()
        plt.show()

        # Name_std1 = cse_result.loc[49][0];
        # Branch_std1 = cse_result.loc[49][1];
        # print("Enrollment No. : %s\t Name: %s\t Branch: %s\n" % (enrollment1, Name_std1, Branch_std1));
        # print(result1)
        # print("\nTotal Marks: %s" %(result1.sum()));
        # marks_std1 = list(result1.values)

