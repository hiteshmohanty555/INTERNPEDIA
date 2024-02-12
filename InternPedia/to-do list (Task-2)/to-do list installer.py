import csv
def install():
    with open("to-do list.csv","w",newline='')as a:
        c=csv.writer(a)
        print("....\n.....\nplease wait installation is going on...\n.......")
        c.writerow(["TASK ID", "TASK", "STATUS","DATE", "TIME"])
        print("Installation successfull...")
        a.close()
        exit()
while True:
    try:
        a=input("Type 'y' or 'Y' to install the software\nType 'n' or 'N' to cancel and exit:")
        if(a=='y'or a=='Y'):
            install()
        elif(a=='n' or a=='N'):
            exit()
    except:
        print("wrong input...\nTry again...")
        continue
