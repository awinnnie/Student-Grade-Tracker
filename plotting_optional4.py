import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

table = pd.read_csv('marksheet.csv')

subjects = ["Science", "English", "History", "Maths"] #encloses the needed columns for average grade calculation
table["mean"] = table[subjects].mean(axis = 1) #Calculates the average of grades for each student

def age_calc(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, '%m/%d/%Y') #this is a standard syntax for "unpacking" the string input into a year- month - day datetime format
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

Ages = []
for i, j in table.iterrows():
    Ages.append(age_calc(j["Date of Birth"]))

plt.scatter(Ages, table['mean'], label='Data Points')

# Add labels and title
plt.xlabel('Ages of the students')
plt.ylabel('Means of the students')
plt.title('The correlation between performance and age')

# Add a legend
plt.legend()

# Show the plot
plt.show()