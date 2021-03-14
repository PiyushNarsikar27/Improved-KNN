def takeFirst(elem):
  return elem[0]
def improved_knn_predictor(xtrain,xtest,ytrain,k,num_classes):
  y_pred=[]
  x=0  # x indicates how many elements are processed so far
  for test_point in xtest: 
    i=0
    distances=[]
    dist=[]
    for train_point in xtrain:  # Creating a list of distances from each of the other test points. Each element of the list "distances" includes the distance and the class of the respective test point.
      dist=[np.linalg.norm(test_point-train_point),ytrain[i]]
      distances.append(dist)
      i += 1
    distances.sort(key=takeFirst) # Sorting the list based on the distance from the test point currently being processed in ascending order
    sumlist=[]
    for f in range(num_classes):  # Creating a list of average distance of k nearest neighbors belonging to each class from the test point currently being processed
      sum=0
      count=0
      toAdd=[]
      for g in range(len(distances)):
        if count==k:
          break
        if distances[g][1]==f:
          sum += distances[g][0]
          count += 1
      sum=sum/k
      toAdd=[sum,f]
      sumlist.append(toAdd)
    sumlist.sort(key=takeFirst)  # Sorting the averages in ascending order
    y_pred.append(distances[0][1]) # Predicting the class of the current test point as the one with lowest average distance
    print(x,end=" ")
    x += 1 # Incrementing the progress indicator variable x
  return y_pred 
