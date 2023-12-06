import pandas as pd
import matplotlib.pyplot as plt
from Reading_the_data import *
from Data_sanitazation import *

# Reading the data
table = read_data('marksheet.csv')
print(table)

# Removing unrelated columns
table = clean_columns(table)

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

# Plotting mean, high, low

subjects = ["Science", "English", "History", "Maths"] #encloses the needed columns for average grade calculation
table["mean"] = table[subjects].mean(axis = 1) #Calculates the average of grades for each student
High_Performers = []
Low_Performers = []
Mid_Performers = []
for i, j in table.iterrows():
    if j['mean']>= 85:
        High_Performers.append(j['Name'])
    if j['mean']<=40:
        Low_Performers.append(j["Name"])
    if j['mean']>=60 and j['mean']<=85:
        Mid_Performers.append(j["Name"])



def y_values(list):
    '''This function returns a list with the average grades of students which are passed to the function in a list'''
    y_values = []
    for index, row in table.iterrows():
        if row['Name'] in list:
            y_values.append(row["mean"])
    return(y_values)

fig, ax = plt.subplots(figsize = (8, 10)) #unpacks the subplot into its' axes. This is a general syntax for creating figures

# Plot high performers in a horizontal bar chart. The first argument creates the y_values(each student)
ax.barh(High_Performers,y_values(High_Performers), color='green', label='High Performers')

#Likewise plot Mid performers
ax.barh(Mid_Performers,y_values(Mid_Performers), color='yellow', label='Mid Performers')

# Plot low performers
ax.barh(Low_Performers, y_values(Low_Performers), color='red', label='Low Performers')

# Customizing the plot
ax.set_yticks(range(len(y_values(High_Performers)) + len(y_values(Low_Performers))+len(y_values(Mid_Performers)))) #Makes sure there are spaces for each label on the Y axis
ax.set_xlabel('Grade Mean') #Shows the label of X axis
ax.set_title('High, Low and Mid Performers in Class')
plt.tight_layout() #adjusts the layout so that the names do not overlap
ax.legend() #Shows the legend

# Display the plot
plt.show()
