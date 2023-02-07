Batches={"PPA":18000,"LB":16700,"python":16600,"Angular":15000}

print("Dateof Diectionary",Batches)
print("Types of Dictionary",type(Batches))
print("Length of Dictionary is",len(Batches))

print("Calue of PPA is",Batches["PPA"])


print("Data trsversal using loop")
for x in Batches:
    print(x)


print("Data trsversal using for loop")

for x in Batches:
    print(x,Batches.get(x))


print("Data trsversal using for loop")

for x in Batches:
    print(x,Batches[x])


    keyBatches=Batches.keys()
    print(type(keyBatches))
    print(keyBatches)

    ValueBatches=Batches.keys()
    print(type(ValueBatches))
    print(ValueBatches)

for i in range:
    print("BAtch name is:",keyBatches,end=" ")
    print("Fees are",ValueBatches[i])    





