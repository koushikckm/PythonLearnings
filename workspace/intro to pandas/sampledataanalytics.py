import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=np.array([['','Col1','Col2'],['Row1',1,2],['Row2',3,4]])
print(data)
type(data)
df=pd.DataFrame(data=data[1:,1:],index=data[1:,0],columns=data[0,1:])
print(df)
mydf=pd.DataFrame(data=[14,15,16,17],index=range(10,14),columns=['Age'])
print(mydf)
print(df.shape)
print(len(df.index))
print(len(df.index))
print(df.iloc[1][1])
print(df.loc['Row1']['Col1'])