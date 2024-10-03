items={1:"Tea",2:"Poha",3:"Paratha",4:"Vada-pav",5:"Dosa",6:"Idali",7:"Coffe",8:"Pavbhaji"}
#var[key]
price={1:10,2:20,3:15,4:15,5:30,6:35,7:80,8:60}
ik=[]
qun=[]
print("-"*100)
print(f'{" "*40} Ronak Hotel')
print("-"*100)
while True:
    print("""
                Menu
        1.Tea     2.Poha
        3.Paratha  4.Vada-Pav
        5.Dosa    6.idali
        7.Coffe   8.Pavbhaji
    """)
    i=int(input("Enter Your Choice: "))
    q=int(input("Enter Quantity: "))
    ik.append(i)
    qun.append(q)
    ch=input("Do You Want To Continue: ")
    if ch=="n":
        print("-"*85)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("ItemName","Quantity","Price","Amount"))
        print("-"*85)
        sum=0
        for i in range(len(ik)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(items[ik[i]],qun[i],price[ik[i]],qun[i]*price[ik[i]]))
            print("-"*85)
            sum=sum+qun[i]*price[ik[i]]
        print(f"Your Total Amount:{sum}\nThank You!Visit Again")
        break
    
