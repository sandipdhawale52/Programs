
def Add(*Values):
    print(type(Values))
    print("Number of arguments are:",len(Values))
    sum = 0
    for no in Values:
        sum=sum+no
    return sum



def Add1(*Values):
    print(type(Values))
    print("Number of arguments are:",len(Values))
    sum = 0
    for i in range(0,len(Values),1):

        sum=sum+Values[i]
    return sum

def main():
    Ans=Add(10,20)
    print("Additon is:",Ans)

    Ans=Add1(10,20)
    print("Additon is:",Ans)

    
    
if __name__=="__main__":
    main()