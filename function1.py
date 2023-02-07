def Demo1():
    print("Inside main")

def Demo2(No):
    print("Inside Demo2 with argument:",No)


def Demo3(NO):
    print("Inside Demo3 is:",NO)
    return NO+2

def Demo4(No1,No2):
    print("Inside Demo4")
    Add=No1+No2
    return Add

def Demo5(No1,No2):
    print("Inside Demo5:")
    Add=No1+No2
    Sub=No1-No2
    return Add,Sub


def main():
    Demo1()
    Demo2("Hello")
    Ans=Demo3(10)
    print("return value of Demo3 is",Ans)
    Ans=Demo4(10,11)
    
    print("Reurn value is",Ans)
    Ans1,Ans2=Demo5(12,11)
    print("First return value:",Ans1)
    print("Second value is :",Ans2)



if __name__=="__main__":
    main()    