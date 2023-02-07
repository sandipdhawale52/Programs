

def Display(iNo):
    iCnt=0
    if(iNo>0):
       
        iNo=iNo-1
        Display(iNo)#Recursive Call
        print(iNo)

Display(4)





