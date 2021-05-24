import pandas as pd


def check_q1(ans):
    expected = pd.DataFrame({'Apples': [30], 'Bananas': [21]})
    return ans.equals(expected)


def answer_q1():
    print("""pd.DataFrame({'Apples': [30], 'Bananas': [21]})""")


def check_q2(ans):
    expected = pd.DataFrame(
        {'Apples': [35, 41], 'Bananas': [21, 34]},
        index=['2017 Sales', '2018 Sales']
    )
    return ans.equals(expected)


def answer_q2():
    print("""pd.DataFrame(
    {'Apples': [35, 41], 'Bananas': [21, 34]},
    index=['2017 Sales', '2018 Sales']
)""")


def check_q3(ans):
    expected = pd.Series(['4 cups', '1 cup', '2 large', '1 can'],
                         index=['Flour', 'Milk', 'Eggs', 'Spam'],
                         name='Dinner')
    return ans.equals(expected)


def answer_q3():
    print("""pd.Series(['4 cups', '1 cup', '2 large', '1 can'], 
index=['Flour', 'Milk', 'Eggs', 'Spam'], 
name='Dinner')""")


def check_q4(ans):
    expected = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)
    return ans.head().equals(expected.head())


def answer_q4():
    print("""pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)""")


def check_q5(ans):
    expected = pd.read_excel("../input/publicassistance/xls_files_all/WICAgencies2014ytd.xls",
                             sheetname='Pregnant Women Participating')
    return ans.head().equals(expected.head())


def answer_q5():
    print("""pd.read_excel("../input/publicassistance/xls_files_all/WICAgencies2014ytd.xls", 
sheetname='Pregnant Women Participating')""")

''' I am commenting on this to point out the error.
I am getting an error in Question 5 of Lesson 1 Creating,Reading and Writing :

FileNotFoundError: [Errno 2] No such file or directory: '../input/publicassistance/xls_files_all/WICAgencies2014ytd.xls'

I wrote this answer code :
pd.read_excel("../input/publicassistance/xls_files_all/WICAgencies2014ytd.xls",
sheetname='Pregnant Women Participating')

It seems this particular dataset is missing.

Kaggle should change the user-defined function of Question 5 of Lesson 1. It must include the excel file US Public Assistance WIC PWP data in the function. CSV File can be found at :
https://www.kaggle.com/jpmiller/publicassistance/WICAgencies2014ytd/Pregnant_Women_Participating.csv

creating_reading_writing.py program of Pandas Lesson 1. The user-defined functions def check_q5(ans) and def answer_q5() must be changed. Unless we can't complete the course and figure out the solution.

def check_q5(ans):
expected = pd.read_excel("../input/publicassistance/xls_files_all/WICAgencies2014ytd.xls",
sheetname='Pregnant Women Participating')
return ans.head().equals(expected.head())

def answer_q5():
print("""pd.read_excel("../input/publicassistance/xls_files_all/WICAgencies2014ytd.xls",
sheetname='Pregnant Women Participating')""")

This file (../input/publicassistance/xls_files_all/WICAgencies2014ytd.xls) is not present in the directory. I think Kaggle must have updated the dataset of US Public Assistance WIC.

Program Path : /opt/conda/lib/python3.6/site-packages/learntools/advanced_pandas/creating_reading_writing.py
'''
''' If Kaggle removed xls files then it can make changes i following locations(I guess) :

/opt/conda/lib/python3.6/site-packages/learntools/advanced_pandas/creating_reading_writing.py

and

/kaggle/input/advanced-pandas-exercises/creating_reading_writing.py

creating_reading_writing.py (on both locations) can be replaced with what I made if Kaggle consider .csv file location for question 5. The markdown of question 5 must also be changed.

My file : https://github.com/deetrojan/Python-Data_Science/blob/main/creating_reading_writing.py

'''
    
    
def check_q6(ans=""):
    import os
    expected = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
    return os.path.exists("cows_and_goats.csv") and pd.read_csv("cows_and_goats.csv", index_col=0).equals(expected)


def answer_q6():
    print("""q6_df.to_csv("cows_and_goats.csv")""")


def check_q7(ans):
    import sqlite3
    conn = sqlite3.connect("../input/pitchfork-data/database.sqlite")
    expected = pd.read_sql_query("SELECT * FROM artists", conn)
    return ans.head().equals(expected.head())


def answer_q7():
    print("""import sqlite3
conn = sqlite3.connect("../input/pitchfork-data/database.sqlite")
pd.read_sql_query("SELECT * FROM artists", conn)""")
