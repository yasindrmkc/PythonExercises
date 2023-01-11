import numpy as np
import pandas as pd

dict1={"İstanbul" : [30,29,np.nan],"Ankara" : [20,np.nan,25],"İzmir" : [40,39,38]}
weatherDataFrame=pd.DataFrame(dict1)
print(weatherDataFrame)
print("\n")
print(weatherDataFrame.dropna())
print("\n")
print(weatherDataFrame.dropna(axis= 1))
dict2={"İstanbul" : [30,29,np.nan],"Ankara" : [20,np.nan,25],"İzmir" : [40,39,38],"Antalya " : [45,np.nan,np.nan]}
newWeatherDataFrame=pd.DataFrame(dict2)
print(newWeatherDataFrame)
print(newWeatherDataFrame.dropna(axis=1,thresh=2)) #thresh na sayısı 2 olanları almıcak tek olanları alıcak
print(newWeatherDataFrame.fillna(20)) #nan olanları 20 ile doldurucak