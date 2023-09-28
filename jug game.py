x = int(input("Enter the A jug capacity : "))
y = int(input("Enter the B jug capacity : "))
ai=int(input("Initially Water in Jug A: "))
bi=int(input("Initially Water in Jug B: "))
xf = int(input("Enter the final value of x glass : "))
yf = int(input("Enter the final value of y glass : "))
Rno = print("the rules are")

while ((x!=xf and y!=yf)):
    Rno = int(print("the rules are"))
    if Rno == 1 :
        if x < 4 :
            x = 4
    if Rno == 2 :
        if y < 3 :
            y = 3
    if Rno == 3 :
        if x > 0 :
            x = 0
    if Rno == 4 :
         if y > 0 :
           y = 0
    if Rno == 5 :
      if (x + y) >= 4 and y > 0 :
          x = 4
          y = y - (x - 3)
    if Rno == 6 :
         if (x + y) >= 4 and x > 0 :
             y = 3
             x = x - (3 - y)
    if Rno == 7 :
        if (x + y) <= 4 and y > 0 :
             x = x + y
             y = 0
    if Rno == 8 :
       if (x + y) <= 3 and x > 0 :
            x= 0
            y = x + y
    
 

print("this is the answer : ","(",xf,yf,")")