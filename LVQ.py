# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 03:38:21 2019

@author: todos
"""

import random
import math
import matplotlib.pyplot as plt


M = 7

Set1 = []
Set2 = []
Set3 = []
Set4 = []
Set5 = []

dataSet2 = []

Neurons = []

Weights = []
Clusters = []


def setCreator():
    
    appended=0
    
    for i in range(0,100):
    
        x1 = random.uniform(-0.3, 0.3)
        y1 = random.uniform(-0.3, 0.3)
        point1=[x1,y1]
        if point1 not in Set1:
            Set1.append(point1)
            dataSet2.append(point1)
            appended = appended + 1
    
        x2 = random.uniform(-1.1, -0.5)
        y2 = random.uniform(0.5, 1.1)
        point2=[x2,y2]
        if point2 not in Set2:
            Set2.append(point2)
            dataSet2.append(point2)
            appended = appended + 1
    
        x3 = random.uniform(-1.1, -0.5)
        y3 = random.uniform(-1.1, -0.5)
        point3=[x3,y3]
        if point3 not in Set3:
            Set3.append(point3)
            dataSet2.append(point3)
            appended = appended + 1
    
        x4 = random.uniform(0.5, 1.1)
        y4 = random.uniform(-1.1, -0.5)
        point4=[x4,y4]
        if point4 not in Set4:
            Set4.append(point4)
            dataSet2.append(point4)
            appended = appended + 1
    
        x5 = random.uniform(0.5, 1.1)
        y5 = random.uniform(0.5, 1.1)
        point5=[x5,y5]
        if point5 not in Set5:
            Set5.append(point5)
            dataSet2.append(point5)
            appended = appended + 1

    #print(appended)
def initialization():
    
    for i in range(0,M):
        #x = random.uniform(-1.1, 1.1)
        #y = random.uniform(-1.1, 1.1)
        rC = random.randint(0, len(dataSet2))
        x=dataSet2[rC][0]
        y=dataSet2[rC][1]
        center = [x,y]
        Weights.append(center)
        newCluster = []
        Clusters.append(newCluster)
    

def euclideanDistanceCalculator(x1,x2,y1,y2):
    

    
    xDif = x1-x2
    yDif = y1-y2
    
    sqrtXD = xDif**2
    sqrtYD = yDif**2
    
    euclideanDistance = math.sqrt(sqrtXD+sqrtYD)
    
    return euclideanDistance

def removeFromCluster(pointToRemove):
    
    for cluster in Clusters:
        for point in cluster:
            if (point[0]==pointToRemove[0]) and (point[1]==pointToRemove[1]) :
                cluster.remove(point)
                #break;
                
def performLVQ():
    
    initialization()
    
    terminationFlag = False
    
    n = 0.1
    while terminationFlag==False:
        
        for i in range(0,len(dataSet2)):
       
            minD = 100
            index =0
            
            for j in range(0,len(Weights)):
                
                current = euclideanDistanceCalculator(dataSet2[i][0],Weights[j][0],dataSet2[i][1],Weights[j][1])
                
                if current < minD:
                    
                    minD = current
                    index = j
        
            if dataSet2[i] not in Clusters[index]:
                removeFromCluster(dataSet2[i])
                Clusters[index].append(dataSet2[i])
                
        
            Weights[index][0]=Weights[index][0] + n*(dataSet2[i][0]-Weights[index][0])
            Weights[index][1]=Weights[index][1] + n*(dataSet2[i][1]-Weights[index][1])
        
        n = n*0.95
        print(n)
        
        if(n<0.005):
            terminationFlag=True
        
        #for q in range(0,M):
            #print("Cluster "+str(q)+" : "+str(len(Clusters[q])))
        #print("-------------------")

def dispersionCalculation():
    
    fSum=0
    
    for i in range(0,len(Clusters)):
        sumOfpDis=0
        for j in range(0,len(Clusters[i])):
            sumOfpDis = sumOfpDis + euclideanDistanceCalculator(Clusters[i][j][0],Weights[i][0],Clusters[i][j][1],Weights[i][1])
        fSum = fSum + sumOfpDis   
    return fSum        
    
setCreator()
performLVQ()
print(dispersionCalculation())    
    
fig1, ax1 = plt.subplots()
x_list = [l[0] for l in dataSet2]
y_list = [l[1] for l in dataSet2]
xC = [t[0] for t in Weights]
yC = [t[1] for t in Weights]


ax1.plot(x_list,y_list ,'r+',xC,yC ,'b*')    
    
    
    
    
    
    
    
    
    
    
    
    