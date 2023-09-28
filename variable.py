
   # varibales are Case Sensitive in Python. 
   # No need to declare the datatype of the variable in python
   # if we want to set the datatype of the variable we need to typecast the variable.
   # String will be allow in both case , single quote as well as double quotes.
x = 5  # int
y = "Hello" # str
X = 'By' # str
Y = 10 #int
x = str('15') #str 


""" get the type of the variable """
print(type(x))
print(type(X))
print(type(y))
print(type(Y))

""" Namin Convention"""
   
   # camel Case : only first leter is small of the first word.
   # Pascal Case : all first letter in word is in captial case.
   # Snake case : word in small case with each underscore sepration.

""" Assign Multiple value to the variable """
 
p,q,r = "Welcome",10,12.50
print(p) # welcome
print(q) # 10
print(r) # 12.50

""" Assign Same value to multiple variable """

s = t = u = "Python"
print(s) # python
print(t) # python
print(u) # python


""" unpack the value for the variable """

fruit = ["Mouse","keyboard","Monitor"]
m,n,o = fruit
print(m) # Mouse
print(n) # Keyboard
print(o) # Monitor

"""Local Variable"""

x = "Awesome" # global variable

def myFun(): # function body start

    x = "fantastic" # local variable
    print("Python is "+ x) #fantastic
    # function body end

myFun() # function calling

print("Python is "+ x) # awesome

""" Make the local variable global using the 'global' keyword"""

def globalVar():
  global x 
  x = "Fantastic"
  print("Python is " + x)
globalVar()

print("Local Variable access : Python is "+ x )