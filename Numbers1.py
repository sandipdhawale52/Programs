class NumberX:
    def __init__(self):
        self.Size = 0
        self.Arr=list()

    def Accept(self):
        print("enter how many element u want")
        self.Size  = int(input())

        print("please emter  the element ")
        value=0
        for i in range(0,self.Size):
            value=int(input())
            self.Arr.append(value)

    def Display(self):
        print("Elemets from list are:")
        for i in range(0,self.Size):
            print(self.Arr[i])

    def Summation(self):
        Sum=0
        for i in range(0,self.Size):
            Sum=Sum+self.Arr[i]
        return Sum
            

def main():
        obj = NumberX()
        obj.Accept()
        obj.Display()
        output=obj.Summation()
        print("Summation is:",output)
        
        
if __name__=="__main__":
        main()