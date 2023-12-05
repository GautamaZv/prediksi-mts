import pandas as pd 
import numpy as np 
  
df = pd.read_excel('datasetmts.xlsx') 
df.head(10) 
  
# splitting the data into the columns which need to be trained(X) and the target column(y) 
X = df.drop(["Keterangan"], axis=1)
y = df['Keterangan']
  
# splitting data into training and testing data with 30 % of data as testing data respectively 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0) 
  
# importing the gauss naive bayes classifier model and training it on the dataset 
from sklearn.naive_bayes import GaussianNB 
classifier = GaussianNB() 
classifier.fit(X_train, y_train) 
  
# predicting on the test dataset 
y_pred = classifier.predict(X_test) 
  
# finding out the accuracy 
from sklearn.metrics import accuracy_score 
score = accuracy_score(y_test, y_pred) 
print(score)

import pickle 
pickle_out = open("nbclassifier.pkl", "wb") 
pickle.dump(classifier, pickle_out) 
pickle_out.close()