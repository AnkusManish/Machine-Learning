#!/usr/bin/env python
# coding: utf-8

# In[244]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sea
from sklearn.decomposition import PCA


data = pd.read_csv('Live.csv')

print(data.info()))


print(data.head())


print(data.isnull().sum())


# In[254]:


data.drop(['Column1','Column2','Column3','Column4', 'status_id'], axis = 1, inplace = True)


# In[255]:


print(data.head())


# In[256]:


#Label encoding status_type
data['status_type'] = data['status_type'].map(lambda x:1 if(x == 'video') else 0)


# In[257]:


print(data.head())


# In[258]:


#converting to date_time object
data['status_published'] = pd.to_datetime(data['status_published'])


# In[259]:


print(data.head())


# In[260]:


data['year'] = data['status_published'].dt.year
data['month'] = data['status_published'].dt.month
data['dayofweek'] = data['status_published'].dt.dayofweek
data['hour'] = data['status_published'].dt.hour

data.drop(['status_published'], axis = 1, inplace = True)


# In[261]:


data.head()


# In[262]:


plt.figure(figsize = (8,6))
sea.countplot(data['status_type'])
plt.title('Count of Videos andPhotos posted', fontsize = 20, pad = 20)
plt.xlabel('Photo / Video', fontsize = 15)
plt.ylabel('Count', fontsize = 15)
plt.show()


# In[263]:


plt.figure(figsize = (8,6))
sea.countplot(data['year'])
plt.title('Count of Instances with respect to the Year', fontsize = 20, pad = 20)
plt.xlabel('Photo / Video', fontsize = 15)
plt.ylabel('Count', fontsize = 15)
plt.show()


# from the above plot we can see that the reactions almost tripled in 2017 and 2018 compared to previous years

# In[264]:


data.describe()


# In[265]:


data_before_2015 = data[data['year'] <= 2015]
data_after_2015 = data[data['year'] > 2015]


# In[266]:


data_before_2015.describe()


# In[267]:


data_after_2015.describe()


# In[274]:


#storing different reactions in the variable to perform EDA
reactions = ['num_reactions', 'num_comments', 'num_shares', 'num_likes', 'num_loves', 'num_wows', 'num_hahas',
            'num_sads', 'num_angrys']


# In[269]:


data_before_2015.groupby('year').sum()[reactions]


# In[270]:


data_after_2015.groupby('year').sum()[reactions]


# In[271]:


data_before_2015.groupby('status_type').mean()[reactions]


# In[272]:


plt.figure(figsize = (8,6))
sea.heatmap(data_before_2015[reactions].corr(), annot = True, cmap = 'summer')


# We can see that comments and shares are closely correlated features

# In[215]:


data_after_2015.groupby('status_type').mean()[reactions]


# In[216]:


plt.figure(figsize = (8,6))
sea.heatmap(data_after_2015[reactions].corr(), annot = True, cmap = 'summer')


# In[217]:


data_before_2015.groupby(['year', 'status_type']).sum()[reactions]


# In[218]:


data_after_2015.groupby(['year', 'status_type']).sum()[reactions]


# In[219]:


data_after_2015.groupby('year').sum()[reactions].plot(figsize = (12,7), title = 'Reactions with respect to Year')
plt.show()


# In[220]:


data_after_2015[data_after_2015['status_type'] == 1].groupby('year').sum()[reactions].plot(figsize = (12,7), title = 'Reactions with respect to Year for Video Content')
plt.show()


# In[221]:


data_after_2015[data_after_2015['status_type'] == 0].groupby('year').sum()[reactions].plot(figsize = (12,7), title = 'Reactions with respect to Year for Photo Content')
plt.show()


# We can clearly see that number of reactions and likes are much higher compared to Video content

# In[242]:


data_after_2015[data_after_2015['status_type'] == 1].groupby('month').sum()[reactions].plot(figsize = (12,7), title = 'Reactions with respect to Month for Video Content')
plt.xlabel('Month', fontsize = 15)
plt.show()


# In[241]:


data_after_2015[data_after_2015['status_type'] == 0].groupby('month').sum()[reactions].plot(figsize = (12,7), title = 'Reactions with respect to Month for Photo Content')
plt.xlabel('Month', fontsize = 15)
plt.show()


