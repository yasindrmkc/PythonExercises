import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as ts
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from sklearn.metrics import mean_absolute_error,mean_squared_error
from tensorflow.python.keras.models import load_model
dataFrame=pd.read_excel("bisiklet_fiyatlari.xlsx")

#y=wx+b
#y-> label
#x -> feature (özellik)


y=dataFrame["Fiyat"].values
x=dataFrame[["BisikletOzellik1","BisikletOzellik2"]].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=15)
#scaling
scaler = MinMaxScaler()
scaler.fit(x_train)
scaler.fit(x_test)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)

#sequential
model=Sequential()
model.add(Dense(4,activation="relu"))  #Nöron
model.add(Dense(4,activation="relu"))  #Nöron
model.add(Dense(4,activation="relu"))  #Nöron
model.add(Dense(1))                    #Çıktı
model.compile(optimizer = "adam",loss="mse")   #Compile türü

model.fit(x_train,y_train,epochs=250)
loss=model.history.history["loss"]
sbn.lineplot(x=range(len(loss)),y=loss)
#plt.show()
trainLoss=model.evaluate(x_train,y_train,verbose=0)
testLoss=model.evaluate(x_test,y_test,verbose=0)
print(trainLoss)
print(testLoss)
testTahminleri=model.predict(x_test)
tahminDf=pd.DataFrame(y_test,columns=["Gerçek Fiyatlar"])
testTahminleri=pd.Series(testTahminleri.reshape(330,))
tahminDf=pd.concat([tahminDf,testTahminleri],axis=1)
tahminDf.columns=["Gerçek Fiyatlar","Tahmini Fiyatlar"]
sbn.scatterplot(x="Gerçek Fiyatlar",y="Tahmini Fiyatlar",data=tahminDf)
mean_squared_error(tahminDf["Gerçek Fiyatlar"],tahminDf["Tahmini Fiyatla"])
dataFrame.describe()
yeniBisikletOzellikleri=[[1760,1758]]
yeniBisikletOzellikleri=scaler.transform(yeniBisikletOzellikleri)
model.predict(yeniBisikletOzellikleri)
model.save("bisiklet_modeli.h5")
loadModel=load_model("bisiklet_modeli.h5")
load_model.predict(yeniBisikletOzellikleri)
