

# Challenge 1: Reverse ssing Game
# Write a program that:

# Asks the user to input a list of numbers separated by commas (e.g., 1,2,3,4,5).
# Reverses the list of numbers.
# Randomly selects one number from the reversed list.
# Asks the user to guess the number.
# Compares the guess to the selected number and prints
#  whether it’s correct or not, along with the reversed list.
import random

# Get input from the user
input_list = input("Enter a list of numbers separated by commas:\n")
numbers = input_list.split(',')

# Validate input and convert to integers
try:
    numbers = [int(x.strip()) for x in numbers]
except ValueError:
    print("Please enter a list of valid numbers separated by commas.")
    exit()

# Reverse the list and pick a random number
reversed_numbers = list(reversed(numbers))
random_number = random.choice(reversed_numbers)

# Ask the user to guess
guess_number = int(input("Guess the number I picked from your list:\n"))

# Check if the guessed number is in the reversed list
if guess_number not in reversed_numbers:
    print("The number you guessed is not in the list you provided. Please try again!")
    exit()

# Check if the guess is correct
guess_status = "correct" if guess_number == random_number else "incorrect"

# Display the results
print(f"Reversed: {reversed_numbers}")
print(f"You guessed: {guess_number}")
print(f"The random number was: {random_number}")
print(f"Your guess is {guess_status}.")
