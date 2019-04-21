# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:35:46 2019

@author: kdandebo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns', 500)
df = pd.read_csv('C:/Users/kdandebo/Desktop/Models/DS training/Yogesh data sets/Universities.csv')
print(df.head(10))
df.drop(['Univ'],axis=1,inplace=True)
print(df.head(10))
print(df.corr())
#converting into array
df = df.values
print(df)
#standardized = pd.DataFrame(df)
#df = standardized
#data = np.loadtxt(df)
#print(data)

#implementing PCA
from sklearn.decomposition import PCA
pca = PCA()
print(pca.fit(df))
print(pca.components_)
print(pca.explained_variance_)
print(pca.transform(df))
print(pca.explained_variance_ratio_)