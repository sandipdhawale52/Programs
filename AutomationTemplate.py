
from sys import * 

def Script_Task(No):
    if(No%2==0):
        print("It is even no")
    else:
        print("is it Not even no")


def main():
    print("-----------------Marvellous Infosystem Automation----------")

    print("Automation script started with name:",argv[0])

    if(len(argv)!=2):
        print("Error : Insufficient Arguments")
        print("Use -h for help ans use -u for usage of script")
        exit()

    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("Help: This script is used to perform_________________")
        exit()


    elif((argv[1]=="-u") or (argv[1]=="U")):
        print("Usage : provide ____ number of arumnets")
        print("First argument as:________")
        print("Second argument as:_______")
        exit()

    else:
        
        Script_Task(int(argv[1]==1))
        print("odd")
        exit()

if __name__=="__main__":
    main()