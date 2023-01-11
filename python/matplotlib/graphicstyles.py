import numpy as np
import matplotlib.pyplot as plt

nparray1=np.linspace(0,10,20)
nparray2=nparray1 ** 2

##SCATTER
"""plt.scatter(nparray1,nparray2)
plt.show()"""

#HİSTOGRAM
"""nparray3=np.random.randint(0,100,50)
plt.hist(nparray3)
plt.show()"""

#BOXPLOT
plt.boxplot(nparray1)
plt.show()
