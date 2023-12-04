import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

table = pd.read_csv('marksheet.csv')
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

