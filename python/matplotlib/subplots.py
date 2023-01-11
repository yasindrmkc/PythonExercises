import numpy as np
import matplotlib.pyplot as plt


nparray=np.linspace(0,10,20)
nparray2=nparray ** 3


(figure1,axes1) = plt.subplots(nrows=1,ncols=2)
for i in axes1:
    i.plot(nparray,nparray2,"b")
    i.set_xlabel("X ekseni")

plt.tight_layout()
plt.show()