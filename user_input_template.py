# User Input Template
"""The following code represents a template that can be used to show 5 rows
at a time of a data file.  In the case of an Excel file 'list1.xlsx' can be replaced
with the appropriate filename.  For working with .csv files the method 
read_excel(<filename>) can be replaced with the method read_csv(<filename>)"""

import pandas as pd

df = pd.read_excel('list1.xlsx')

view_data = input('Would you like to see the first 5 rows?\n')
view_data = view_data.lower()
while view_data not in ['yes', 'no']:
    view_data = input('Please input "yes" or "no"')
    view_data = view_data.lower()
while view_data == 'yes':
    print(df.head())
    initial_row = 0
    fifth_row = 5
    view_data = input('Would you like to see another 5 rows of data?\n')
    view_data = view_data.lower()
    # note that after a 'yes' answer is provided to show the first 5 rows, any
    # answer other than 'yes' after the first display of 5 rows will exit out
    while view_data == 'yes':
        initial_row += 5
        fifth_row += 5
        print(df.iloc[initial_row:fifth_row])
        view_data = input('Would you like to see another 5 rows of data?\n')
        view_data = view_data.lower()
    else:
        print('\n')
