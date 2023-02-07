def Add(No1,No2):
    return No1+No2


    #lamda function/unnamed function
    #lamda parameters:body
AddFunction = lambda A,B :A+B
Ans1 = Add(10,11)
Ans2 = AddFunction(10,21)

print("Op using normal function:",Ans1)
print("Op using normal function:",Ans2)
print("Type of lambda function is",type(AddFunction))