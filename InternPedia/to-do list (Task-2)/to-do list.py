import csv
import datetime
from datetime import date
from datetime import datetime
import random
print("==================================WELCOME================================")
print("--------------------------------------------------------------------------")
print("=================================TO-DO LIST==============================")
def create_record(task, status):
    with open("to-do list.csv","a",newline='')as a:
        c=csv.writer(a)       
        date1=date.today()
        y=datetime.now()
        time=y.strftime("%H:%M:%S")
        sl_no=random.randint(101,9999)
        rec=[sl_no, task, status, date1, time]
        print(".....\n.....\n....")
        c.writerow(rec)
        print("Task has been added to the list successfully....")
        a.close()
def show_record():
    with open("to-do list.csv",'r')as a:
        c=csv.reader(a)
        
        for row in c:
            print(row)
        print("This much task is present in the list.....")
        a.close()
def update():
    L = []
    found = False

    with open("D:\\InternPedia\\to-do list\\to-do list.csv", 'r') as a:
        c = csv.reader(a)
        
        choice = input("Enter the sl.no of the task whose status you want to update:")

        for row in c:
            if row[0] == choice:
                found = True
                t = row[1]
                print("TASK:", t)
                s = input("update status:")
                row[2] = s
            L.append(row)

        if found == False:
            print("No such task found with the task id....")
        else:
            with open("D:\\InternPedia\\to-do list\\to-do list.csv", 'w', newline='') as a:
                e = csv.writer(a)
                e.writerows(L)

    print("Status updated successfully...\nUpdated status is...")

    with open("D:\\InternPedia\\to-do list\\to-do list.csv", 'r') as a:
        R = csv.reader(a)
        for row in R:
            print(row)

    
def options():
    while True:
        try:
            b=int(input("press 1 to add new task to the list\npress 2 to view the task and its status from the list\npress 3 to update the status of the task\npress 4 to exit:"))
            if(b==1):
                print(".....\n......\nAdd new task")
                task=input("TASK:")
                status=input("STATUS:")
                create_record(task, status)
            elif(b==2):
                print(".....\n......\nShowing the task list")
                show_record()
            elif(b==3):
                print("UPDATION")
                update()
            elif(b==4):
                print("Thank you visit again\ngood bye\nsee you again...")
                exit()
        except:
            print("wrong input\nenter valid input and try again....")
            continue
options()       
        

        
            
            
              
        
