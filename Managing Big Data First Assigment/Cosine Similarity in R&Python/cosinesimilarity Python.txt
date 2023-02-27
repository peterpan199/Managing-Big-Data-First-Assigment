import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def cosineSimilarity(vec1, vec2):
    cos = cosine_similarity(vec1.reshape(1,-1),vec2.reshape(1,-1))
    cos = str(cos)
    if len(cos) < 7 :
        return cos[2]
    elif cos[2] == "-" :
        return cos[2:9]
    else:
        return cos[2:8]


#####   A   #####
x = np.array([9.32, -8.3, 0.2])
y =  np.array([-5.3, 8.2, 7])
cosdist = cosineSimilarity(x, y)
print(f'The cosine similarity for task A is {cosdist}')

#####   B   #####
x = np.array([6.5, 1.3, 0.3, 16, 2.4, -5.2, 2, -6, -6.3])
y =  np.array([0.5, -1, -7.3, -7, -9.4, 8.2, -9, 6, 6.3])
cosdist = cosineSimilarity(x, y)
print(f'The cosine similarity for task B is {cosdist}')

#####   C   #####
x = np.array([-0.5, 1, 7.3, 7, 9.4, -8.2])
y =  np.array([1.25, 9.02, -7.3, -7, 15, 12.3])
cosdist = cosineSimilarity(x, y)
print(f'The cosine similarity for task C is {cosdist}')

#####   D   #####
x = np.array([2, 8, 5.2])
y =  np.array([2, 8, 5.2])
cosdist = cosineSimilarity(x, y)
print(f'The cosine similarity for task D is {cosdist}')



