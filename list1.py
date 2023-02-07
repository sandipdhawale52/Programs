

Values = [10,20,30,40]

print(Values)

print(type(Values))

print(len(Values))

print(Values[0])
print(Values[1])
print(Values[2])
print(Values[3])

Values.append(50)
print(Values)

Values.remove(20)
print(Values)

Values.append(50)
print(Values)
print(type(Values[0]))

Values.append(10.89)
print(Values)

Values.insert(2,11)
print(Values)

print("Size of lisrt is now :",len(Values))
