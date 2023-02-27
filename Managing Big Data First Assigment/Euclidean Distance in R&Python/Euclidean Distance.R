############# create a function #############
euclideanDistance <- function(a,b){
  if (length(a) != length(b))
    return( "error")
  else 
    dist <- sqrt(sum(((a-b)^2)))
  return(dist)
} 

############ TASK 1 #############

#############     Α     #############
x= c(1,2,3,4,5,6)
y= c(1,2,3,4,5,6)
distance.a = euclideanDistance(x , y)
print(paste("The Distance between first x and y is : ", distance.a))


#############     B     #############
x= c(-0.5, 1, 7.3, 7, 9.4, -8.2, 9, -6, -6.3)
y= c(0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3)
distance.b = euclideanDistance(x , y)
print(paste("The Distance between first x and y is : ",distance.b ))


#############     C     #############
x= c(-0.5, 1, 7.3, 7, 9.4, -8.2)
y= c(1.25, 9.02, -7.3, -7, 5, 1.3)
distance.c = euclideanDistance(x , y)
print(paste("The Distance between first x and y is : ", distance.c))


#############     D     #############
x= c(0, 0, 0.2)
y= c(0.2, 0.2, 0)
distance.d = euclideanDistance(x , y)
print(paste("The Distance between first x and y is : ", distance.d))



############# TASK 2 #############

#############     Α     #############
user1 = c(25000, 14, 7)
user2 = c(42000, 17, 9)
user3 = c(55000, 22, 5)
user4 = c(27000, 13, 11)
user5 = c(58000, 21, 13)

distance.15 = euclideanDistance(user1, user5)
distance.25 = euclideanDistance(user2, user5)
distance.35 = euclideanDistance(user3, user5)
distance.45 = euclideanDistance(user4, user5)
distance.55 = euclideanDistance(user5, user5)
print(paste('The Distance between user 1 and user 5 is : ', distance.15))
print(paste('The Distance between user 2 and user 5 is : ', distance.25))
print(paste('The Distance between user 3 and user 5 is : ', distance.35))
print(paste('The Distance between user 4 and user 5 is : ', distance.45))
print(paste('The Distance between user 5 and user 5 is : ', distance.55))
d = c(distance.15, distance.25, distance.35, distance.45)
d
print(min(d))
##### User 3 is the most similar to user 5,because he has the smallest Euclidean differrence. 
#############     Β     #############

df = data.frame (distances = c(distance.15, distance.25, distance.35, distance.45, distance.55),
                minutes = c(25000, 42000, 55000, 27000, 58000),
                sms = c(12, 17, 22, 13, 21),
                mb = c(7, 9, 5, 11, 13))
                
model = lm(distances ~ minutes + sms + mb, data = df)

summary(model)$r.squared
var(df$minutes)
var(df$sms)
var(df$mb)
print('The variable that effects the most the variability of distance is "Minutes" because this variable has the highest varation(var=234300000).')

##### The coefficient of determination (R square) is 1. 
##### So the model represent perfect the varation of distance.
##### The variable that effects the most the variability of distance is "Minutes",
##### because this variable has the highest varation(var=234300000).

