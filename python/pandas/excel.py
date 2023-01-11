import numpy as np
import pandas as pd


dataFrame = pd.read_excel("maas.xlsx")
print(dataFrame)
dataFrame2=dataFrame.dropna()
dataFrame2.to_excel("yenimaas.xlsx")
