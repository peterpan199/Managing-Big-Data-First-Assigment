############# create a function #############
cosineSimilarity<- function(A,B) { (sum(A*B))/sqrt((sum(A^2))*(sum(B^2))) }

#############     Α     #############
x = c(9.32, -8.3, 0.2) 
y = c(-5.3, 8.2, 7)
cos = cosineSimilarity(x , y)
cos

#############     B     #############
x = c(6.5, 1.3, 0.3, 16, 2.4, -5.2, 2, -6, -6.3)
y = c(0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3)
cos = cosineSimilarity(x , y)
cos

#############     C     #############
x = c(-0.5, 1, 7.3, 7, 9.4, -8.2)
y = c(1.25, 9.02, -7.3, -7, 15, 12.3)
cos = cosineSimilarity(x , y)
cos

#############     D     #############
x = c(2, 8, 5.2)
y = c(2, 8, 5.2)
cos = cosineSimilarity(x , y)
cos



