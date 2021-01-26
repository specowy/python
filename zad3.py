word = "python"
turns = 5
print("Odgadnij słowo w", +turns, "ruchach")
while turns > 0:
    guess = input("guess a character:")

    if guess != word:
        turns -= 1
        print("To nie to słowo")
        print("Masz jeszcze", + turns, 'możliwości')

        if turns == 0:
            print("Przegrałeś")
    else:
        print("Brawo, zgadłeś!",)
        break
