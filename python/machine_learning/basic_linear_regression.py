#y=ax+b

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




veriler=pd.read_csv('satislar.csv')
aylar=veriler[['Aylar']]
satislar=veriler[['Satislar']]
satislar2=veriler.iloc[:,:1].values

#verilerin eğitim ve test  için bölünmesi 
from  sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(aylar,satislar,test_size=0.33,random_state=0)

#verilen ölçeklenmesi
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)
Y_train=sc.fit_transform(y_train)
Y_test=sc.fit_transform(y_test)

#model inşası(linear regression)
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)
tahmin=lr.predict(x_test)

x_train=x_train.sort_index()
y_train=y_train.sort_index()        #içindeki verileri sıralı bir şekilde sıralar

plt.title("Aylara göre satis")
plt.xlable("Aylar")
plt.ylable("Satislar")
plt.plot(x_train,y_train)
plt.plot(x_test,lr.predict(x_test))
plt.show()
