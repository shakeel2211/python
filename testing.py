
# Lecture no 14 Data type in python
a=5
print(a,type(a))  # int


a=5.5
print(a,type(a))   # float


a= 2+5j
print(a,type(a))   # complex


a= "hello"
print(a,type(a))   # string


a= [10,20,30,"ws"]
print(a , type(a))   #  list


a=(19,20,"hello")
print(a, type(a))    #  tuple


d={
   "course_name" : "python" ,      # directory
   "course_duration" : "2 Month"  
   }
print(d["course_name"])
print(d["course_duration"])
print(d,type(d))


s= { 20,40,50,60}
print(s,type(s))    # set
