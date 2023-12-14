import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

table = pd.read_csv('marksheet.csv') #pandas prints the top 5 and bottom 5 rows by default in a table
subjects = ["Science", "English", "History", "Maths"] #encloses the needed columns for average grade calculation
table["mean"] = table[subjects].mean(axis = 1) #Calculates the average of grades for each student

def plot_high_low(table):
    '''This function just plots high, mid and low performers by scanning through the given pandas dataframe and then plots the corresponding average grades in a bar chart'''
    High_Performers = []
    Low_Performers = []
    Mid_Performers = []
    High_Grades = []
    Low_Grades = []
    Mid_Grades = []
    for i, j in table.iterrows():
        if j['mean']>= 85:
            High_Performers.append(j['Name'])
            High_Grades.append(j["mean"])
        if j['mean']<=40:
            Low_Performers.append(j["Name"])
            Low_Grades.append(j["mean"])
        if j['mean']>=60 and j['mean']<=85:
            Mid_Performers.append(j["Name"])
            Mid_Grades.append(j["mean"])

    fig, ax = plt.subplots(figsize = (8, 10)) #unpacks the subplot into its' axes. This is a general syntax for creating figures

    # Plot high performers in a horizontal bar chart. The first argument creates the y_values(each student)
    ax.barh(High_Performers,High_Grades, color='green', label='High Performers')

    #Likewise plot Mid performers
    ax.barh(Mid_Performers,Mid_Grades, color='yellow', label='Mid Performers')

    # Plot low performers
    ax.barh(Low_Performers, Low_Grades, color='red', label='Low Performers')

    # Customizing the plot
    ax.set_yticks(range(len(High_Grades) + len(Low_Grades)+len(Mid_Grades))) #Makes sure there are spaces for each label on the Y axis
    ax.set_xlabel('Grade Mean') #Shows the label of X axis
    ax.set_title('High, Low and Mid Performers in Class')
    plt.tight_layout() #adjusts the layout so that the names do not overlap
    ax.legend() #Shows the legend

    # Display the plot
    plt.show()
    
def plot_subjects(table):
    """Plots a bar chart comparing the performance based on the subjects. Takes the dataframe as an argument."""
    fig, ax = plt.subplots()
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
    '''This function collects all the ages into a list to plot those in a scatter plot'''
    def age_calc(birthdate):
        '''This function calculates the exact age of a person based on whether it has passed or not. It implements the "datetime" module and returns the exact age.'''
        today = datetime.today()
        birthdate = datetime.strptime(birthdate, '%m/%d/%Y') #this is a standard syntax for "unpacking" the string input into a year- month - day datetime format
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
            months = 12 - (birthdate.month - today.month) - 1
            days = 30 - (birthdate.day - today.day)
        else:
            months = today.month - birthdate.month
            days = today.day - birthdate.day

        # Calculate the exact age
        age += months / 12 + days / 365
        return age
    
    

    Ages = []
    for i, j in table.iterrows():
        Ages.append(age_calc(j["Date of Birth"]))
    #This part is for the creation of the line of best fit for the scatter plot
    coefficients = np.polyfit(Ages, table['mean'], 1)
    poly_fit = np.poly1d(coefficients)
    y_fit = poly_fit(Ages)

    plt.scatter(Ages, table['mean'], label='Data Points')
    plt.plot(Ages, y_fit, label='Line of Best Fit', color='red')
    


    # Adds labels and title
    plt.xlabel('Ages of the students')
    plt.ylabel('Means of the students')
    plt.title('The correlation between performance and age')

    # Adds a legend
    plt.legend()

    # Shows the plot
    plt.show()
    
# plot_high_low(table)
# plot_sections(table)
# plot_subjects(table)
# plot_gender(table)
# plot_age_performance(table)
