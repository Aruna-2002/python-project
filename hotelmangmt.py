print("WELCOME TO ABC STAR HOTEL")
def starter():
    print("paneertikkadry")
    print("paneeer65")
    print("chicken65")
    print("vegmanchurian")
    print("chillichicken")
def lunchmenu():
    print("meals")
    print("varietyrice")
    print("briyani")
    print("friedrice")
    print("noodles")
def drinks():
    print("rosemilk")
    print("badammilk")
    print("coolcoffee")
    print("dalgonacoffee")
    print("fruit juice")
print("**MENU LIST:**")    
print("^^STARTER^^:") 
starter()
print("^^LUNCHENU:^^")
lunchmenu()
print("^^COOL DRINKS^^")
drinks()
print("PRESS 1 TO ORDER STARTER\nPRESS 2 TO ORDER LUNCH MENU\nPRESS 3 TO ORDER COOL DRINKS")
order=int(input("ENTER YOUR ORDER="))
if order==1:
    print("PLS ORDER YOUR STARTER HERE")
    starter=("paneertikkadry=rs.75\npaneeer65=rs.40\nchicken65=rs.55\nvegmanchurianrs.70\nchillichicken=rs.44")
    print(starter)
    starterorder=input("ENTER YOUR STARTER HERE=").strip()
    if starterorder=="paneertikkadry" :
        count=int(input(f"HOW MANY {starterorder} YOU WANT="))
        paneertikkadry=75*count
        print(f"your bill amount is PANEERTIKKADRY={paneertikkadry}.00\nTOTAL={paneertikkadry}.00")
    elif starterorder=="paneer65" :
        count=int(input(f"HOW MANY {starterorder} YOU WANT="))
        paneer65=40*count
        print(f"your bill amount is PANEER65={paneer65}.00\nTOTAL={paneer65}.00")    
    elif starterorder=="chicken65" :
        count=int(input(f"HOW MANY {starterorder} YOU WANT="))
        chicken65=55*count
        print(f"your bill amount is CHICKEN65={chicken65}.00\nTOTAL={chicken65}.00")
    elif starterorder=="vegmanuchurian" :
        count=int(input(f"HOW MANY {starterorder} YOU WANT="))
        vegmanuchurian=70*count
        print(f"your bill amount is VEGMANUCHUEIAN={vegmanuchurian}.00\nTOTAL={vegmanuchurian}.00")
    elif starterorder=="chillichicken" :
        count=int(input(f"HOW MANY {starterorder} YOU WANT="))
        chillichicken=44*count
        print(f"your bill amount is CHILLICHICKEN={chillichicken}.00\nTOTAL={chillichicken}.00")   
    else:
        print("SRY YOUR ORDER IS NOT AVAILABLE")         
