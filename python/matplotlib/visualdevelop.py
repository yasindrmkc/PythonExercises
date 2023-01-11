import numpy as np
import matplotlib.pyplot as plt

nparray=np.linspace(0,10,20)
nparray2=nparray ** 3
figure1=plt.figure(dpi=100)
axes1=figure1.add_axes([0.1,0.1,0.9,0.9])
axes1.plot(nparray,nparray**2,label="nparray ** 2")
axes1.plot(nparray,nparray2,label="nparray ** 3")
axes1.legend(loc=6)
plt.show()
figure1.savefig("figuredeneme.png",dpi=200)