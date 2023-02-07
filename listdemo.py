print("Demondstration of list")

#Data:   Hetererogeneous  
#ordered:  yes
#Indexed:  yes
#Mutable:  yes
#Duplicates:  yels

data=[11,21,51,101]

data1=[10,20,30,True,"Hello",10,29]
print("Data is Heterogeneous",data1)
print("Data is ordered",data1)
print("Data is index",data1[2])
print("Data is Heterogeneous",data)

print("List is mutable")
data.append(201)
print("Data after append is",data)

data.pop(3)
print("Data after remove is",data)


data.pop()

