#!/usr/bin/env python
# coding: utf-8

# In[216]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sea
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA

import os
import glob
import pickle
# path for S_1 Folder
path_s1 = '/Users/ankusmanish/Desktop/Datasets_Healthy_Older_People/S1_Dataset/'


all_files=glob.glob(path_s1+'/*')


li=[]
for file in all_files:
    #print(file)
    if file.endswith('.txt'):
        continue
    df = pd.read_csv(file,header=None,index_col=None)
    li.append(df)
data_s1 = pd.concat(li,axis=0,ignore_index=True)
data_s1.columns = ['Time ', 'Acceleration-Frontal', 'Acceleration-Vertical', 'Acceleration-Lateral', 'Id', 'Signal-Strength', 'Phase', 'Frequency', 'Label']

#Path for S_2 Folder
path_s2 = '/Users/ankusmanish/Desktop/Datasets_Healthy_Older_People/S2_Dataset'

all_files_2=glob.glob(path_s2+'/*')


li=[]
for file in all_files_2:
    #print(file)
    if file.endswith('.txt'):
        continue
    df = pd.read_csv(file,header=None,index_col=None)
    li.append(df)
data_s2 = pd.concat(li,axis=0,ignore_index=True)
data_s2.columns = ['Time ', 'Acceleration-Frontal', 'Acceleration-Vertical', 'Acceleration-Lateral', 'Id', 'Signal-Strength', 'Phase', 'Frequency', 'Label']


data = pd.concat([data_s1, data_s2], axis = 0)


sea.set(style="darkgrid")
plt.figure(figsize = (10,8))
sea.countplot(x = data['Label'],
              linewidth = 5)

plt.title('Label Distribution', fontsize = 25, pad = 20)
plt.xlabel('Label', fontsize = 15)
plt.ylabel('Count', fontsize = 15)
plt.show()


fig, ax = plt.subplots(figsize = (15,8)) 
sea.kdeplot(data[data['Label'] == 1]['Id'],
            color = 'gray',
            shade = True,
            legend = True,
            label = 'Sit on bed')

sea.kdeplot(data[data['Label'] == 2]['Id'],
            color = 'lightgreen',
            shade = True,
            legend = True,
            label = 'Sit on chair')

sea.kdeplot(data[data['Label'] == 3]['Id'],
            color = 'red',
            shade = True,
            legend = True,
            label = 'Lying')

sea.kdeplot(data[data['Label'] == 4]['Id'],
            color = 'blue',
            shade = True,
            legend = True,
            label = 'Ambulating')

plt.title('Label of Activity ', fontsize = 25, pad = 40)
plt.ylabel("Frequency of Activities", fontsize = 15, labelpad = 20)
plt.xlabel("Activity", fontsize = 15,labelpad =20)
plt.show()


fig, ax = plt.subplots(2,2,figsize = (15,9))
sea.boxplot(x = 'Acceleration-Vertical', data = data, ax = ax[0][0])
sea.boxplot(x = 'Acceleration-Frontal', data = data, ax = ax[0][1])
sea.boxplot(x = 'Frequency', data = data, ax = ax[1][0])
sea.boxplot(x = 'Phase', data = data, ax = ax[1][1])
plt.show()


plt.figure(figsize=(12,10))
sea.pairplot(data) 


#Plotting Correlation Matrix
plt.figure(figsize=(10,8))
data_corr = data.corr()
sea.heatmap(data_corr)
plt.title('Correlation Matrix', fontsize = 25, pad = 20)

X = data.iloc[:,:-1].values
y = data['Label'].values


# ## Model without Scaling

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

best_svc = SVC(kernel='rbf', gamma = 'auto')
best_svc.fit(X_train, y_train)
y_pred = best_svc.predict(X_test)
print(accuracy_score(y_test, y_pred))
sea.heatmap(confusion_matrix(y_test, y_pred), annot = True, cmap = 'summer')
plt.show()


# ## Model using Standard Scalar

sc = StandardScaler()
X = sc.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
best_svc = SVC(kernel='rbf', gamma = 0.0001, C = 10)
best_svc.fit(X_train, y_train)
y_pred = best_svc.predict(X_test)
print(accuracy_score(y_test, y_pred))
sea.heatmap(confusion_matrix(y_test, y_pred), annot = True, cmap = 'summer')
plt.show()


# ## Model using PCA
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pca = PCA(n_components = 2, random_state = 42)
X_train = pca.fit_transform(X_train)
X_test = pca.transform((X_test))
explained_variance = pca.explained_variance_ratio_
best_svc = SVC(kernel='rbf', gamma = 0.0001, C = 10)
best_svc.fit(X_train, y_train)
y_pred = best_svc.predict(X_test)
print(accuracy_score(y_test, y_pred))


#Testing the model by taking random values
X = data.iloc[:,:-1].values
y = data['Label'].values
sc = StandardScaler()
X = sc.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
y_pred = best_svc.predict(X_test)
print(accuracy_score(y_pred, y_test))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
y_pred = best_svc.predict(X_test)
print(accuracy_score(y_pred, y_test))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=5)
y_pred = best_svc.predict(X_test)
print(accuracy_score(y_pred, y_test))


# ## Testing on dataset - 1

test = pd.read_csv('/Users/ankusmanish/Desktop/Datasets_Healthy_Older_People/S1_Dataset/d1p48M')
test.columns = ['Time ', 'Acceleration-Frontal', 'Acceleration-Vertical', 'Acceleration-Lateral', 'Id', 'Signal-Strength', 'Phase', 'Frequency', 'Label']

X = test.iloc[:,:-1].values
y = test['Label'].values
X = sc.transform(X)
y_pred = best_svc.predict(X)
print(accuracy_score(y_pred, y))


# ## Testing on dataset - 2

test = pd.read_csv('/Users/ankusmanish/Desktop/Datasets_Healthy_Older_People/S1_Dataset/d1p31F')
test.columns = ['Time ', 'Acceleration-Frontal', 'Acceleration-Vertical', 'Acceleration-Lateral', 'Id', 'Signal-Strength', 'Phase', 'Frequency', 'Label']

X = test.iloc[:,:-1].values
y = test['Label'].values
X = sc.transform(X)
y_pred = best_svc.predict(X)
print(accuracy_score(y_pred, y))


# ## Testing on dataset - 3

test = pd.read_csv('/Users/ankusmanish/Desktop/Datasets_Healthy_Older_People/S1_Dataset/d1p41M')
test.columns = ['Time ', 'Acceleration-Frontal', 'Acceleration-Vertical', 'Acceleration-Lateral', 'Id', 'Signal-Strength', 'Phase', 'Frequency', 'Label']
X = test.iloc[:,:-1].values
y = test['Label'].values
X = sc.transform(X)
y_pred = best_svc.predict(X)
print(accuracy_score(y_pred, y))


# ## Storing model

with open("object.pickle", "wb") as output_file:
    pickle.dump(best_svc, output_file)

# Storing the standard scalar object
with open("sc.pickle", "wb") as output_file:
    pickle.dump(sc, output_file)






