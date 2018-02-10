import pandas as pd


def check_q1(ans):
    expected = pd.DataFrame({'Product A': [30], 'Product B': [21]})
    return ans.equals(expected)


def answer_q1():
    print("""pd.DataFrame({'Product A': [30], 'Product B': [21]})""")


def check_q2(ans):
    expected = pd.DataFrame(
        {'Product A': [30, 35, 41], 'Product B': [21, 34, 11], 'Product C': [9, 1, 11]},
        index=['2015 Sales', '2016 Sales', '2017 Sales']
    )
    return ans.equals(expected)


def answer_q2():
    print("""pd.DataFrame({'Product A': [30, 35, 41], 'Product B': [21, 34, 11], 'Product C': [9, 1, 11]},
index=['2015 Sales', '2016 Sales', '2017 Sales'])""")


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


def check_q6(ans):
    import sqlite3
    conn = sqlite3.connect("../input/pitchfork-data/database.sqlite")
    expected = pd.read_sql_query("SELECT * FROM artists", conn)
    ans.head().equals(expected.head())


def answer_q6():
    print("""import sqlite3
conn = sqlite3.connect("../input/pitchfork-data/database.sqlite")
pd.read_sql_query("SELECT * FROM artists", conn)""")
