import sklearn
import pandas
import matplotlib.pyplot as plt
import seaborn as sns # visualization
import numpy as np
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import normalize


#shows the 150 datasets
data=pandas.read_csv("iris.data", header=None)
print(data)

"""
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica

#4 answers: The Iris Setosa is easily identifyable as it's usually separate from
from the other two on the graphs. The Iris versicoulour and Iris Vigrinica are harder
to identify as they overlap in almost every area.
"""

#shows the graphs for Iris Setosa, Iris Versicolour, Iris Virginica
sns.pairplot( data=data,vars=(0,1,2,3), hue=4 )
plt.show()

#turns dataset into an array
data=np.array(data)

#defines variables X and y as part of the array
X=data[:,0:4] #This gets all the rows and only the first 4 columns.
y=data[:,4] #This gets all the rows and the 5th column.
# ~ print(X.shape) #(150,4)
# ~ print(y.shape) #(150,1)

#shuffles X and y
X,y=shuffle(X,y,random_state=0)
print(X[:])
x=normalize(X)
print(X[:4])

"""
#8 answers: if you print the dataset it before the shuffle it is different then
after so therefore it has been shuffled. This is useful for testing multiple of the
same dataset in a random way.
"""

#Trains on about 100/150 of X
#Trains on about 100/150 of y
#Tests on the rest of the dataset of X
#tests on the rest of the dataset of y
trainX=X[:100]
trainy=y[:100]
testX=X[100:151]
testy=y[100:151]

#builds the NN
# ~ for layerSize in range(1,12):
clf = MLPClassifier(hidden_layer_sizes=[2,2], random_state=42, max_iter =1336)
clf.fit(trainX, trainy)
trainScore = clf.score(trainX,trainy)
testScore = clf.score(testX,testy)
# ~ print("%d, %f, %f"%(layerSize,trainScore,testScore))
# ~ print(dir(clf))

#prints how our nodes are wieghted
print(clf.coefs_)
print(clf.intercepts_)

#prints the predictions for testX
prediction=clf.predict(testX)
print(prediction)

#prints the accuracy of the training
print(clf.score(trainX,trainy))
print(clf.score(testX,testy))

# #13 answer: These numbers show the success rates in divding the number of flowers into groups

#cross validates the results
cv_results = cross_validate(clf, X, y, cv=4)
print(cv_results)
