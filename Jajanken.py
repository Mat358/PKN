import random

marks = ("Kamień", "Papier", "Nożyce")
computer = marks[random.randrange(0,3)]

while True:
    try:
        move = int(input("Wybierz swój znak: \n1. Kamień \n2. Papier \n3. Nożyce \nWprowadź liczbe od 1 do 3: "))

        if move in range(1,4):
            player = marks[move - 1]

            if player == computer:
                print(f"Gracz: {player} \nKomputer: {computer}")
                print("Ramis")
                break
            elif player == marks[0] and computer == marks[2]:
                print(f"Gracz: {player} \nKomputer: {computer}")
                print("Wygrałeś")
                break
            elif player == marks[1] and computer == marks[0]:
                print(f"Gracz: {player} \nKomputer: {computer}")
                print("Wygrałeś")
                break
            elif player == marks[2] and computer == marks[1]:
                print(f"Gracz: {player} \nKomputer: {computer}")
                print("Wygrałeś")
                break


            elif player == marks[0] and computer == marks[1]:
                print(f"Gracz: {player} \nKomputer: {computer}")
                print("Przegrałeś")
                break
            elif player == marks[1] and computer == marks[2]:
                print(f"Gracz: {player} \nKomputer: {computer}")
                print("Przegrałeś")
                break
            elif player == marks[2] and computer == marks[0]:
                print(f"Gracz: {player} \nKomputer: {computer}")
                print("Przegrałeś")
                break
        else:
            print("Wprowadź odpowiednią liczbę.")
            continue
    except ValueError:
        print("--------------\nWprowadź cyfrę od 1 do 3.\n--------------")        

