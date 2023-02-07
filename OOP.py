
class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
    

    def Add(self):
        return self.No1+self.No2

    
    def Sub(self):
        return self.No1-self.No2


def main():

    print("Enter First no")
    No1 =int(input())

    print("Enter secomd no")
    No2 =int(input())

    obj =Arithmatic(No1,No2)
    Ans = obj.Add()
    print("ADDtion is",Ans)

    Ans = obj.Sub()
    print("Substraction is",Ans)


if __name__=="__main__":
    main()






