import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("D:\HỌC\Hoc_PYTHON\Python_Pandas\Fintech\Bank_Personal_Loan_Modelling.xlsx", 1)
print(df.head(5))

#print(df.shape)
#print(df.info())
#or
#print(df.isnull().sum())
print(df.columns)
#Xóa cột id vs zipcode
print(df.drop(['ID', 'ZIP Code'], axis = 1, inplace = True))
print(df.columns)

import plotly.express as ps
fig = ps.box(df, y = ['Age', 'Experience', 'Income', 'Family', 'Education'])
fig.show()
#Tìm độ lẹch của dữ liệu trên trục chỉ mục cột
print(df.skew())

#Dựng bđ cột 
df.hist(figsize = (20, 20))
plt.show()


