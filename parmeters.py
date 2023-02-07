#Positional Argument==//Keywors argument//In this case you should know the name of function parameters--------
def Add(No1,No2):
    print("Value of No1:",No1)
    print("Value of No2:",No2)
    return No1+No2

def Sub1(No1,No2):
    print("Value of No1:",No1)
    print("Value of No2:",No2)
    return No1-No2

def main():
    Ans = 0.0
    Ans=Add(10,11)                  #Positional Parametres
    print("Adition is:",Ans)

    Ans=Sub1(No1 = 11, No2 = 10)    #Keyword Parametrs
    print("Substraction is:",Ans)




if __name__=="__main__":
    main()