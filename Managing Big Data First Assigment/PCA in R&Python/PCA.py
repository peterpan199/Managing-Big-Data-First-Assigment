import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import csv
from math import fabs


##### Read csv file in python #####
data= pd.read_csv('C:\metaptyxiako\diaxeirhsh megalwn dedomenwn\Managing Big Data First Assigment\Topic 3\winequality-white.csv',sep=";", header=0)

print('Lets take a look at the data')
print(data)

print('Lets take a look at the types of the data')
print(data.dtypes)


print('We have to delete variable quality')
datapca = data.loc[:, :"alcohol"]
print('Data ready for PCA')
print(datapca)

variables = []
##### PCA #####
pca = decomposition.PCA(n_components=11)
pca.fit(datapca)
tdata= pca.transform(datapca)
print('transformedwines')
print(tdata)
cov_mat = np.cov(tdata)

##### Print Eigenvalues #####
print("Eigenvalues:")
for i in range(len(pca.explained_variance_)):
    print("-----+++++-----")
    print(f"λ{i+1}: {pca.explained_variance_[i]}")

##### Print Eigenvectors #####
print("Eigenvectors:")
eigen = []
z = 0
for eigenvector in pca.components_:
    print("---------------++++++++++---------------")
    z += 1
    print(f"Eigenvector {z} : {eigenvector}")
    eigen.append(eigenvector)

variables = []
for col in datapca.columns:
    variables.append(col)
print(variables)
for i in range(len(eigen)):
    print(f'New variable {i + 1}= ')
    for j in range(len(variables)):
         if eigen[i][j] >= 0:
            print(f'+({eigen[i][j]} * {variables[j]})',)
         else:
             print(f'-({fabs(eigen[i][j])} * {variables[j]})',)
    print('\n')





##### Print the variance ratio #####
for i in range(len(pca.explained_variance_ratio_)) :
    print("---------------+++++++++++++++---------------")
    print(f"The variance ratio for λ{i+1} is {pca.explained_variance_ratio_[i]}")


















