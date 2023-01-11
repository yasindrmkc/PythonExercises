import numpy as np
import matplotlib.pyplot as plt

yasListesi = [10,20,30,30,30,40,50,60,70,75]
kiloListesi = [20,60,80,85,86,87,70,90,95,90]

"""nparray1=np.array(yasListesi)
nparray2=np.array(kiloListesi)
plt.plot(nparray1,nparray2,"g")
plt.xlabel("Yas")
plt.ylabel("Kilo")
plt.title("Kilonun yaşa göre değişimi")
plt.show()  """

nparray3=np.linspace(0,10,20)
nparray4=nparray3 ** 3
"""plt.subplot(1,2,1)
plt.plot(nparray3,nparray4,"g")
plt.subplot(1,2,2)
plt.plot(nparray4,nparray3,"r")
plt.show()"""

figure1=plt.figure()
figureAxes=figure1.add_axes([0.2,0.2,0.9,0.9])
figureAxes.plot(nparray3,nparray4,"g")
figureAxes.set_title("Veri başlığı")
figureAxes.set_xlabel("X verileri")
figureAxes.set_ylabel("Y verileri")
plt.show()


