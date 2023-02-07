from operator import truediv


def CheckEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False

def CheckEvenX(no):
    return(no % 2 ==0)

iRet = CheckEven(12)
if(iRet ==True):
    print("Its Even")
else:
    print("Its odd")






