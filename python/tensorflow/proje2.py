import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

dataFrame=pd.read_excel("merc.xlsx")
plt.figure(figsize=(7,5))
sbn.displot(dataFrame["price"])
sbn.countplot(dataFrame["year"])
plt.show()
dataFrame.corr()
dataFrame.corr()["price"].sort_values()
dataFrame.corr()["year"].sort_values() 