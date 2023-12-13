import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

table = pd.read_csv('marksheet.csv') #pandas prints the top 5 and bottom 5 rows by default in a table
subjects = ["Science", "English", "History", "Maths"] #encloses the needed columns for average grade calculation
table["mean"] = table[subjects].mean(axis = 1) #Calculates the average of grades for each student

def plot_high_low(table):
    """This function plots high, mid and low performers taking the dataframe as an argument"""
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

    # Plots high performers in a horizontal bar chart. The first argument creates the y_values(each student)
    ax.barh(High_Performers,y_values(High_Performers), color='green', label='High Performers')

    #Likewise plots Mid performers
    ax.barh(Mid_Performers,y_values(Mid_Performers), color='yellow', label='Mid Performers')

    # Plots low performers
    ax.barh(Low_Performers, y_values(Low_Performers), color='red', label='Low Performers')

    # Some customization for the plot
    ax.set_yticks(range(len(y_values(High_Performers)) + len(y_values(Low_Performers))+len(y_values(Mid_Performers)))) #Makes sure there are spaces for each label on the Y axis
    ax.set_xlabel('Grade Mean') #Shows the label of X axis
    ax.set_title('High, Low and Mid Performers in Class')
    plt.tight_layout() #adjusts the layout so that the names do not overlap
    ax.legend() #Shows the legend

    # Displays the plot
    plt.show()
    
def plot_subjects(table):
    """Plots a bar chart comparing the performance based on the subjects. Takes the dataframe as an argument."""
    fig, ax = plt.subplots()
    subjects = ["Science", "English", "History", "Maths"]
    subject_means = table[['Science', 'English', 'History', 'Maths']].mean()
    plt.bar(subjects, subject_means)
    plt.title("the means of the subjects")
    plt.show()
    
def plot_sections(table):
    """Plots the performance based on the sections. Calculates the average grades for each section then plots it as a bar chart, takes the dataframe as an argument"""
    Sum_A = 0
    Sum_B = 0
    Sum_C = 0
    Count_A = 0
    Count_B = 0
    Count_C = 0
    for i, j in table.iterrows():
        count = 0
        if j['Section'] == "A":
            Count_A += 1
            Sum_A += j["mean"]
        elif j['Section'] == "B":
            Count_B += 1
            Sum_B += j["mean"]
        else:
            Count_C += 1
            Sum_C += j["mean"]

    Mean_A = Sum_A/Count_A
    Mean_B = Sum_B/Count_B
    Mean_C = Sum_C/Count_C
    Sections = ['A', 'B', 'C']
    Means = [Mean_A, Mean_B, Mean_C]
    fig, ax = plt.subplots()
    plt.bar(Sections, Means)
    plt.title("Means based on Sections")
    plt.show()
    
def plot_gender(table):
    """compares the average grade for math based on gender in a bar chart"""
    F_mean = 0
    M_mean = 0
    F_math = []
    M_math = []
    for i, j in table.iterrows():
        if j['Gender'] == "Female":
            F_math.append(j['Maths'])
        else:
            M_math.append(j["Maths"])

    F_mean = np.mean(F_math)
    M_mean = np.mean(M_math)

    Genders = ["Men", "Women"]
    Grades = [M_mean, F_mean]

    fig, ax = plt.subplots()
    plt.bar(Genders, Grades)
    plt.title("Math means based on gender")
    plt.show()
    
def plot_age_performance(table):
    """Creates a scatter plot which correlates the performance with age"""
    def age_calc(birthdate):
        """Calculates the exact age based on the birthdate"""
        today = datetime.today()
        birthdate = datetime.strptime(birthdate, '%m/%d/%Y') #this is a standard syntax for "unpacking" the string input into a month- day - year datetime format
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
    
# plot_high_low(table)
# plot_sections(table)
# plot_subjects(table)
# plot_gender(table)
# plot_age_performance(table)
