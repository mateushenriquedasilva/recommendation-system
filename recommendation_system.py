from math import sqrt
from data.reviews import reviews

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

def getRecommendations(user):
  total={}
  sumSimilarity={}

  for other in reviews:
    if other == user: continue
    similarity = euclidean_distance(user, other)

    if similarity <= 0: continue

    for item in reviews[other]:
      if item not in reviews[user]:
        total.setdefault(item, 0)
        total[item] += reviews[other][item] * similarity
        sumSimilarity.setdefault(item, 0)
        sumSimilarity[item] += similarity

  rankings=[(total/sumSimilarity[item], item) for item, total in total.items()] 
  rankings.sort()
  rankings.reverse()
  
  filtering = [item for item in rankings if item[0] > 3]
  
  return rankings

print(getRecommendations('Claudia'))