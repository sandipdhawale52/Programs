def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B


def main():
    print("Enter First no")
    No1 =int(input())

    print("Enter secomd no")
    No2 =int(input())


    Ans=Add(No1,No2)
    print("Adddtion is",Ans)


    Ans=Sub(No1,No2)
    print("Substraction is",Ans)




if __name__=="__main__":
    main()