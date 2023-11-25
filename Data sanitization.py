import pandas as pd

table = pd.read_csv('marksheet.csv') #pandas prints the top 5 and bottom 5 rows by default in a table

print(table)

# Missing Values
missing_values = table.isna().sum()
print(f"\nMissing Values: ")
print(missing_values)

table = table.dropna()

# Duplicate rows
before_dup = len(table)
table.drop_duplicates(inplace=True)
after_dup = len(table)
dup_removed = before_dup - after_dup
print(f"\nDuplicate Rows Removed: {dup_removed}")

# Checking for data consistency ?
 

# Statistics about the cleaned dataset
print(f"\nCleaned Dataset Statistics:")
print(table.info())  #information about the cleaned dataframe