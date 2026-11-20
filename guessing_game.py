import random

high = 100
low = 1
max_attempts = 10
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
