# lecture no 28 list comprehension in python.

p = []
for a in range(1,101): # for loop ka use 
    p.append(a)    # normal formula append() function say
    
    print(p)
    
    
    a = [ b for b in  range(1,101) if b%2==0 ] # for loop ka use hoga or pher filter ka formula use ho gaa  (if b%2==0) .or wo formula niklne gaa jo 2 py divide ho gaa.
    print(a) # is main list comprehension ka kiya hai.
    
    s = "hello kamoka" # list comprehension example no 2.
    t = [u for u in s]
    print(t)