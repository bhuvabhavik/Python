a=[1,2,"Bhavik",4,5.85]   # we can create mix types lists
# Create lists using [] 

#changing the lists value
a[2] = "Bhavik Bhuva"

print(a) #print full list


#printing specific index element
print(a[4])
print(a[2])
print(a[1])

#list Slicing
friends = ["Ram","Shyam","Ghanshyam","Mani","Peter"]

print(friends[3])
print(friends[0:3])
print(friends[-3])

friends.sort()
print(friends)

friends.append("Manish") #inserts at end
print(friends)


friends.insert(0,"Radhi") #Inserts at specified index
print(friends)

friends.remove("Ghanshyam") #Removes the element
print(friends)

# friends.pop(0) #removes from specified index
# print(friends)





