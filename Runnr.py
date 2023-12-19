import random

def display_intro():
    print("Welcome to the Python Car Game!")
    print("Type 'start' to begin the game.")
    print("Type 'quit' to exit.")

def start_game():
    distance = 0
    while True:
        user_input = input("Type 'accelerate' to speed up, 'brake' to slow down, or 'quit' to exit: ").lower()

        if user_input == 'quit':
            print("Game over. Your final distance is:", distance)
            break
        elif user_input == 'accelerate':
            speed = random.randint(5, 15)
            distance += speed
            print(f"You accelerated and covered {speed} units of distance. Total distance: {distance}")
        elif user_input == 'brake':
            speed = random.randint(1, 5)
            distance += speed
            print(f"You slowed down and covered {speed} units of distance. Total distance: {distance}")
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    display_intro()
    user_start = input("Type 'start' to begin: ").lower()

    if user_start == 'start':
        start_game()
    else:
        print("Invalid input. Exiting.")
