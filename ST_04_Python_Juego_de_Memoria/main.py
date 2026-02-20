import random

NUM_PAIRS = 3

def main():
    # Milestone #1: Crear la lista de "verdad" (truth list)
    truth = []
    for i in range(NUM_PAIRS):
        for _ in range(2):
            truth.append(i)

    # Milestone #2: Barajar la lista
    random.shuffle(truth)
    # print(truth) # Descomenta para probar

    # Milestone #3: Crear la lista visual (displayed list)
    displayed = ["*"] * (NUM_PAIRS * 2)

    # Milestone #6: Jugar múltiples turnos
    pairs_found = 0
    while pairs_found < NUM_PAIRS:
        print(displayed)
        
        # Milestone #4 & #5: Obtener índices y validar
        index1 = get_valid_index(displayed)
        index2 = get_valid_index(displayed)

        if index1 == index2:
            input("No puedes poner dos indices iguales. Press Enter to continue...")
            clear_terminal()
            continue

        # Lógica de comprobación
        if truth[index1] == truth[index2]:
            displayed[index1] = truth[index1]
            displayed[index2] = truth[index2]
            input("Match!")
            pairs_found += 1
        else:
            print(f"Value at index {index1} is {truth[index1]}")
            print(f"Value at index {index2} is {truth[index2]}")
            input("No match. Try again. Press Enter to continue...")
        
        clear_terminal()

    print(displayed)
    print('Congratulations! You won!')

def get_valid_index(displayed):
    """
    Milestone #4: Solicita un índice y valida que:
    1. Esté dentro del rango de la lista.
    2. No haya sido revelado ya (que sea '*').
    """
    while True:
        try:
            val = int(input("Enter an index: "))
            # Validar rango
            if val < 0 or val >= len(displayed):
                print(f"Index must be between 0 and {len(displayed) - 1}.")
            # Validar si ya fue revelado
            elif displayed[val] != "*":
                print("That index is already revealed! Try another one.")
            else:
                return val
        except ValueError:
            print("Please enter a valid number.")

def clear_terminal():
    for i in range(20):
        print('\n')

if __name__ == '__main__':
    main()