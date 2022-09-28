#print("~~~~~~~WELCOME TO SIB ATM~~~~~~~")
print("1.BALANCE ENQUIRY    2.CASH WITHDRAWL\n3.MINISTATEMENT      4.TRANSFER\n        5.PIN GENERATE")
option=int(input("Enter the <OPTION> you want:"))

if option==1:
    name=input("ENTER YOUR NAME:")
    acc_no=int(input("ENTER YOUR ACCOUNT NUMBER="))
    pin=int(input("ENTER YOUR FOUR DIGIT PIN:"))
    p="pin"
    if p=="pin":
        print("successfully logged in...... ")
        import random
        a=random.randint(100,1000000)
        print("                           ")
        print(f"**YOUR ACC BALANCE RS.{a}.00**")
elif option==2:
    print("WELCOME")
    print("PLS INSERT YOUR ATM CARD")
    pin=int(input("ENTER YOUR FOUR DIGIT PIN:"))
    p="pin"
    if p=="pin":
        print("click *CONTINUE*:")
        amt=int(input("ENTER THE AMOUNT="))
        if amt<=10000:
            choice=3
            while choice>3:
                print("s")
                if choice==3:
                    break
                print("you have no more chances")
                choice=choice+1



        import random
        a=random.randint(500,99999)#minimum balance in the acc will be not less than 500 
        if amt<=10000:
            print("pls wait......\n") 
            rec=input("do you want receipt(*y* for yes *n* for no):")  
            if rec=="y":
                print("COLLECT YOUR CASH AND RECEIPT")
                import datetime
                time=datetime.datetime.now()
                import random
                b=random.randint(1000,9999)
                print("|-----------------------------------------|")
                print("|                                         |")
                print("|         welcome to sib atm              |")
                print("|                                         |")
                print("|-----------------------------------------|")
                print("|                                         |")
                print(f"|DATE AND TIME:{time} |") 
                print("|                                         |")
                print("|-----------------------------------------|")
                print(f"|transction=withdrawal                    |")
                print(f"|acc_num=                    *********{b}|")
                print(f"|available balance=    Rs.{a-amt}.00        |")
                print("|-----------------------------------------|")
                print("|     THANKS FOR CHOOSING US\n       !!!VISIT AGAIN!!!")
                print("|-----------------------------------------|")
                print("COLLECT YOUR CARD")
            elif rec=="n":
                print("COLLECT YOUR CASH")
                print(      "THANKS FOR CHOOSING US\n!!!        VISIT AGAIN!!!")
                print("COLLECT YOUR CARD")
        elif amt>=10001:
            print("Sry only Rs.10000 will be withdrawl in one time")        
elif option==3:
    name=input("ENTER YOUR NAME:")
    acc_no=int(input("ENTER YOUR 9 DIGIT ACCOUNT NUMBER="))
    a="acc_no"
    if a=="acc_no":
        print("welcome")
        print("YOU WILL RECEIVE THE 5 TRANSACTION FROM THE DATE U GIVEN")
        import calendar
        date=int(input("ENTER THE DATE FROM YOU WANT THE HISTORY:"))
        month=int(input("ENTER THE MONTH(IN NUMBER):"))
        time=(calendar.month(date,month))
        import random
        c=random.randint(100,9999)
        import datetime
        time=datetime.datetime.now()
        print("|-----------------------------------------|")
        print("|                                         |")
        print("|         welcome to sib atm              |")
        print("|                                         |")
        print("|-----------------------------------------|")
        print("|                                         |")
        print(f"|DATE AND TIME:{time} |") 
        print("|                                         |")
        print("|-----------------------------------------|")
        print(f"|{date}/{month}/2022---------RS.{c}.00              |")
        print(f"|{date+6}/{month}/2022---------RS.{c+560}.00              |")
        print(f"|{date}/{month+1}/2022---------RS.{c-654}.00              |")
        print(f"|{date+3}/{month+1}/2022---------RS.{c+560}.00              |")
        print(f"|{date}/{month+1}/2022---------RS.{c-654}.00              |")
        print("|-----------------------------------------|")
        print(      "THANKS FOR CHOOSING US\n!!!        VISIT AGAIN!!!")
        print("COLLECT YOUR CARD")
elif option==4:
    print("INSERT YOUR ATM CARD")
    pin=int(input("ENTER YOUR FOUR DIGIT PIN:"))
    p="pin"
    if p=="pin":
        amt=int(input("ENTER THE AMOUNT YOU NEED TO TRANSFER:"))

        if amt<=50000:
            acc_no=int(input("ENTER YOUR ACCOUNT NUMBER OF RECEIVER="))
            a="acc_no"
            if a=="acc_no":
                print("click *CONTINUE*:")
                print("SUCCESSFULLY TRANSFERRED")
                import random
                a=random.randint(100,99999)
                print(f"your account balance is {a-amt}")
        elif amt>=50000:
            print("ONLY YOU CAN TRANSFER A RS.50000 PER DAY")        
elif option==5:
    print("INSERT YOUR DEBIT CARD IN ATM")
    print("***ENTER 11 DIGIT ACCOUNT NUMBER & PRESS 'CONFIRM'***")
    acc=int(input("ENTER YOUR ACC.NUMBER="))
    con=input("Press 'CONFIRM':")
    a="acc"
    if a=="acc":
        print("***Enter the 'REGISTERED MOBILE NUMBER'& press 'CONFIRM'***")
        mob=int(input("Enter your 'REGISTERED MOBILE NUMBER'="))
        con=input("Press 'CONFIRM':")
        print("***YOU WILL RECEIVE A OTP TO YOUR REGISTERED MOBILE NUMBER***")
        print("***Remove and re-insert the ATM card***")
        print("***click 'BANKING'***")
        opt=input("Give 'BANKING'")
        if opt=="banking":
            print("Enter the otp you received:")
            otp=int(input("Enter the otp="))
            p="otp"
            if p=="otp":
                print("***choose'Select transaction > PIN change'***")
                tran=input("Give ''TRANSACTION':")
                chn=input("Give 'PIN change':")
                pin=int(input("Enter 4-digit PIN of your choice:"))
                new="pin"
                if new=="pin":
                    re=int(input("Re-enter the otp to confirm PIN:"))
                    new="re"
                    if new=="re":
                        print("SUCCESSFULLY UPDATED YOUR PIN")
        else:
            print("pls select banking")
print("""
    -------------------------------------
   |        Thanks for choosing us       |
   |           !Visit us again!          |
    -------------------------------------
        """)
