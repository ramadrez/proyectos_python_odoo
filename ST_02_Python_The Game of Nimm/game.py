def main():
    piedras = 20
    jugador = 1

    while piedras > 0:
        print("There are",piedras,"stones left.")
        msg = int(input(f"Player {jugador} would you like to remove 1 or 2 stones? "))
        while msg != 1 and msg != 2:
            msg = int(input("Please enter 1 or 2: "))
        print("")
        
        piedras -= msg
        if jugador == 1:
            jugador = 2
        else:
            jugador = 1
        
    if jugador == 1:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

if __name__ == '__main__':
    main()