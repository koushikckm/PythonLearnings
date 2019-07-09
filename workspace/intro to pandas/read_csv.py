import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('D:/PYTHON/sample.csv')
print(df)
print('************************************************************************************')
df['B1']=df['B'].apply(lambda x : 'Male' if x=='m' else 'Female')
print(df)
print('************************************************************************************')
df['D']=pd.to_datetime(df['D'])
print(df)
print('************************************************************************************')
mynewdf=pd.to_datetime(df['D'])
print(mynewdf)
print('************************************************************************************')
df['D']=df['D'].dt.strftime('%Y/%B/%d')
print(df)