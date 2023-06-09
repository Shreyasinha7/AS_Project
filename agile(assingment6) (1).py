# -*- coding: utf-8 -*-
"""AGILE(assingment6).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R6M7ldoBWhaC88kQByRsMrit4emidMEz

LINEAR REGRESSION
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
height=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0]]
weight=[  8, 10 , 12, 14, 16, 18, 20]
plt.scatter(height,weight,color='pink')
plt.xlabel("height")
plt.ylabel("weight")
reg=linear_model.LinearRegression()    #JUST linearreggrssion is a class ,  LinearRegression() becomes an object , with a dot is calling an object inside an object linear_model.LinearRegression()
reg.fit(height,weight)
X_height=[[13.0]]
print(reg.predict(X_height))

"""LINEAR REGRESSION WITH ACCURACY"""

# import modules
import warnings
import pandas as pd
from sklearn import model_selection
import numpy as np
import sklearn
from sklearn import linear_model
X=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0]]
y=[  8, 10 , 12, 14, 16, 18, 20]
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=7)
print("Training Features", X_train);print("Training Labels",y_train);print("Training Data",X_test);print("Testing Data",y_test)
reg=linear_model.LinearRegression()
reg.fit(X_train,y_train)
#accuracy on test set
result = reg.score(X_test, y_test)
print("Accuracy - test set: %.2f%%" % (result*100.0))
X_height=[[13.0]]
print(reg.predict(X_test))

"""DECISSION TREE

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
X = [[30],[40],[50],[60],[20],[10],[70]]
y = [0,1,1,1,0,0,1]
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X,y)
X_marks=[[20]]
print(classifier.predict(X_marks))

"""RAMDOM FOREST"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
RandomForestRegModel = RandomForestRegressor()
RandomForestRegModel.fit(X,y)
X_marks=[[70]]
print(RandomForestRegModel.predict(X_marks))

"""NAIVE BAISE """

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("diabetes.csv.xls")
df.head()
x=df.drop('diabetes',axis=1)
y=df['diabetes']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)
model=GaussianNB()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
y_pred

"""SUPPORT VECTOR MACHINE

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import SVC
X = [[30],[40],[50],[60],[20],[10],[70]]
y = [0,1,1,1,0,0,1]
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X,y)
X_marks=[[55]]
print(classifier.predict(X_marks))

"""K N N

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
X = [[30],[40],[50],[60],[20],[10],[70]]
y = [0,1,1,1,0,0,1]
from sklearn.neighbors import KNeighborsClassifier  
classifier= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2 )  
classifier.fit(X,y) 
X_marks=[[50]]
print(classifier.predict(X_marks))