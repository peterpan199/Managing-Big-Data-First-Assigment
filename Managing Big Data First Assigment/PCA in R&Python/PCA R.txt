install.packages("MASS")
library(MASS)
data(Cars93)
head(Cars93)


pcaData = Cars93[,c(4,5,6,7,8,12,13,14,15,17,18,19,20,21,22,23,24,25)]
pcaData

#check for missing values in each column
if (any(is.na(pcaData[,"Min.Price"]))) {
  sprintf("Min.Price has NA values")
} else
  sprintf("Min.Price is ok! ")

if (any(is.na(pcaData[,"Price"]))) {
  sprintf("Price has NA values")
} else
  sprintf("Price is ok! ")

if (any(is.na(pcaData[,"Max.Price"]))) {
  sprintf("Max.Price has NA values")
} else
  sprintf("Max.Price is ok! ")

if (any(is.na(pcaData[,"MPG.city"]))) {
  sprintf("MPG.city has NA values")
} else
  sprintf("MPG.city is ok! ")

if (any(is.na(pcaData[,"MPG.highway"]))) {
  sprintf("MPG.highway has NA values")
} else
  sprintf("MPG.highway is ok! ")

if (any(is.na(pcaData[,"EngineSize"]))) {
  sprintf("EngineSize has NA values")
} else
  sprintf("EngineSize is ok! ")

if (any(is.na(pcaData[,"Horsepower"]))) {
  sprintf("Horsepower has NA values")
} else
  sprintf("Horsepower is ok! ")

if (any(is.na(pcaData[,"RPM"]))) {
  sprintf("RPM has NA values")
} else
  sprintf("RPM is ok! ")

if (any(is.na(pcaData[,"Rev.per.mile"]))) {
  sprintf("Rev.per.mile has NA values")
} else
  sprintf("Rev.per.mile is ok! ")

if (any(is.na(pcaData[,"Fuel.tank.capacity"]))) {
  sprintf("Fuel.tank.capacity has NA values")
} else
  sprintf("Fuel.tank.capacity is ok! ")

if (any(is.na(pcaData[,"Passengers"]))) {
  sprintf("Panseggers has NA values")
} else
  sprintf("Panseggers is ok! ")

if (any(is.na(pcaData[,"Length"]))) {
  sprintf("Length has NA values")
} else
  sprintf("Length is ok! ")

if (any(is.na(pcaData[,"Wheelbase"]))) {
  sprintf("Wheelbase has NA values")
} else
  sprintf("Whellbase is ok! ")

if (any(is.na(pcaData[,"Width"]))) {
  sprintf("Width has NA values")
} else
  sprintf("Width is ok! ")

if (any(is.na(pcaData[,"Turn.circle"]))) {
  sprintf("Turn.circle has NA values")
} else
  sprintf("Turn.circle is ok! ")

if (any(is.na(pcaData[,"Rear.seat.room"]))) {
  sprintf("Rear.seat.room has NA values")
} else
  sprintf("Rear.seat.room is ok! ")

if (any(is.na(pcaData[,"Luggage.room"]))) {
  sprintf("Luggage.room has NA values")
} else
  sprintf("Luggage.room is ok! ")

if (any(is.na(pcaData[,"Weight"]))) {
  sprintf("Weight has NA values")
} else
  sprintf("Weight is ok! ")

#handling missing values in columns "Rear.seat.room" and "Luggage.room"
pcaData = pcaData[,-(16:17)]
str(pcaData)

#execute pca
principalComponents<-princomp(pcaData, cor=TRUE, score=FALSE)
print(principalComponents)
plot(principalComponents)


#Eigenvectors
Eigenvectors<-principalComponents$loadings[,1:16]
print(Eigenvectors)
plot(Eigenvectors)

#Eigenvalues
Eigenvalues<-principalComponents$sdev^2
print(Eigenvalues)
plot(Eigenvalues)

# The proportion of variance of new principal components
percent = proportions(Eigenvalues)*100
  print(percent)


principalComponents$loadings
principalComponents$scores

