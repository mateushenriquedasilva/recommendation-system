from math import sqrt
from recommendation import reviews

def euclidean_distance(userOne, userTwo):
  si = {}
  for item in reviews[userOne]:
    if item in reviews[userTwo]: si[item] = 1
    
  if len(si) == 0: return 0

  _sum = sum([pow(reviews[userOne][item] - reviews[userTwo][item], 2)
                  for item in reviews[userOne] if item in reviews[userTwo]])
  return 1/(1 + sqrt(_sum))

def getSimilar(user):
  similar = [(euclidean_distance(user, other), other)
             for other in reviews if other != user]
  
  similar.sort()
  similar.reverse()

  return similar

print(getSimilar('Pedro'))