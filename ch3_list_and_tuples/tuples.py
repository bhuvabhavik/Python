myTuple = (10,4,5,2,80,41,45,10)  #Once defined--cant modify later..its immutable

myEmptyTuple = ()

myOneElementTuple = (1,)  #Comma is necessary here coz else it cant identify that its tuple


print(myEmptyTuple)
print(myTuple)
print(myTuple[1])


#tuples method


print(myTuple.__len__())



print(myTuple.index(45))  #returns index of given element

print(myTuple.count(10))   #Counts no of 10s in tuple


