import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

table = pd.read_csv('marksheet.csv') 

fig, ax = plt.subplots()
subjects = ["Science", "English", "History", "Maths"]
subject_means = table[['Science', 'English', 'History', 'Maths']].mean()
plt.bar(subjects, subject_means)
plt.title("the means of the subjects")
plt.show()

