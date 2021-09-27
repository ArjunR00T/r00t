print("importing libraries")

from statistics import mean
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("successfully imported")
df=pd.read_csv('J:/Buggy Utility  Deserved Youth(BUDY)/ML/Practice/Data/kc_house_data.csv')


x=np.array(df['price'])
y=np.array(df['sqft_living15'])

def slope_and_intercept_calc(x,y):
    m=( ((mean(x)*mean(y))-mean(x*y))/((mean(x)*mean(x))-mean(x*x)))
    b=mean(y)-m*mean(x)
    return m,b

def sqerror(y_org,y_line):
    return sum((y_line-y_org)**2)

def coe_determination(y_org,y_line):
    y_mean_line=[mean(y_org) for i in y_org]
    sq_err_reg=sqerror(y_org, y_line)
    sq_err_mean_reg=sqerror(y_org, y_mean_line)
    return 1-(sq_err_reg/sq_err_mean_reg )

 

m,b=slope_and_intercept_calc(x,y) 
#print(m,b)
reg_line=[(m*i+b) for i in x]
print(sqerror(y,reg_line))
coefficient_determination=coe_determination(y, reg_line)
print(coefficient_determination)

px=12
py=(m*px)+b
print(py)