if order==2:
    print("HERE IS LUNCH MENU")
    lunchmenu()
    lunchorder=input("ENTER YOUR LUNCH=")
    if lunchorder=="meals":
        type=input("WHICH MEALS YOU WANT(VEG OR NONVEG)=")
        count=int(input(f"HOW MANY {type} YOU WANT="))
        if type=="veg":
            meals=100*count
            sidedish=45*count
            print(f"sidedish=Rs.{sidedish}.00\nmaindish=Rs.{meals}.00")
            print(f"your ovrall bill amount is {meals+sidedish}.00")
        elif type=="nonveg" or "non veg":
            meals=150*count
            omlette=50*count
            sweet=15*count 
            print(f"meals={meals}.00\nomelette={omlette}.00\nsweet={sweet}.00\ntotal={meals+omlette+sweet}.00")   
    elif lunchorder=="varietyrice":
        
        print("AVAILABLE VARIETY RICE ARE:\nsambar=45\ncurdrice=45\nbrinji=60\ntomatorice=50")
        sambar=45
        curdrice=45
        brinji=60
        tomatorice=50
        varietyorder=input("ENTER THE VARIETY RICE YOU WANT=")
        count=int(input(f"HOW MANY {varietyorder} YOU WANT="))
        if varietyorder=="sambar" or "tomatorice":
            sambar=45*count
            tomatorice=45*count
            sidedish1=10*count
            pickle=5*count
            sidedish=input("WHETHER YOU WANT SIDEDISH OR NOT:")
            if sidedish=="yes":
                print(f"your bill amount is \nmaindish={sambar or tomatorice}.00\nsidedish={sidedish1+pickle}.00\ntotal={(sambar or tomatorice)+sidedish1+pickle}.00")
            else:
                print(f"your over all bill amount\nmaindish={sambar or tomatorice}.00\npickle={pickle}.00\nTOTAL={(sambar or tomatorice)+pickle}.00")        
        if varietyorder=="curdrice":
            curdrice=45*count
            sidedish1=10*count
            sidedish2=10*count
            pickle=5*count 
            sidedish=input("WHETHER YOU WANT SIDEDISH OR NOT:")
            if sidedish=="yes":
               
                count=int(input("ENTER HOW MANY SIDEDISH YOU WANT="))
                if count==1:
                    print(f"your over all bill amount\nsidedish={sidedish1 or sidedish2}.00\npickle={pickle}.00\nmaindish={curdrice}.00\ntotal={(sidedish1 or sidedish2)+pickle+curdrice}.00")
                elif count==2:
                    print(f"your over all bill amount\nsidedish={sidedish1}.00\nsidedish2={sidedish2}.00\npickle={pickle}.00\nmaindish={curdrice}.00\ntotal={sidedish1+sidedish2+pickle+curdrice}.00")
            else:
                print(f"your over all bill amount\nmaindish={curdrice}.00\npickle={pickle}.00\ntotal={curdrice+pickle}.00")  
        elif varietyorder=="brinji":
            count=int(input(f"HOW MANY {lunchorder} YOU WANT"))
            brinji=45*count
            onionraitha=20*count
            extra=input("PLS SELECT WHETHER YOU VEG OR NON VEG SIDEDISH=")
            if extra=="veg":
                gobimanuchurain=45*count
                print(f"maindish={brinji}.00\nonionraitha={onionraitha}.00\ngobimanuchurian={gobimanuchurain}.00\nGRANDTOTAL={brinji+onionraitha+gobimanuchurain}.00")
            elif extra==" nonveg" :
                chicken65=55*count
                print(f"maindish={brinji}.00\nonionraitha={onionraitha}.00\nchicken65={chicken65}.00\nGRANDTOTAL={brinji+onionraitha+chicken65}.00")
    elif lunchorder=="biriyani":
        print("Pls Enter as *chickenbiriyani* *muttonbiriyani* in nextstep")
        type=input("WHICH BIRIYANI YOU WANT(CHICKEN OR MUTTON)=")
        if type=="chickenbiriyani":
            count=int(input(f"HOW MANY {type} YOU WANT="))
            biriyani=120*count
            onionraitha=20*count
            breadhalwa=20*count
            print(f"biriyani={biriyani}.00\nonionraitha={onionraitha}.00\nbreadhalwa={breadhalwa}.00\nTOTAL={biriyani+onionraitha+breadhalwa}.00")
        elif type=="muttonbiriyani":
            count=int(input(f"HOW MANY {type} YOU WANT="))
            biriyani=160*count
            onionraitha=20*count
            breadhalwa=20*count
            print(f"biriyani={biriyani}.00\nonionraitha={onionraitha}.00\nbreadhalwa={breadhalwa}.00\nTOTAL={biriyani+onionraitha+breadhalwa}.00")
    elif lunchorder=="friedrice":
        print("Pls Enter as *chickenfriedrice* *eggfriedrice* in nextstep")
        type=input("WHICH FRIEDRICE YOU WANT(CHICKEN OR EGG):")
        if type=="chickenfriedrice":
            count=int(input(f"HOW MANY {type} YOU WANT="))
            friedrice=100*count 
            onionraitha=20*count
            sauce=10*count
            print(f"firedrice={friedrice}.00\nonionraitha={onionraitha}.00\nsauce={sauce}.00\nTOTAL={friedrice+onionraitha+sauce}.00")
        elif type=="eggfriedrice":
            count=int(input(f"HOW MANY {type} YOU WANT="))
            friedrice=90*count
            onionraitha=20*count
            sauce=10*count
            print(f"firedrice={friedrice}.00\nonionraitha={onionraitha}.00\nsauce={sauce}.00\nTOTAL={friedrice+onionraitha+sauce}.00")
    elif lunchorder=="noodles":
        print("Pls Enter as *chickennoodles* *eggnoodles* *vegnoodles*in nextstep")
        type=input("WHICH NOODLES YOU WANT(CHICKEN OR EGG OR VEG)=")
        if type=="chickennoodles":
            count=int(input(f"HOW MANY {type} YOU WANT="))
            noodles=100*count
            onionraitha=20*count
            sauce=10*count
            print(f"firedrice={noodles}.00\nonionraitha={onionraitha}.00\nsauce={sauce}.00\nTOTAL={noodles+onionraitha+sauce}.00")
        elif type=="eggnoodles":
            count=int(input(f"HOW MANY {type} YOU WANT="))
            noodles=90*count 
            onionraitha=20*count 
            sauce=10*count
            print(f"firedrice={noodles}.00\nonionraitha={onionraitha}.00\nsauce={sauce}.00\nTOTAL={noodles+onionraitha+sauce}.00")
        elif type=="vegnoodles":
            count=int(input(f"HOW MANY {type} YOU WANT="))
            noodles=80*count 
            onionraitha=20*count 
            sauce=10*count
            print(f"firedrice={noodles}.00\nonionraitha={onionraitha}.00\nsauce={sauce}.00\nTOTAL={noodles+onionraitha+sauce}.00")
