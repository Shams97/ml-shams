# -*- coding: utf-8 -*-
"""
This is sleep study based on survey within US  indiviuals 
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from random import random
from random import normalvariate


"Reading the csv file "
df = pd.read_csv("/Users/shams/Downloads/archive/SleepStudyData.csv")
df[df["Breakfast"] == "Yes"].describe()
df.head()
df.corr(numeric_only=True)
df.describe()

" Normalization and converting data into numeric forms"
df["Breakfast"] = df["Breakfast"] == "Yes"
df = df.astype({"Breakfast" : np.int_})

df["PhoneReach"] = df["PhoneReach"] == "Yes"
df = df.astype({"PhoneReach" : np.int_})

df["PhoneTime"] = df["PhoneTime"] =="Yes"
df = df.astype({"PhoneTime" : np.int_})
df.head()


" Draw the plot"
x = np.arange(10)
y = np.array([round(2*i + 3*random(), 1) for i in x])
plt.plot(x,y)
plt.show()

" Draw the scatter "
plt.scatter(x, y)
plt.show()

"Display the normal variant in sleeping hours compared with age variant"

x = np.array([normalvariate(7,2) for i in range(100)])
plt.hist(df["Hours"], bins=9)
plt.show()


