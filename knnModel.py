import numpy as np 
from collections import Counter
from metrics import accuracy_score

class KNeighborsClassifier():

	def __init__(self,k=5):
		self.k = k

		self._X_train = None
		self._y_train = None

	def fit(self,X_train,y_train):
		self._X_train = X_train
		self._y_train = y_train

	def predictall(self,x_predict):
		return np.array([self._predict(x) for x in x_predict])

	def _predict(self,x):
		distances = [distance(item,x) for item in self._X_train]
		nearest = np.argsort(distances)[:self.k]
		k_labels = self._y_train[nearest]

		return Counter(k_labels).most_common(1)[0][0]

	def score(self,X_test,y_test):
		y_predict = self.predictall(X_test)
		return accuracy_score(y_test,y_predict)


def knn_classify(X_train,y_train,x_predict,k=5):
	return [_predict(X_train,y_train,x,k=5) for x in x_predict]

def _predict(X_train,y_train,x,k=5):
	distances = [distance(item,x) for item in X_train]
	nearest = np.argsort(distances)[:k]
	k_labels = y_train[nearest]

	return Counter(k_labels).most_common(1)[0][0]
def distance(a,b):
	return np.sum(np.abs(a-b)**2)**(1/2)
