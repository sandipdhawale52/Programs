Data=[11,21,51,101]

print("Outpit usinf for :")
for no in Data:
    print(no,end="  ")
print()

print("----------------------------------")

print("Outpit using for wiith index :")
for i in range(0,len(Data)):
    print(Data[i],end="  ")
print()


print("----------------------------------")


print("Outpit using  while with index :")
while(i < len(Data)):
    print(Data[i],end=" ")
    i+=1
    print()
