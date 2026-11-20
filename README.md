# Number Guessing Game

[A command-line number guessing game written in Python, where you choose a difficulty and try to find the secret number within a limited number of attempts, using hints after each guess.]

## Features

- [Difficulty levels: easy (1-10, 5 attempts) and hard (1-100, 10 attempts)]
- [Hints after each wrong guess]
- [Input validation: what happens with text or out-of-range numbers]
- [Whether invalid input costs an attempt]
- [Play again option and what it lets the player do]

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/vaibhavbhardwajwork-a11y/number-guessing-game.git
   ```
2. Go into the folder:
   ```
   cd number-guessing-game
   ```
3. Start the game:
   ```
   python guessing_game.py
   ```

## How to Play

1. [Choose a difficulty]
2. [Guess the number within the allowed attempts]
3. [Use the hints to narrow it down]
4. [Choose whether to play again]

## Example

```
[Enter difficulty (easy/hard): easy
Attempts remaining: 5
Enter a number between 1 and 10: 5
Hint: it's lower than your guess.
Attempts remaining: 4
Enter a number between 1 and 10: 4
Hint: it's lower than your guess.
Attempts remaining: 3
Enter a number between 1 and 10: 3
Hint: it's lower than your guess.
Attempts remaining: 2
Enter a number between 1 and 10: 2
Hint: it's lower than your guess.
Attempts remaining: 1
Enter a number between 1 and 10: 1
Congrats!! You guessed the right number.
Play again (y/n): y
Enter difficulty (easy/hard): easy
Attempts remaining: 5
Enter a number between 1 and 10: 5
Hint: it's lower than your guess.
Attempts remaining: 4
Enter a number between 1 and 10: 9
Hint: it's lower than your guess.
Attempts remaining: 3
Enter a number between 1 and 10: 1
Congrats!! You guessed the right number.
Play again (y/n): n
Thanks for playing!!]
```

## What I Practiced

- [Loops: nested while loops, break and continue]
- [Error handling with try/except]
- [Input validation]
- [f-strings]
- [Git and GitHub workflow]

