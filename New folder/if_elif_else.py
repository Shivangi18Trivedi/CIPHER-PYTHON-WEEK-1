age = input("please input your age")
age = int(age)
if age==0 or age <0:
    print("you can't watch")
elif 0<age<=3:
    print("Ticket price :free")    
elif 10<age<=60:
        print("ticket price : 250")
else:
    print("Ticket price : 200")        

