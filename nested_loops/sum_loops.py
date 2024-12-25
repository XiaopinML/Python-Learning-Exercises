# Define a list of lists (2D list)
list = [1, 2, 3], [2, 3, 4]

# Initialize a variable to hold the total sum
total = 0

# Outer loop iterates over each sublist in the list
for list1 in list:
    # Inner loop iterates over each element in the current sublist
    for list2 in list1:
        # Add the current element to the total sum
        total += list2
        # Print the current total sum followed by a space
        print(total, end=' ')

# Print a newline after the loops are completed
print()