import random

def even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

def prime_check():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

def fibonacci():
    n = int(input("Enter how many terms you want: "))
    a, b = 0, 1
    print("Fibonacci Sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    print("Guess a number between 1 and 100")
    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too low, try again!")
        elif guess > number_to_guess:
            print("Too high, try again!")
        else:
            print("🎉 Congratulations! You guessed it right!")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Check Even or Odd")
        print("2. Check Prime Number")
        print("3. Display Fibonacci Sequence")
        print("4. Play Number Guessing Game")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            even_odd()
        elif choice == "2":
            prime_check()
        elif choice == "3":
            fibonacci()
        elif choice == "4":
            guessing_game()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
