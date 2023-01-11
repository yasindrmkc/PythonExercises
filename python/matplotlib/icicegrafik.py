import numpy as np
import matplotlib.pyplot as plt

nparray=np.linspace(0,10,20)
nparray2=nparray ** 3
figure1=plt.figure()
axes1=figure1.add_axes([0.1,0.1,0.7,0.7])
axes2=figure1.add_axes([0.2,0.4,0.3,0.3])
axes1.plot(nparray,nparray2,"g")
axes1.set_title("Ana Grafik")
axes1.set_xlabel("X Ekseni")
axes1.set_ylabel("Y Ekseni")

axes2.plot(nparray2,nparray,"r")
axes2.set_title("Küçük Grafik")
axes2.set_ylabel("Y Ekseni")
axes2.set_xlabel("X Ekseni")
plt.show()
