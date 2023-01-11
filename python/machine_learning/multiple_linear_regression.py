# y=b0+b1x1+b2x2+b3x3+e


#         P-VALUE
# H0=null hypothesis = boş hipotez
# H1=alternatif hipotez
# p-degeri= olasılık degeri (genelde 0.05 alınır)
# p-degeri kücüldükce H0 hatalı olma ihtimali artar
# p-degeri büyüdükce H1 hatalı olma ihtimali artar

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv('veriler.csv')
Yas=veriler.iloc[:,1:4].values

#encoder:Cinsiyeti sayıya dönüştürme 
c=veriler.iloc[:,-1:].values
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
c[:,-1]=le.fit_transform(veriler.iloc[:,-1])
ohe=preprocessing.OneHotEncoder()
c=ohe.fit_transform(c).toarray()

#encoder:Ulkeleri sayıya dönüştürme
ulke=veriler.iloc[:,0:1].values
ulke[:,0]=le.fit_transform(veriler.iloc[:,0])
ohe=preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray()

#numpy dizilerini dataFrame dönüsümü
sonuc=pd.DataFrame(data=ulke,index=range(22),columns=['fr','tr','us'])
sonuc2=pd.DataFrame(data=Yas,index=range(22),columns=['boy','kilo','yas'])
sonuc3=pd.DataFrame(data=c[:,:1],index=range(22),columns=['cinsiyet'])

#dataframe birleştirme işlemi
s=pd.concat([sonuc,sonuc2],axis=1)
s2=pd.concat([s,sonuc3],axis=1)
print(s2)

#verilerin eğitim ve test icin bölünmesi
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(s,sonuc3,test_size=0.33,random_state=0)

#verilerin ölçeklendirilmesi
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)

#boy tahmini için
boy=s2.iloc[:3:4].values
solkolon=s2.iloc[:,:3]
sagkolon=s2.iloc[:,4:]
veri=pd.concat([solkolon,sagkolon],axis=1)
a_train,a_test,b_train,b_test=train_test_split(veri,boy,test_size=0.33,random_state=0)
lr.fit(a_train,b_train)
b_pred=lr.predict(a_test)

import statsmodels.api as sm
X=np.append(arr=np.ones((22,1)).astype(int),values=veri,axis=1)
X_L=veri.iloc[:,[0,1,2,3,4,5]].values
X_L=np.array(X_L,dtype=float)
model=sm.OLS(boy,X_L).fit()
print(model.summary())