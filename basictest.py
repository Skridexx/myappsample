import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web


x = np.linspace(0,100,11)
y = x**2


plt.plot(x,y)
plt.show()
print('This was added!')