import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

data_dict = {-1:np.array([[1,7],
                          [2,8],
                          [3,8],]),
             
             1:np.array([[5,1],
                         [6,-1],
                         [7,3],])
             }


class SVM:
    def  __init__(self,graph=True):
        self.graph=graph
        self.color={1:'g',-1:'r'}
        if self.graph:
            self.fig=plt.figure()
            self.axis=self.fig.add_subplot(1,1,1)

    def train(self,data):
        self.data=data
        #opt_dict wwill store all values of w and b and later we can
        #choose the lowest and largest  value among them.
        #minimize w and maximize b---> thats our optimimzation goal
        # dictionary will be in the form {||w||:[w,b]}
        opt_dict={}
        #transfrom to try all possible values
        transform=[[1,1],
                    [1,-1],
                    [-1,1],
                    [-1,-1]]

        all_data=[]
        for yi in self.data:
            for featureset in self.data[yi]:
                for features in featureset:
                    all_data.append(features)
        #all_data=[1, 7, 2, 8, 3, 8, 5, 1, 6, -1, 7, 3]
        #after execution
        self.maxFeatureValue=max(all_data)
        self.minFeatureValue=min(all_data)
        all_data=None
       
        stepSizes=[self.maxFeatureValue*0.1,
                    self.maxFeatureValue*0.01,
                    self.maxFeatureValue*0.001
                   ]

        bRangeMultiple=5
        bMultiple=5
        #Bruteforcing all values of w, from a given range in 
        #this case from -80 to 80
        #to find optimal value
        latestOptimum = self.maxFeatureValue*10
        # Stepping process starts from Here:
        for steps in stepSizes:
            #initalizing a list of 80 x 80
            w=np.array([latestOptimum,latestOptimum])
            optimized=False
            ############################################################
            ## First ,we take random w and b values in this case(w)   ## 
            ## 80x80 and we take all possible combintion like[80,80]  ##
            ## [-80,80],[80,-80] and a specific b value range calcted ##
            ## using np.arange and we bruteforce over all  value      ##
            ## of b for specific w eg:[80,-80] with input data and    ##
            ## check if the yi[x.w+b] is -ve value,if yes we add that ##
            ## w and b to a dictionary which can be later used to     ##
            ## take the smallest value among them after checking for  ##
            ## all possible value of w and b,we update w as w=w-steps ##
            ## and we continue the process for all value of new w and ##
            ## b,until the w value reaches a specific small value in  ##
            ## this case less than 0.After we have all the value of w ##
            ## and b which satify this eq yi[x.w+b] to be negative we ##
            ## find the smallest values among them and thats the      ##
            ## optimum value of w and b which we can later use to make##
            ## new prediction(NOTE:We are only taking value of w till ##
            ## than zero is because the  value of w does not depend on##
            ## sign so the same value gets repeted again and again)   ##
            ############################################################
            while not optimized:

                #np.arage is advance range and has more feature
                #than python range
                for b in np.arange(-1*(self.maxFeatureValue*bRangeMultiple),
                    self.maxFeatureValue*bRangeMultiple,steps*bMultiple):
                    for trans in transform:                           
                        w_t=w*trans                                     
                        found = True                                    
                        for i in self.data:                             
                            for xi in self.data[i]:
                                yi=i
                                if not yi*(np.dot(w_t,xi)+b)>=1:
                                    found=False
                        if found:
                            #finding magnitude of vector
                            opt_dict[np.linalg.norm(w_t)]=[w_t,b]
                if w[0]<0:
                    optimized=True
                    print('Optimzed a Step')
                else:  
                    w=w-steps
                    


    def predict(self,features):
        #sign=x.w+b
        #goal is to find w and b so that we can make prediction
        #sign=y sub i
        #sign can implemented with numpy with np.sign method
        classification=np.sign(np.dot(np.array(features),self.w)+self.b)
        return classification

sv=SVM()
sv.train(data=data_dict)


