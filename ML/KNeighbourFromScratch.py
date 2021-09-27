from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import warnings
from collections import Counter
import pandas as pd
plot1=[1,3]
plot2=[2,5]

#data1={'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}
#newFeatures=[1,2]

'''
for i in data:
    for ii in data[i]:
        plt.scatter(ii[0],ii[1],s=100)
        plt.show()
'''
def kNeighbour(data,predict,k=4):
    if len(data)>=k:
        warnings.warn('k value should be less than len(data).....ShitHead!')
    distance=[]
    for group in data:
        for features in data[group]:
            #euclidean_distance=sqrt((features[0]-predict[0]**2)+(featres[1]-predict[1]**2)
            #euclidean_distance=np.sqrt(np.sum(np.array(features)-np.array(predictions)**2)
            ed=np.linalg.norm(np.array(features)-np.array(predict))
            distance.append([ed,group])

    #print(sorted(distance))
    votes=[i[1] for i in sorted(distance)[:k]]
    #print(votes)
    voteresult=Counter(votes).most_common(1)[0][0]
    #print(vote)
    confidence=Counter(votes).most_common(1)[0][1]/k
    
    return voteresult,confidence





df=pd.read_csv('J:/Buggy Utility  Deserved Youth(BUDY)/ML/Course/Data/breastcancerdata.txt')
df.replace('?',-9999,inplace=True)
df.drop(['id'],1,inplace=True)
data=df.astype(float).values.tolist()

size=0.2
train_set={2:[],4:[]}
test_set={2:[],4:[]}

x=data[:-int(size*len(data))]
y=data[-int(size*len(data)):]
#print(y)
for i in x:
    train_set[i[-1]].append(i[:-1])
    
for i in y:
    test_set[i[-1]].append(i[:-1])

#print(train_set)
c=0
t=0
o=[4, 8, 8, 5, 4, 5, 10, 4, 1]
for group in test_set:
    for i in test_set[group]:
        result,conf=kNeighbour(data=train_set, predict=i,k=4)
        if result==group:
            c+=1
        

        t+=1

print(c/t*100,"----->acc")
print(conf,"------>conf")
print(result,"------->Prediction")
        

