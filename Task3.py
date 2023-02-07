
import schedule 
import time
import datetime
import sys


def Task_Hour():
    print("Task ased on minutes  scheduled",datetime.datetime.now())

def Task_Day():
    print("Task ased on day scheduled",datetime.datetime.now())

def Task_Minutes(Cnt=4):
    print("Task ased on minutes scheduled",datetime.datetime.now())
    sys.exit()
def main():
    print("Inside task schedular")
    print("Current time is:",datetime.datetime.now())


    schedule.every(1).minutes.do(Task_Minutes(Cnt=+1))
    schedule.every(1).hour.do(Task_Hour)
    schedule.every().saturday.at("18:00").do(Task_Day)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()