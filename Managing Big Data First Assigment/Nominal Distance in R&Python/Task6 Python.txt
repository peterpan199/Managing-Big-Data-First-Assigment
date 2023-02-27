# we import the numpy library
import numpy as np

# we define the function
def nominalDistance(x,y):
    i=0
    l=0
    d=0
    for s in x:
         
         print(i)
         
         if s==y[i]:
             l +=1
             i=i+1
         else:
             l +=0  
             i=i+1
    d = (len(x) - l)
    return(d)

#Question a

x= ("Green", "Potato", "Ford")
y = ("Tyrian purple", "Pasta", "Opel")

d=nominalDistance(x,y)
print("The nominal Distance between x and y is equal to : ", d)

#Question b
x = np.array(["Eagle",  "Ronaldo", "Real madrid", "Prussian blue", "Michael Bay"]) 
y = np.array(["Eagle",  "Ronaldo", "Real madrid", "Prussian blue", "Michael Bay"]) 

d=nominalDistance(x,y)
print("The nominal Distance between x and y is equal to : ", d)

#Question c
x = np.array(["Werner Herzog", "Aquirre, the wrath of God", "Audi", "Spanish red"]) 
y = np.array(["Martin Scorsese", "Taxi driver", "Toyota", "Spanish red"]) 


d=nominalDistance(x,y)
print("The nominal Distance between x and y is equal to : ", d)

