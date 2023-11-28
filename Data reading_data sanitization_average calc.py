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

subjects = ["Science", "English", "History", "Maths"] #encloses the needed columns for average grade calculation
table["mean"] = table[subjects].mean(axis = 1) #Calculates the average of grades for each student
High_Performers = []
Low_Performers = []
for i, j in table.iterrows():
    if j['mean']>= 85:
        High_Performers.append(j['Name'])
    if j['mean']<=40:
        Low_Performers.append(j["Name"])



print(table)
print("The high performing students: ", High_Performers)
print("The low performing students: ", Low_Performers)