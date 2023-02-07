#Parameters passing mechanism
def Area(Radius,PI=3.14):
    Radius = PI* Radius * Radius
    return Radius

def main():

    Rvalue = 10.5
    PIvalue = 3.14
    
    Ans = Area(Rvalue,PIvalue)
    print("Area of circle is :",Ans)

    Ans = Area(Radius =10.5)
    print("Area of circle is :",Ans)

    Ans = Area(PI = 7.14,Radius =10.5)
    print("Area of circle is :",Ans)

if __name__=="__main__"    :
    main()