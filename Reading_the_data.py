import pandas as pd

def read_data(file):
    table = pd.read_csv(file) #pandas prints the top 5 and bottom 5 rows by default in a table

    return table