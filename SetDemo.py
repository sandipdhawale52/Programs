print("Demondstration of Set")

#Data:   Hetererogeneous  
#ordered:  No
#Indexed: No
#Mutable:  yes
#Duplicates:  No

data={11,21,51,101,51,11}  #Duplicate no store
print("Length of Data is :",len(data))
data1={10,20,30,True,"Hello"}
print("data first",data)
print("Data is Heterogeneous",data1)
print("Data is unordered",data1)
print("Data is index",data1[2])
print("Data is Unique element",data)

print("Set is mutable")
data.add(44)
print(data)
