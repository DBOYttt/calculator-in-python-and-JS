print("HI im calculator maked by D-BOY")

print('''
Wybierz co chcesz zrobić 
1 - Dodać 
2 - Odjąć 
3 - Podzielić
4 - Pomnożyć
5 - Spotengować
''')

a = int(input("wybierz: "))

if a == 1: 
    b = int(input("Liczba 1: "))
    c = int(input("Liczba 2: "))
    print("wynik to: " + str(b + c))
elif a == 2:
    b = int(input("Liczba 1: "))
    c = int(input("Liczba 2: "))
    print("wynik to: " + str(b - c))