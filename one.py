# lec no 27 What is List Iteration in Python.

u = [10,20,30,40,50,60,70,80,90] # sab say phely hum list lay gay.
v = len(u)    # length get kare gay
for a in range(v):  # for loop use kare gay.
    print(u[a])     # print kare gay.
    
    
    # for loop ko reverse kase karna hai.
u = [10,20,30,40,50,60,70,80,90] # sab say phely hum list lay gay.
v = len(u)    # length get kare gay
for a in range(v-1,-1,-1):
    print(u[a])