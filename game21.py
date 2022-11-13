import random

sum=0
cnt=0
current_player=""
current_player_int=random.randint(0,1)
if current_player_int==0:
    current_player  = "human"
else:
    current_player  = "computer"    

while sum<21:
    
    if current_player=="human":
   
        value=int(input("nguoi choi nhap:"))
        while value<1 or value>3:
            value=int(input("moi nguoi choi nhap lai:"))
        sum+=value
        print("tong so diem la:",sum) 
        if sum<21:
            current_player  = "computer"

    else:
        current_player  = "computer"
        value=random.randint(1,3)
        sum+=value
        print("may nhap la:{0} va tong diem la:{1}".format(value,sum))
        if sum<21:
            
            current_player  = "human"
if sum>=21:
    print("nguoi thua la:",current_player)
