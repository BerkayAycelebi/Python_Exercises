from typing import final


midtem_grade=int(input("Enter a midtem grade"))
final_grade=int(input("Enter a final grade"))
average=midtem_grade*0.4+final_grade*0.6

if average>=85:
    print("AA")
elif average >=65:
    print("BB")
elif average>=50:
    print("CC")
else:
    print("You are Fail")