import numpy as np
import matplotlib.pyplot as plt

nparray1=np.linspace(0,10,20)
nparray2=nparray1 ** 2
(figure1,axes1) = plt.subplots()
axes1.plot(nparray1,nparray2,color="#3A95A8",alpha=0.5,linewidth=5.0,linestyle="-.",marker="o",markersize=4,markerfacecolor="red")
plt.show()

