phone ={}

def Phone_No_Add(x):
    print("***PHONE NO ADDING PART***")
    name=input("Please enter a name")
    phone_no=input("Please enter a phone number")
    x=phone.setdefault(name,phone_no)
    print(f"{name}, adlı kişi telefon rehberine eklendi")

def Phone_Show(x):
    name_count=len(x)
    print(f"Name of count on your directory is {name_count}")
    print("Welcome to Phone Directory")
    for i,j in x.items():
        print(i,":",j)
def Phone_No_Delete(x):
    print("***Delete page***")
    delete_name=input("Please enter a name you want delete")
    x=phone.pop(delete_name)

while True:
    print("**WELCOME***")
    print("***Please make choose***")
    make_choose=int(input("1-Add\n2-Delete\n3-See Directory"))
    
    if(make_choose==1):
        Phone_No_Add(phone)
    elif(make_choose==2):
        Phone_No_Delete(phone)
    elif make_choose==3:
        Phone_Show(phone)
    else:
        print("Please enter correct key")
