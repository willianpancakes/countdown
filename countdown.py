import sys
import random
import time

def numbers_round() -> None:
    all_numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 25, 50, 50, 75, 75, 100, 100]
    available_numbers = all_numbers
    small_numbers = []
    big_numbers = []
    
    for _ in range(6):
        number = random.choice(available_numbers)

        if number <= 10:
            available_numbers.remove(number)
            small_numbers.append(number)
        else:
            while number in available_numbers:
                available_numbers.remove(number)
            
            big_numbers.append(number)
    
    target_number = random.randint(100, 999)
    
    print(target_number)
    
    for number in big_numbers:
        print(number, end=" ")
    
    for number in small_numbers:
        print(number, end=" ")
    
    print()


def letters_round() -> None:
    all_letters = ["A", "A", "A", "A", "A", "A", "A", "A", "A", 
                    "B", "B", 
                    "C", "C", "C", 
                    "D", "D", "D", "D", "D", 
                    "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", 
                    "F", "F", "F", 
                    "G", "G", "G", 
                    "H", "H", "H", "H", "H", "H", "H", 
                    "I", "I", "I", "I", "I", "I", "I", 
                    "J", 
                    "K", "K", 
                    "L", "L", "L", "L", "L", 
                    "M", "M", "M", 
                    "N", "N", "N", "N", "N", "N", "N", 
                    "O", "O", "O", "O", "O", "O", "O", "O", 
                    "P", "P", 
                    "Q", 
                    "R", "R", "R", "R", "R", "R", 
                    "S", "S", "S", "S", "S", "S", "S", 
                    "T", "T", "T", "T", "T", "T", "T", "T", "T", "T", 
                    "U", "U", "U", 
                    "V", 
                    "W", "W", "W", 
                    "X", 
                    "Y", "Y", 
                    "Z"]
    
    available_letters = all_letters
    letters = []

    for _ in range(9):
        letter = random.choice(available_letters)
        available_letters.remove(letter)
        letters.append(letter)
        print(letter, end=" ")
    
    print()


def main():
    try:
        if sys.argv[1] == "numbers":
            numbers_round()
        elif sys.argv[1] == "letters":
            letters_round()
        else:
            print("Invalid argument.")
        
        time.sleep(30)
        
    except IndexError:
        print("Select either the 'letters' or the 'numbers' round.")


main()