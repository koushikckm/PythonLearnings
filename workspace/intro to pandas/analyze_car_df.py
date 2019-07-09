import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cardf=pd.read_csv('D:/PYTHON/mtcars.csv')
print(cardf)

cardf['hp'].plot.hist();
plt.show()

cardf['hp'].value_counts()

cardf.describe()