# In[240]:


data_after_2015[data_after_2015['status_type'] == 0].groupby('dayofweek').sum()[reactions].plot(figsize = (12,7), title = 'Reactions with respect to Day for Photo Content')
plt.xlabel('Day of Week', fontsize = 15)
plt.show()


# In[239]:


data_after_2015[data_after_2015['status_type'] == 1].groupby('dayofweek').sum()[reactions].plot(figsize = (12,7), title = 'Reactions with respect to Day for Video Content')
plt.xlabel('Day of Week', fontsize = 15)
plt.show()


# In[238]:


data_after_2015[data_after_2015['status_type'] == 1].groupby('hour').sum()[reactions].plot(figsize = (12,7), title = 'Reactions with respect to Hour for Video Content')
plt.xlabel('Hour', fontsize = 15)
plt.show()


# In[237]:


data_after_2015[data_after_2015['status_type'] == 0].groupby('hour').sum()[reactions].plot(figsize = (12,7), title = 'Reactions with respect to Day for Photo Content')
plt.xlabel('Day', fontsize = 15)
plt.show()


# In[273]:


data_reactions = data.drop(['status_type','year','month','dayofweek','hour'], axis = 1)


# In[246]:


pca = PCA(n_components = 2, random_state = 42)
data = pca.fit_transform(data_reactions)
explained_variance = pca.explained_variance_ratio_


# In[247]:


explained_variance


# In[248]:


loadings = pd.DataFrame({'PC1':pca.components_[0],'PC2':pca.components_[1], 'Feature':reactions})


# In[249]:


fig = plt.figure(figsize = (6,6))
plt.scatter(loadings.PC1, loadings.PC2)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
for i, txt in enumerate(loadings.Feature):
    plt.annotate(txt, (loadings.PC1[i],loadings.PC2[i]))
plt.tight_layout()
plt.show()


# In[140]:


from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import time


# In[133]:


X = data.iloc[:,:].values


# In[136]:


sc = StandardScaler()
X = sc.fit_transform(X)


# ## Choosing optimal K value 

# ## Method 1

# In[141]:


start_time = time.time()
SSD = []

for i in range(1,15):
    clf = KMeans(n_clusters = i)
    clf.fit(data)
    SSD.append(clf.inertia_)
print('Total time taken : {}'.format(time.time() - start_time))

plt.figure(figsize = (8,6))
plt.plot(range(1,15), SSD, 'bx')
plt.plot(range(1,15), SSD)
plt.xlabel('K Value', fontsize = 15)
plt.ylabel('Inertia', fontsize = 15)
plt.title('Graph for showing the optimal K value', fontsize = 20, pad = 20)
plt.show()


# ## Method - 2

# In[142]:


from sklearn.metrics import silhouette_score, silhouette_samples

for n_clusters in range(2,15):
    km = KMeans (n_clusters=n_clusters)
    preds = km.fit_predict(data)
    centers = km.cluster_centers_

    score = silhouette_score(data, preds, metric='euclidean')
    print ("For n_clusters = {}, silhouette score is {}".format(n_clusters, score))


# ## Method - 3

# In[153]:


from yellowbrick.cluster import SilhouetteVisualizer

# Instantiate the clustering model and visualizer
km = KMeans(n_clusters=2)
visualizer = SilhouetteVisualizer(km)

visualizer.fit(data) # Fit the training data to the visualizer
visualizer.poof() # Draw/show/poof the data


# ## Defining K means Model

# In[159]:


def model(data):
    #defining number of cluster you want
    n_clusters = 2

    clf = KMeans(n_clusters = n_clusters, init = 'k-means++', max_iter = 100)
    clf.fit(data)
    
    print('The centroids for the clusters are: \n')
    print(clf.cluster_centers_)
    
    y_pred = clf.predict(data)
    
    return y_pred, clf.cluster_centers_ 


# In[160]:


y_pred, clusters = model(data)


# ## Applying Agglomerative Clustering

# In[154]:


from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering


# In[277]:


cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')  
cluster.fit(data)


# In[156]:


plt.figure(figsize=(10, 7))  
plt.title("Dendrograms", fontsize = 15)  
dend = dendrogram(linkage(data, method='ward'))


# The above plot represents the clustering diagram
