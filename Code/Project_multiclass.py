#!/usr/bin/env python2
#Ashish Jain(MT18052)
#Shubham Gupta(MT18055)


import pandas as pd
import numpy as np
import copy
import seaborn as seab
from sklearn import metrics
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from scipy.sparse import csr_matrix, hstack

def add_feature(X, feature_to_add):
    '''
    Returns sparse feature matrix with added feature.
    feature_to_add can also be a list of features.
    '''
    return hstack([X, csr_matrix(feature_to_add).T], 'csr')

train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('testtest.csv')
print train_df.describe()

import warnings
warnings.filterwarnings('ignore')

print ('comments that are non toxic:')
nontoxic=len(train_df[(train_df['toxic']==0) & (train_df['severe_toxic']==0) & (train_df['obscene']==0) & (train_df['threat']== 0) & (train_df['insult']==0) & (train_df['identity_hate']==0)])
print nontoxic 
print ('Percentage of comments that are non toxic:')
print (float(nontoxic)/len(train_df))*100

categories = ['toxic','severe_toxic','obscene','threat','insult','identity_hate']
train_comment = train_df.comment_text
test_comment = test_df.comment_text
print test_comment.shape,train_comment.shape

data = train_df[['toxic','severe_toxic','obscene','threat','insult','identity_hate']]
corr = data.astype(float).corr()
seab.heatmap(corr,linewidths=0.4,linecolor='white',annot=True)

vect = TfidfVectorizer(max_features=4000,stop_words='english')
train_vec = vect.fit_transform(train_comment)
test_vec = vect.transform(test_comment)
Zlist = []
for clas in categories:
    Zlist.append(test_df[clas].tolist())
    #print test_df[clas]
    #print Zlist[len(Zlist) - 1]
    

print train_vec.shape
Zlist = np.array(Zlist)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
logreg = LogisticRegression(C=12.0)
nbmodel = MultinomialNB()




resultantMatrix = []
resultantMatrix.append(['Labels','toxic','severe_toxic','obscene','threat','insult','identity_hate'])
matindex = 0



#######################################################################

#logistic regression with binary relevance

matindex +=1
resultantMatrix.append([])
resultantMatrix[matindex].append("Logistic Regression Binary Relevance Accuracy")
index = 0
for classes in categories:
    print 'Processing',classes
    y = train_df[classes]
    Z = Zlist[index]
    logreg.fit(train_vec, y)
    y_pred_X = logreg.predict(test_vec)
    accuracy=accuracy_score(Z, y_pred_X)
    print 'Training accuracy :',accuracy
    resultantMatrix[matindex].append(accuracy)
    mett=metrics.classification_report(Z,y_pred_X)
    print mett
    test_y_prob = logreg.predict_proba(test_vec)[:,1]
    index +=1
    
 
dummy = []
#######################################################################
#Naive Bayes with binary relevance
index = 0
matindex +=1
resultantMatrix.append([])
resultantMatrix[matindex].append("MultinomialNB Binary Relevance Accuracy")
for classes in categories:
    print 'Processing',classes
    y = train_df[classes]
    Z = Zlist[index]
    #logreg.fit(train_vec, y)
    model = MultinomialNB()
    model.fit(train_vec, y)  
    #y_pred_X = logreg.predict(test_vec)
    y_pred_X= model.predict(test_vec)
    #dummy.append(y_pred_X[0])
    accuracy=accuracy_score(Z, y_pred_X)
    print 'Training accuracy :',accuracy
    resultantMatrix[matindex].append(accuracy)
    mett=metrics.classification_report(Z,y_pred_X)
    print mett
    test_y_prob = model.predict_proba(test_vec)[:,1]
    dummy.append(test_y_prob)
    index +=1
print dummy

#######################################################################
# Logistic regression with classifier chain

index = 0
matindex +=1
resultantMatrix.append([])
resultantMatrix[matindex].append("Logistic Regression Classifier Chain Accuracy")
test_vec_chain = copy.deepcopy(test_vec)
train_vec_chain = copy.deepcopy(train_vec)
for classes in categories:
    print 'Processing',classes
    y = train_df[classes]
    Z = Zlist[index]
    #model = MultinomialNB()
    #logreg.fit(train_vec, y)
    logreg.fit(train_vec_chain, y)  
    y_pred_X = logreg.predict(test_vec_chain)
    #y_pred_X= model.predict(test_vec_chain)
    accuracy=accuracy_score(Z, y_pred_X)
    print 'Training accuracy :',accuracy
    resultantMatrix[matindex].append(accuracy)
    mett=metrics.classification_report(Z,y_pred_X)
    print mett    
    #test_y=logreg.predict(test_vec)
    #test_y_prob = model.predict_proba(test_vec)[:,1]
    train_vec_chain = add_feature(train_vec_chain, y)
    print('Shape of train_vec is now {}'.format(train_vec_chain.shape))
    # chain current label predictions to test_train_vec
    test_vec_chain = add_feature(test_vec_chain, y_pred_X)
    print('Shape of test_train_vec is now {}'.format(test_vec_chain.shape))
    index +=1

#######################################################################
#Naive Bayes with classifier chain
index = 0
matindex +=1
resultantMatrix.append([])
resultantMatrix[matindex].append("MultinomialNB Classifier Chain Accuracy")
test_vec_chain = copy.deepcopy(test_vec)
train_vec_chain = copy.deepcopy(train_vec)
for classes in categories:
    print 'Processing',classes
    y = train_df[classes]
    Z = Zlist[index]
    nbmodel.fit(train_vec_chain, y)  
    y_pred_X= nbmodel.predict(test_vec_chain)
    accuracy=accuracy_score(Z, y_pred_X)
    print 'Training accuracy :',accuracy
    resultantMatrix[matindex].append(accuracy)
    mett=metrics.classification_report(Z,y_pred_X)
    print mett    
    train_vec_chain = add_feature(train_vec_chain, y)
    print('Shape of train_vec is now {}'.format(train_vec_chain.shape))
    # chain current label predictions to test_train_vec
    test_vec_chain = add_feature(test_vec_chain, y_pred_X)
    print('Shape of test_train_vec is now {}'.format(test_vec_chain.shape))
    index +=1
#######################################################################    
import csv
with open("graph.csv", 'w') as writeFile:
   writer = csv.DictWriter(writeFile, fieldnames=resultantMatrix[0])
   writer = csv.writer(writeFile)
   for row in range(0,len(resultantMatrix)):
       writer.writerow(resultantMatrix[row])