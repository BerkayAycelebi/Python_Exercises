from cmath import pi
from tkinter import Y


name="Ahmed"
Birth_Year=1993
Current_Year=2022
Calculate_Age=Current_Year-Birth_Year
print(name,"in yaşı",Calculate_Age,"Doğum Yılı",Birth_Year)
print(name,"in yaşı"+" "+str(Calculate_Age))

x="Tenseflow"
y="Keras"
z=y*5
t=x+y
print(z," ",t)

UpperCase="tensorflow and Keras"
print(UpperCase.upper())
LowerCase="tTENSORFLOW and KERAS"
print(UpperCase.lower())

Capitalize="tensorflow and Keras"
print(Capitalize.capitalize())

swap="tensorflow and Keras"
print(swap.swapcase())

delete="++Python".strip("+")
print(delete)

name="Ahmed"
surname="Uğur"
Age=29
print("Kişinin adı: {} \n Kişinin soyadı {} \n Kişinin yaşı {}".format(name,surname,Age))
print(f"Kişinin adı: {name} \n Kişinin soyadı {surname} \n Kişinin yaşı {Age}")

username=input("Pelase enter username")
password=input("Please enter password")