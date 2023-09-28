#problem Statement :  

m1 = 3  # 3 missionary
m2 = 0  # 0 missionary
c1 = 3  # 3 cannibals
c2 = 0  # 0 cannibals

print("Rules are given below : ")

# Rules for from Bank1 to Bank2
print("Rule 1 : 1 missionary 0 cannibals from bank1 -> bank2")
print("Rule 2 : 2 missionary 0 cannibals from bank1 -> bank2")
print("Rule 3 : 1 cannibals + 1 missionary from bank1 -> bank2")
print("Rule 4 : 1 cannibals from bank1 -> bank2")
print("Rule 5 : 2 cannibals from bank1 -> bank2")

# Rules for from Bank2 to Bank1
print("Rule 6 : 1 missionary 0 cannibals from bank2 -> bank1")
print("Rule 7 : 2 missionary 0 cannibals from bank2 -> bank1")
print("Rule 8 : 1 cannibals + 1 missionary from bank2 -> bank1")
print("Rule 9 : 1 cannibals from bank2 -> bank1")
print("Rule 10 : 2 cannibals from bank2 -> bank1")

while (m2 != 3) or (c2 != 3):
    r = int(input("enter your choice : "))

    if (r<1) and (r>10):
        print("Invalid choice")
        break

    # Rule 1
    elif r == 1:
        m1 = m1 - 1
        m2 = m2 + 1

    # Rule 2
    elif r == 2:
        m1 = m1 - 2
        m2 = m2 + 2

    # Rule 3
    elif r == 3:
        m1 = m1 - 1
        m2 = m2 + 1
        c1 = c1 - 1
        c2 = c2 + 1

    # Rule 4
    elif r == 4:
        c1 = c1 - 1
        c2 = c2 + 1

    # Rule 5
    elif r == 5:
        c1 = c1 - 2
        c2 = c2 + 2

    # Rule 6
    elif r == 6:
        m2 = m2 - 1
        m1 = m1 + 1

    # Rule 7
    elif r == 7:
        m2 = m2 - 2
        m1 = m1 + 2

    # Rule 8
    elif r == 8:
        m2 = m2 - 1
        m1 = m1 + 1
        c2 = c2 - 1
        c1 = c1 + 1

    # Rule 9
    elif r == 9:
        c2 = c2 - 1
        c1 = c1 + 1

    # Rule 10
    elif r == 10:
        c2 = c2 - 2
        c1 = c1 + 2

    #end Condition
    elif( m1<c1) or (c2>m2 ):
        print("cannibals ate missionary")
        break
print("Done : \n They Haved Successfully passed the river.",m2,c2)

#5, 9, 5, 9, 2, 8, 2, 9, 5, 9, 5
    