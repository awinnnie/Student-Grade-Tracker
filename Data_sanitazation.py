import pandas as pd

def missing_values(table):
    missing_values = table.isna().sum()
    return missing_values

def missing_to_zero(table)  : 
    table = table.fillna(0)
    return table

def clean_columns(table):
    table.drop('Gender', inplace=True, axis=1)
    table.drop('Section', inplace=True, axis=1)
    return table 

def remove_dup(table):
    before_dup = len(table)
    table.drop_duplicates(inplace=True)
    after_dup = len(table)
    global dup_removed # Number of duplicates
    dup_removed = before_dup - after_dup
    return dup_removed