print("<><><><><><>WELCOME HAPPY JOURNEY TRAVELS ONLINE TICKET BOOKING<><><><><><>")
print("WEE ARE PROVIDING BUS ONLINE TICKET BOOKING SERVICE")
firstservice=("<><>TRAVELS<><>:","1.BUS")
for i in firstservice:
    print(i)
# RULES FOR BOOKING THE TICKET IN MENTIONED IN CLASS 
    class roadways():
        def bus(self):
            print("*WELCOME TO HAPPY JOURNEY BUS TICKET BOOKING SERVICE")
            print("**MENTION YOUR ORGIN AND DESTINATION CORRECTLY")
            print("***GIVE THE VALID ID PROOF")
            print("****PAN CARD ISSUED BY TH INCOME TAX DEPARTMENT IS MANDATORY")
travel=input("give *YES* to book ticket=").upper()
if travel=="YES":
    obj=roadways()
    obj.bus()
    print("WE ARE RUN THE BOTH AC AND NON-AC BUS FROM THE CHENNAI TO BELOW MENTIONED CITIES:")
    cities=("*VELLORE*\n*MADURAI*\n*TIRUNELVELI*\n*COIMBATORE*")
    print(cities)
    to=input("ENTER YOUR DESTINATION FROM CHENNAI:").upper()
    if to=="TIRUNELVELI":
        
        print("TICKET PRICE FROM CHENNAI TO TIRUNELVELI FOR PER PERSON IS RS.900.00")
        
        print("Enter 1 To book the ticket: ")
        type=int(input("press 1:"))
        if type==1:
            count=int(input("HOW MANY SEATS YOU NEED TO BOOK:"))
            import calendar
            date=int(input("ENTER THE DATE:"))
            month=int(input("ENTER THE MONTH(IN NUMBER):"))
            time=(calendar.month(date,month))
            fair=1200*count
            foodcharge=150*count
            sts=input("Give *CONFIRM* to book ticket:")
            if sts=="confirm":
                ret=input("Give *YES* to bookk return ticket:")
                if ret=="yes":
                    print(f"pay your amount Rs.{fair*2 + foodcharge*2}.00")
                    payment=input("Enter the payment sts(*y for yes* *n for no*):")
                    if payment=="y":
                        import calendar
                        date1=int(input("ENTER THE RETURN DATE:"))
                        month1=int(input("ENTER THE MONTH(IN NUMBER):"))
                        time=(calendar.month(date,month))
                        print(f"YOUR TICKET IS BOOKED ON {date}/{month}/2022 AND RETURN TICKET IS BOOKED ON {date1}/{month1}/2022")
                        print(f"YOUR SEATS ARE ALOTED ON {date}/{month} and {date1}/{month}/2022")
                    else:
                        print("PLS PAY YOUR AMOUNT")
                elif ret=="no":         
                    print(f"you need to pay {fair + foodcharge }")
                    payment=input("Enter the payment sts(*y for yes* *n for no*):")
                    if payment=="y":
                        print(f"YOUR TICKET IS BOOKED ON {date}/{month}/2022")
                        print(f"YOUR SEATS ARE ALOTED ON {date}/{month}/2022")
                    else:
                        print("PLS PAY YOUR AMOUNT")
            else:
                print("PLS CONFIRM YOUR TICKET")
    elif to=="VELLORE":
        
            print("TICKET PRICE FROM CHENNAI TO VELLORE FOR PER PERSON IS RS.500.00")
            
            print("Enter 1 To book the ticket: ")
            type=int(input("press 1:"))
            if type==1:
                count=int(input("HOW MANY SEATS YOU NEED TO BOOK:"))
                import calendar 
                date=int(input("ENTER THE DATE:"))
                month=int(input("ENTER THE MONTH(IN NUMBER):"))
                time=(calendar.month(date,month))
                fair=500*count
                waterbottle=20*count
                sts=input("Give *CONFIRM* to book ticket:")
                if sts=="confirm":
                    ret=input("Give *YES to book return ticket:")
                    if ret=="yes":
                        print(f"pay your amount Rs.{fair*2 + waterbottle*2}.00")
                        payment=input("Enter the payment sts(*y for yes* *n for no*):")
                        if payment=="y":
                            import calendar
                            date1=int(input("ENTER THE RETURN DATE:"))
                            month1=int(input("ENTER THE MONTH(IN NUMBER):"))
                            time=(calendar.month(date,month))
                            print(f"YOUR TICKET IS BOOKED ON {date}/{month}/2022 AND RETURN TICKET IS BOOKED ON {date1}/{month1}/2022")
                            print(f"YOUR SEATS ARE ALOTED ON {date}/{month} and {date1}/{month}/2022")
                        else:
                            print("PLS PAY YOUR AMOUNT")
                    elif ret=="no":         
                        print(f"you need to pay {fair + waterbottle }")
                        payment=input("Enter the payment sts(y for yes* *n for no*):")
                        if payment=="y":
                            print(f"YOUR TICKET IS BOOKED ON {date}/{month}/2022")
                            print(f"YOUR SEATS ARE ALOTED ON {date}/{month}")
                        else:
                            print("PLS PAY YOUR AMOUNT")
                else:
                    print("PLS CONFIRM YOUR TICKET")  
    elif to=="MADURAI":
        
            print("TICKET PRICE FROM CHENNAI TO MADURAI FOR PER PERSON IS RS.800.00")
            
            print("Enter 1 To book the ticket: ")
            type=int(input("press 1:"))
            if type==1:
                count=int(input("HOW MANY SEATS YOU NEED TO BOOK:"))
                import calendar 
                date=int(input("ENTER THE DATE:"))
                month=int(input("ENTER THE MONTH(IN NUMBER):"))
                time=(calendar.month(date,month))
                fair=800*count
                food=120*count
                sts=input("Give *CONFIRM* to book ticket:")
                if sts=="confirm":
                    ret=input("Give *YES* to book return ticket:")
                    if ret=="yes":
                        print(f"pay your amount Rs.{fair*2 + food*2}.00")
                        payment=input("Enter the payment sts(*y for yes* *n for no*):")
                        if payment=="y":
                            import calendar
                            date1=int(input("ENTER THE RETURN DATE:"))
                            month1=int(input("ENTER THE MONTH(IN NUMBER):"))
                            time=(calendar.month(date,month))
                            print(f"YOUR TICKET IS BOOKED ON {date}/{month}/2022 AND RETURN TICKET IS BOOKED ON {date1}/{month1}/2022")
                            print(f"YOUR SEATS ARE ALOTED ON {date}/{month} and {date1}/{month}/2022")
                        else:
                            print("PLS PAY YOUR AMOUNT")
                    elif ret=="no":         
                        print(f"you need to pay {fair + food }")
                        payment=input("Enter the payment sts(y for yes* *n for no*):")
                        if payment=="y":
                            print(f"YOUR TICKET IS BOOKED ON {date}/{month}/2022")
                            print(f"YOUR SEATS ARE ALOTED ON {date}/{month}")
                        else:
                            print("PLS PAY YOUR AMOUNT")
                else:
                    print("PLS CONFIRM YOUR TICKET")                        
    elif to=="COIMBATORE":
        
            print("TICKET PRICE FROM CHENNAI TO COIMBATOE FOR PER PERSON IS RS.800.00")
            
            print("Enter 1 To book the ticket: ")
            type=int(input("press 1:"))
            if type==1:
                count=int(input("HOW MANY SEATS YOU NEED TO BOOK:"))
                import calendar 
                date=int(input("ENTER THE DATE:"))
                month=int(input("ENTER THE MONTH(IN NUMBER):"))
                time=(calendar.month(date,month))
                fair=800*count
                waterbottle=20*count
                sts=input("Give *CONFIRM* to book ticket:")
                if sts=="confirm":
                    ret=input("Give *YES* to book return ticket:")
                    if ret=="yes":
                        print(f"pay your amount Rs.{fair*2 + waterbottle*2}.00")
                        payment=input("Enter the payment sts(*y for yes* *n for no*):")
                        if payment=="y":
                            import calendar
                            date1=int(input("ENTER THE RETURN DATE:"))
                            month1=int(input("ENTER THE MONTH(IN NUMBER):"))
                            time=(calendar.month(date,month))
                            print(f"YOUR TICKET IS BOOKED ON {date}/{month}/2022 AND RETURN TICKET IS BOOKED ON {date1}/{month1}/2022")
                            print(f"YOUR SEATS ARE ALOTED ON {date}/{month} and {date1}/{month}/2022")
                        else:
                            print("PLS PAY YOUR AMOUNT")
                    elif ret=="no":         
                        print(f"you need to pay {fair + waterbottle }")
                        payment=input("Enter the payment sts(y for yes* *n for no*):")
                        if payment=="y":
                            print(f"YOUR TICKET IS BOOKED ON {date}/{month}/2022")
                            print(f"YOUR SEATS ARE ALOTED ON {date}/{month}")
                        else:
                            print("PLS PAY YOUR AMOUNT")
                else:
                    print("PLS CONFIRM YOUR TICKET")                      
        