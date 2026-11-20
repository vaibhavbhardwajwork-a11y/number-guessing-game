import random


while True:
    difficulty = input("Enter difficulty (easy/hard): ")
    difficulty = difficulty.strip().lower()
     
    if difficulty == "easy":
        low = 1
        high = 10
        max_attempts = 5
        break

    elif difficulty == "hard":
        low = 1
        high = 100
        max_attempts = 10
        break

    else:
        print("Pls enter a valid difficulty level.")
        
     
attempts = max_attempts     
secret = random.randint(low, high)



while attempts > 0:
    
    print("Attempts remaining:", attempts)
    try:
        guess = int(input(f"Enter a number between {low} and {high}: "))
        
    except ValueError:
        print("Please enter a valid number.")
        continue 

    if guess > high or guess < low:
            print(f"Pls enter numbers between {low} & {high}.")
            continue

    if guess == secret:
        print("Congrats!! You guessed the right number.")
        break
    elif guess > secret:
        print("Hint: it's lower than your guess.")
    else:
        print("Hint: it's higher than your guess.")
    attempts -= 1
else:
    print("Out of attempts. The number was:", secret)
