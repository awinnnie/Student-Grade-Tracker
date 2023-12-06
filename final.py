from Reading_the_data import *
from Data_sanitazation import *
from plotting import *

# Reading the data
table = read_data('marksheet.csv')
print(table)

# # Removing unrelated columns
# table = clean_columns(table)

# Missing values
miss_val = missing_values(table)
print(f"\nMissing Values: ")
print(miss_val)

table = missing_to_zero(table) # changes missing values to zero
miss_val_new = missing_values(table)
print(f"\nUpdated missing Values: ")
print(miss_val_new)

# Removing duplicate rows
dup_removed = remove_dup(table)
print(f"\nDuplicate Rows Removed: {dup_removed}")

# Statistics about the cleaned dataset
print(f"\nCleaned Dataset Statistics:")
print(table.info())  #information about the cleaned dataframe

subjects = ["Science", "English", "History", "Maths"] #encloses the needed columns for average grade calculation
table["mean"] = table[subjects].mean(axis = 1) #Calculates the average of grades for each student

# Plotting high, low, mid performances
plot_high_low(table)

# Plotting based on sections
plot_sections(table)

# Plotting based on subjects
plot_subjects(table)

# Plotting based on gender
plot_gender(table)

# Plotting based on age
plot_age_performance(table)
