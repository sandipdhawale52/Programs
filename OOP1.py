class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B


    def Add(self):
         Ans = self.No1+self.No2
         return Ans

    def Substraction(self):
            Ans = self.No1-self.No2
            return Ans

def main():
    print("Inside main method")
    obj = Arithmatic(11,10)
    output=obj.Add()
    print("Additon is",output)
    
    output=obj.Substraction()
    print("Sub  is",output)
  
if __name__=="__main__":
    print("Inside Starter")

    main()