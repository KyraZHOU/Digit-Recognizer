import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from time import time

from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier 

def importSplit():
    ''' Import train and test datasets, 
    then split train dataset into feature columns and label column'''
    train_data = pd.read_csv('train.csv')
    test_data = pd.read_csv('test.csv')
    
    train_features = train_data.values[0:,1:]
    train_labels = train_data.values[0:,0]
    test_data = test_data.values[0:,0:]
    return train_features, train_labels, test_data

def minMaxData(train_features,test_data):
	train_features = MinMaxScaler().fit_transform(train_features)
	test_data = MinMaxScaler().fit_transform(test_data)
	return train_features,test_data
	
def dRPCA(x_train, x_test, n_components):
    trainData = np.array(x_train)
    testData = np.array(x_test)
    
    pca = PCA(n_components=n_components, whiten=False)
    pca.fit(trainData)  # Fit the model with X
    pcaTrainData = pca.transform(trainData) # Transform X
    pcaTestData = pca.transform(testData) # Transform X

    return pcaTrainData, pcaTestData

def dR_KNN():
	# Record start time
	startTime = time()
	# Load data
	train_features,train_labels, test_data = importSplit()
	# Record finished time
	finishedTime = datetime.datetime.now()
	usedTime = finishedTime - startTime
	print("KNN load data finished, total loading time used:",usedTime)

	# Dimensionality reduction
	train_features, test_data = dRPCA(train_features, test_data, 0.8)

	# KNN Modelling
	knnModel = KNeighborsClassifier() # default: k=5
	knnModel.fit(train_features,np.ravel(train_labels))
	knnModel.predict(test_data)





