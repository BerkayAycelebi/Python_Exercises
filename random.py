import random as rd


x=rd.random()
print(x)

y=rd.uniform(4,8)
print(y)

c=rd.randint(10,20)
print(c)

list=["Ahmed","Mahmed","Gizem","Merve","Elif","Melike"]
z=rd.choice(list)
print(z)


rd.shuffle(list)
for t in list:
    print(t)
print(rd.sample(list,3))



