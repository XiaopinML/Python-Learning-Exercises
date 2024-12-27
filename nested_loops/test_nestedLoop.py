# Exercise 1: Multiplication Table (Easy)
# Write a Python program that uses nested loops 
# to generate a 10x10 multiplication table. 
# The table should display the product
#  of the row and column numbers.

# Example Output:

# python
# Copy code
# 1  2   3   4   5   6   7   8   9  10
# 2  4   6   8  10  12  14  16  18  20
# 3  6   9  12  15  18  21  24  27  30
# ...
# 10 20  30  40  50  60  70  80  90 100

# for i in range(1,11):
#      for j in range(1,11):
#           print (i*j,end=' ')
#      print()          
   
#the first execise is done easy!

# Exercise 2: Pyramid Pattern (Intermediate)
# Write a Python program that uses nested 
# loops to create a pyramid pattern of stars (*). 
# The number of rows should be specified by the user.

# Example Output for 5 rows:

# markdown
# Copy code
#     *
#    ***
#   *****
#  *******
# *********

num_input = int(input('Please enter your input to see a pyramid pattern\n'))

for i in range(num_input):
    # Print spaces
    for j in range(num_input - i - 1):
        print(' ', end='')

    # Print stars
    for k in range(2* i + 1):
        print('*', end='')

    # Move to the next line
    print()

    

