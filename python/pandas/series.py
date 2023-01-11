import numpy as np
import pandas as pd 

dict1={"Bora" : 50,"İrem" : 18,"Yasin" : 19}
print(pd.Series(dict1))
age=[50,18,19]
name=["Bora","İrem","Yasin"]
print("\n")
print(pd.Series(age,name))