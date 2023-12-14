import pandas as pd

def missing_values(table):
    """Calculates the number of missing values in each column of the file."""
    missing_values = table.isna().sum()
    return missing_values

def missing_to_zero(table): 
    """Replaces the missing values with zeros."""
    table = table.fillna(0)
    return table

def clean_columns(table):
    """Removes specific columns ('Gender','Section')"""
    table.drop('Gender', inplace=True, axis=1)
    table.drop('Section', inplace=True, axis=1)
    return table 

def remove_dup(table):
    """Removes duplicate rows and returns the number of them"""
    before_dup = len(table)
    table.drop_duplicates(inplace=True)
    after_dup = len(table)
    global dup_removed # Number of duplicates
    dup_removed = before_dup - after_dup
    return dup_removed

def to_string(table):
    """COnverts specific columns ('Name', 'Gender', 'Section') to string data type"""
    table[["Name", "Gender", "Section"]] = table[["Name", "Gender", "Section"]].astype('string')