if order==3:
    drinks()
    liquiditem=input("ENTER YOUR ORDER=")
    if liquiditem=="rosemilk":
        count=int(input(f"HOW MANY {liquiditem} YOU WANT= "))
        rosemilk=30*count
        print(f"your bill amount is ROSEMILK={rosemilk}.00")
    if liquiditem=="badammilk":
        print("1.HOT BADAMMILK\n2.COOL BADAMMLK")
        print("PRESS 1 FOR HOTBADAM MILK\n2.PRESS 2 FOR COOL BADAM MILK")
        type=int(input("ENTER THE TYPE OF BADAMMILK YOU WANT="))
        if type==1:
            count=int(input("HOW MANY HOTBADAMMILK YOU WANT= "))
            hotbadammilk=45*count
            print(f"your bill amount is  HOTBADAMMILK={hotbadammilk}.00") 
        elif type==2:
            count=int(input("HOW MANY COOLBADAMMILK YOU WANT= "))
            coolbadammilk=45*count
            print(f"your bill amount is {coolbadammilk}.00")    
    if liquiditem=="coolcoffee":
        count=int(input(f"HOW MANY {liquiditem} YOU WANT= "))
        coolcoffee=30*count
        print(f"your bill amount is COOLCOFFEE={coolcoffee}.00")
    if liquiditem=="dalgonacoffee":
        count=int(input(f"HOW MANY {liquiditem} YOU WANT= "))
        dalgonacoffee=30*count
        print(f"your bill amount is DALGONA={dalgonacoffee}.00")
    if liquiditem=="fruitjuice":
        fruitjuice=("apple juice", "pomogrante juice", "orange juice", "mango juice", "grape juice") 
        for i in fruitjuice:
            print(i)
        fruitjuice=input("ENTER YOUR ORDER=")    
        if fruitjuice=="applejuice":
            count=int(input(f" HOW MANY {fruitjuice} YOU WANT="))   
            applejuice=50*count
            print(f"bill amount AJ={applejuice}.00")
        if fruitjuice=="pomograntejuice":
            count=int(input(f" HOW MANY {fruitjuice} YOU WANT="))   
            pomograntejuice=50*count
            print(f"bill amountPJ={pomograntejuice}.00") 
        if fruitjuice=="orangejuice":
            count=int(input(f" HOW MANY {fruitjuice} YOU WANT="))   
            orangejuice=50*count
            print(f"bill amountOJ={orangejuice}.00")    
        if fruitjuice=="mangojuice":
            count=int(input(f" HOW MANY {fruitjuice} YOU WANT="))   
            mangojuice=60*count
            print(f"bill amountMJ={mangojuice}.00")       
        if fruitjuice=="grapejuice":
            count=int(input(f" HOW MANY {fruitjuice} YOU WANT="))   
            grapejuice=40*count
            print(f"bill amount GJ={grapejuice}.00") 
print("********************THANKS FOR CHOOSING US**************************")        
print("*****************HAVE A NICE DAY*******************")       
                      


            
            

        
       






