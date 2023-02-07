def main():
    try:
        print("Enter first no")
        No1=int(input())

        print("Enter second no")
        No2=int(input())

        Ans=No1/No2
        print("Division is",Ans)

    except ZeroDivisionError:
        print("Exception occouredInside Divison Error")

    except ValueError:
        print("Inside value error")
    finally:
        print("Inside finally block")   
if __name__=="__main__":
            main()