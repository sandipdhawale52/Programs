
def Display(iNo):
    iCnt=0
    if(iNo>0):
        print(iNo)
        iNo=iNo-1
        Display(iNo)#Recursive Call

Display(4)





