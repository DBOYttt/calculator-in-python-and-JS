print("HI im calculator maked by D-BOY")

print('''
Choose what you want to do
1 - Add
2 - Subtract
3 - Divide
4 - Multiply
5 - Spoteng
''')

a = int(input("Choose: "))

if a == 1: 
    b = int(input("Number 1: "))
    c = int(input("Number 2: "))
    print("the result is : " + str(b + c))
elif a == 2:
    b = int(input("Number 1: "))
    c = int(input("Number 2: "))
    print("the result is: " + str(b - c))
elif a == 3:
    b = int(input("Number 1: "))
    c = int(input("Number 2: "))
    print("the result is: " + str(int(b / c)))
elif a == 4:
    b = int(input("Number 1: "))
    c = int(input("Number 2: "))
    print("the result is: " + str(b * c))
elif a == 5:
    b = int(input("Number 1: "))
    c = int(input("Number 2: "))
    print("the result is: " + str(b ** c))