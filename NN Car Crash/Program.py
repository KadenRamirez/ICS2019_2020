import sklearn
import pandas
import matplotlib.pyplot as plt
import seaborn as sns # visualization
import numpy as np
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import normalize
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV

"""
figure out the percentage of outcomes in the data
to show it's not just chance.
"""
#shows all the datasets
data=pandas.read_csv("crash.data", header = None)
# ~ print(data)

#shows a graph for all 18 variables
# ~ sns.pairplot( data=data,vars=(0,1,2,3,4,5,6,7,8,9,10,11), hue= 12)
# ~ plt.show()

#turns dataset into an array
data=np.array(data)

X=data[:,0:11] #Get the 2-18 columns.
y=data[:,12] #Get the 1st column.

#shuffles X and y
X,y=shuffle(X,y,random_state=42)
# ~ print(X[:])
x=normalize(X)

#Trains on about 100/150 of X
#Trains on about 100/150 of y
#Tests on the rest of the dataset of X
#tests on the rest of the dataset of y
trainX=X[:120]
trainy=y[:120]
testX=X[120:]
testy=y[120:]

#Builds the NN
# ~ clf = MLPClassifier(hidden_layer_sizes=[10], random_state=0, max_iter =10000)
clf = MLPClassifier(activation='identity', alpha=0.0001, batch_size='auto',
              beta_1=0.9, beta_2=0.999, early_stopping=False, epsilon=1e-08,
              hidden_layer_sizes=[5], learning_rate='constant',
              learning_rate_init=0.001, max_iter=10000, momentum=0.9,
              n_iter_no_change=10, nesterovs_momentum=True, power_t=0.5,
              random_state=0, shuffle=True, solver='adam', tol=0.0001,
              validation_fraction=0.1, verbose=False, warm_start=False)
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

"""
#GridsearchCV
parameters = {'hidden_layer_sizes':([1], [2], [3], [4], [5], [6], [7], [8], [9], [10]), 'activation':('identity', 'logistic')}
gs = GridSearchCV(clf,parameters)
gs.fit(X,y)
print(gs.best_estimator_)
# ~ print(gs.cv_results_)
"""
