def get_sum(a,b):
    if (a == b) :
        return a
    abArray = [a,b]
    arrayToAdd = []
    minAb = min(abArray)
    maxAb = max(abArray)
    while (minAb <= maxAb) :
      arrayToAdd.append(minAb)
      minAb = minAb + 1
    return sum(arrayToAdd)
  
get_sum(1,2)
