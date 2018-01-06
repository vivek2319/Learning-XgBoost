
# coding: utf-8

# In[3]:

#Load the packages 
import numpy as np
import urllib.request
import xgboost
from sklearn import cross_validation
from sklearn.metrics import accuracy_score


# In[4]:

# URL for the Pima Indians Diabetes dataset (UCI Machine Learning Repository)
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"


# In[6]:

#Download the file 
raw_data = urllib.request.urlopen(url)


# In[7]:

# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
print(dataset.shape)


# In[8]:

X = dataset[:,0:8]
Y = dataset[:,8]


# In[9]:

# split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,Y)


# In[10]:

model = xgboost.XGBClassifier()
model.fit(X_train, y_train)


# In[11]:

# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]


# In[12]:

# evaluate predictions
accuracy = accuracy_score(y_test, predictions)

print("Accuracy: %.2f%%" % (accuracy * 100.0))


# In[ ]:


