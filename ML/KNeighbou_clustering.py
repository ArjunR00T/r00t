import numpy as np
from sklearn import preprocessing,neighbors
from sklearn.model_selection import train_test_split
import pandas as pd

data=pd.read_csv('breastcancerdata.txt')
data.replace('?',-9999,inplace=True)

data.drop(['id'],1,inplace=True)

x=np.matrix(data.drop(['class'],1),dtype=np.float64)
#x=x.reshape((699,1))
y=np.matrix(['class'])

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25)

clf=neighbors.KNeighborsClassifier()
clf.fit(xtrain,ytrain)
acc=clf.score(xtest,ytest)

print(acc)


