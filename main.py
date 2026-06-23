import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.random.normal(0, 0.8, 1000)
y = np.random.normal(-2, 1, 1000)

plt.hist2d(x, y, bins=5, cmap='reds')
cb = plt.colorbar()
plt.show()