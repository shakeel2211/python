# lecture no 29 delete element from list
# del()
y = [ 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 ]
del y[2]
print(y)

# pop()
y = [ 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 ]
y.pop(3)
print(y)

# remove()
y = [ 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 ]
y.remove(60)
print(y)

# clear()
y = [ 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 ]
y.clear()
print(y)

# update()
z = [ 10,20,30,40,50,60,70,80,90 ]
z[3] = 45
print(z)

# insert()
z = [ 10,20,30,40,50,60,70,80,90 ]
z.insert(3,10)
print(z)

# append()
z = [ 10,20,30,40,50,60,70,80,90 ]
z.append(100)
print(z)

# extends()
y = [40,50,60,]
z = [70,80,90,100]
y.extend(z)
print(y)
