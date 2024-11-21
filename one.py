   # simple calculator 
print('''     
      + Add
      - Subtrack
      * Multiply
      / Divide
      ''') # calculator k liye yee sab print kare gay
num1 = int(input("Enter the value1:-")) # input ki value 1 aye gee
num2 = int(input("Enter the value2:-")) # input ki value 2 aye gee
opr = input("Enter the Opr..(+ , - , * , / )") # ye input lay gay simble bnane k liye
if opr == "+":  # if opr ka simble == + k braber hai to yee print aye gaa.
    print(num1+num2)
elif opr == "-": # if opr ka simble == - ka braber hai to yee print aye gaa.
    print(num1 - num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":
    print(num1 / num2)
else:       # else mean ager kuch bhi nahi to invalid opr.. print aye gaa
    print("invalid opr...")
