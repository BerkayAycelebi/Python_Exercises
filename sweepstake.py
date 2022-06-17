import random
import time

users=[]

def userAdd(x):
    print("-"*30)
    print("User Adding Screen")
    user=input("Please enter a user name ")
    users.append(user)
    input("Please enter for keep to contunie")

def userSee(x):
    counter=1
    print(""*30)
    for i in x:
        print(str(counter)+"User Name:",i)
        counter+=1
    print(""*30)
    input("Please enter for keep to contunie")

def choose(x):
    print(""*30)
    cnt=1
    chooseUser=int(input("How many user do u want choose?"))
    random_choose=random.sample(users,chooseUser)
    for i in random_choose:
        print(str(cnt)+"User Name:",i)
        cnt+=1
    print(""*30)
    input("Please enter for keep to contunie")
def ShuffleUser(x):
    print(""*30)
    cnt=1
    random.shuffle(x)
    for i in x:
        print(str(cnt)+"User Name:",i)
        cnt+=1
    print(""*30)
    input("Please enter for keep to contunie")

while True:
    print("****Welcome to SweepStake")
    choosing=int(input("1-User Add\n2-Look At User\n3-Shuffle to User\n4-Choose Randomly"))

    if choosing==1:
        userAdd(users)
    elif choosing==2:
        userSee(users)
    elif choosing==3:
        ShuffleUser(users)
    elif choosing==4:
        print("User choosing getting ready")
        time.sleep(2)
        choose(users)
    else:
        print("Please choose correctly")







