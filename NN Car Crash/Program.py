import sklearn
import pandas
import matplotlib.pyplot as plt
import seaborn as sns # visualization
import numpy as np
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import normalize

#shows all the datasets
data=pandas.read_csv("crash.data", header = None)
print(data)

#shows a graph for all 18 variables
sns.pairplot( data=data,vars=(0,1,2,3,4,5,6,7,8,9,10,11), hue= 12)
plt.show()

#turns dataset into an array
data=np.array(data)

X=data[:,0:11] #Get the 2-18 columns.
y=data[:,12] #Get the 1st column.

#shuffles X and y
X,y=shuffle(X,y,random_state=42)
print(X[:])
x=normalize(X)

#Trains on about 100/150 of X
#Trains on about 100/150 of y
#Tests on the rest of the dataset of X
#tests on the rest of the dataset of y
trainX=X[:25]
trainy=y[:25]
testX=X[25:]
testy=y[25:]

#Builds the NN
clf = MLPClassifier(hidden_layer_sizes=[12,6], random_state=0, max_iter =10000)
clf.fit(trainX, trainy)
trainScore = clf.score(trainX,trainy)
testScore = clf.score(testX,testy)

#prints the predictions for testX
prediction=clf.predict(testX)
print(prediction)

#prints the accuracy of the training
print(clf.score(trainX,trainy))
print(clf.score(testX,testy))

#cross validates the results
cv_results = cross_validate(clf, X, y, cv=4)
print(cv_results)
