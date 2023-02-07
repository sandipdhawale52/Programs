def CheckEvenX(No):
    return(No % 2 ==0)

Even = lambda No : No%2==0
ret =Even(112)

iRet = CheckEvenX(12)
if(iRet ==True):
    print("Its Even")
else:
    print("Its odd")
