import pandas as pd
import numpy as np
#1 (1 points) Write a python reads creates a dataframe from a URL that points to a CSV file
#such as the pronto data or CSVs in data.gov.
def ReadFunction(url):
    df = pd.read_csv(url)
    return df


#2(6 points) Create the function test_create_dataframe that takes as input: (a) a pandas DataFrame and 
#(b) a list of column names. The function returns True if the following conditions hold:
#The DataFrame contains only the columns that you specified as the second argument.
#The values in each column have the same python type
#There are at least 10 rows in the DataFrame.
def test_create_dataframe(DataFrame,ColumnList):
    if list(DataFrame.columns) == ColumnList:
        for col in DataFrame.columns:
            ex = type(DataFrame[col][0])
            if all(isinstance(x, ex) for x in DataFrame[col]):
                if len(DataFrame)>=10:
                    return True
                else:return False
            else: return False
    else: return False
