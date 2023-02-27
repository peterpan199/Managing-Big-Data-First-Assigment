from sklearn.linear_model import  LinearRegression
import numpy as np
import pandas
import statistics

##### Difine cosine similariry function #####
def euclideanDistance(vec1, vec2):
    dist = np.linalg.norm(vec1 - vec2)
    return dist

##### TASK 1 #####
#####   A   #####
print("-----  TASK 1  -----")
print("-----    A     -----")
x = np.array([1,2,3,4,5,6])
y = np.array([1,2,3,4,5,6])
dist = euclideanDistance(x, y)
print(f"The distance between the two vectors is {dist}")

#####   B   #####
print("-----    B     -----")
x = np.array([-0.5, 1, 7.3, 7, 9.4, -8.2, 9, -6, -6.3])
y = np.array([0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3])
dist = euclideanDistance(x, y)
print(f"The distance between the two vectors is {dist}")

#####   C   #####
print("-----    C     -----")
x = np.array([-0.5, 1, 7.3, 7, 9.4, -8.2])
y = np.array([1.25, 9.02, -7.3, -7, 5, 1.3])
dist = euclideanDistance(x, y)
print(f"The distance between the two vectors is {dist}")

#####   D   #####
print("-----    D     -----")
x = np.array([0, 0, 0.2])
y = np.array([0.2, 0.2, 0])
dist = euclideanDistance(x, y)
print(f"The distance between the two vectors is {dist}")
print("")
print("")

##### TASK 2 #####
#####   A    #####
print("-----  TASK 2  -----")
print("-----    A     -----")
##### Difine the vectors for users #####
user1 = np.array([25000, 14, 7])
user2 = np.array([42000, 17, 9])
user3 = np.array([55000, 22, 5])
user4 = np.array([27000, 13, 11])
user5 = np.array([58000, 21, 13])
userlist = [user1, user2, user3, user4,user5]


##### Find the distances #####
distances = []
for i in range(len(userlist)-1 ) :
    distance = euclideanDistance(userlist[i], user5)
    print(f'The distance between user{i+1} and user 5 is {distance}')
    distances.append(distance)
distances = list(distances)
minimum = min(distances)
finder = 0
for i in range(len(distances)):
    if distances[i] == minimum :
        finder = i
        break
print(f'User {finder + 1} looks like the most with user 5')
distances.append(0)

####    B   #########

print("-----    B     -----")
user1 = np.array([25000, 12, 7, distances[0]])
user2 = np.array([42000, 17, 9, distances[1]])
user3 = np.array([55000, 22, 5, distances[2]])
user4 = np.array([27000, 13, 11, distances[3]])
user5 = np.array([58000, 21, 13, distances[4]])
#####  WE create a linear regression model and the variable with the biggest r square has the most effect in distance 's change #####
data = pandas.DataFrame([user1,user2,user3,user4,user5],["User 1", "User 2", "User 3", "User 4", "User 5"],['min','sms', 'mb', 'distance'])
print(data)

#####  R^2 for minutes  #####
X = data[['min', "sms", "mb"]]
y = data[['distance']]
regr = LinearRegression().fit(X, y)
r_sq = regr.score(X, y)

print(f"R squared for minutes is {r_sq}. So all the proportion of total variation of distance is explained by the model")
varmin =statistics.variance(data['min'])
print(f'The Variance of variable min is {varmin}')
varsms =statistics.variance(data['sms'])
print(f'The Variance of variable sms is {varsms}')
varmb =statistics.variance(data['mb'])
print(f'The Variance of variable mb is {varmb}')
print(f'The variable with the highest variance has the most effect on the variation of distance, which in our case is Minutes')
