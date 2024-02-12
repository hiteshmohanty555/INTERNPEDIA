def calculate():
    total=0
    def add(total,a,b,c):        
        total=total+c
        return total
    def sub(total,a,b,c):
        total=total-c
        return total 
    def multi(total,a,b,c):
        total=total*c
        return total
    def div(total,a,b,c):
        total=total/c
        return total  

    print("=======================================WELCOME=============================================\n======================================CALCULATOR=========================================")
    print("Instructions:-\n1. first enter a number\n2. Then enter a operator to perform the specific mathematical operations\n3. Then enter the another number\n4. In total you will get the total\n5. type e in the operator section to exit\n6. Type 'c' to reset the total to 0")
    
    choice=int(input("Do you want to continue or exit\npress 1 to continue or 2 exit:"))
    if(choice==1):
        print("total=",total)
        a=float(input("enter a num:"))
        total=a
        
        while True:
            
            try:
                b=input("enter the operator (+,-,*,/,e,c):")
                
                if(b=='+'):
                    c=float(input("enter another num:"))
                    total=add(total,a,b,c)
                    print("total=",total)
                elif(b=='-'):
                    c=float(input("enter another num:"))
                    total=sub(total,a,b,c)
                    print("total=",total)
                elif(b=='*'):
                    c=float(input("enter another num:"))
                    total=multi(total,a,b,c)
                    print("total=",total)
                elif(b=='/'):
                    c=float(input("enter another num:"))
                    total=div(total,a,b,c)
                    print("total=",total)
                elif(b=="c"):
                    
                    total=0
                    print("total=",total)
                elif(b=='e'):
                    print("Thank you come again next time...")
                    exit()
            except:
                print("wrong operator...\nEnter valid operator")
                continue
    elif(choice==2):
        exit()
    else:
        print("wrong input\nTry again")
    calculate()            


calculate()
