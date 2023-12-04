import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

table = pd.read_csv('marksheet.csv')
subjects = ["Science", "English", "History", "Maths"]
table["mean"] = table[subjects].mean(axis = 1) #Calculates the average of grades for each student
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