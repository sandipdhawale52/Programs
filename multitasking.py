import multiprocessing
import threading


def DispalyEven(No):
    for i in range(1,N0,1):
        if(No%2==0):
            print("Even  no:",i)

def Dispalyodd(No):
    for i in range(1,No,1):
        if(No%2!=0):
            print("odd  no:",i)

 def main():
    print("Demonstration of pareallel programming")


    P1=multiprocessing.Thread(target=DispalyEven.args=(number,))
    P2=multiprocessing.Thread(target=Dispalyodd.args=(Number,))
    
    start_time=time.time_strat()
if __name__=="__main__":
    main()
    end_time=time.time_end()