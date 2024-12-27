# players = ["Ali","farah","jamac"]
# for rank,player in enumerate(players,start=1):
#     print(f'Rank : {rank} : {player}')

# fruits = ["farah","ali","Cherry"]
# for index, fruit in enumerate(fruits,start=7):
#     print(f'Index : {index} : {fruit}')
# info = {
#     "Name": "Ali",
#      "age": 25,
#       "Job": "SalesMan"
#         }
# for index, infos in enumerate(info):
#     print(f'{index} : {infos}')
# chars = "hello"
# for index, char in enumerate("hello"):
#     print(f'{index} : {char}')

#analayzing a file and u need to log which line contains an issue

# lines =["Good line", " bad line", "Good line"]
# for line_numbers, line in enumerate(lines):
#     if "bad" in line:
#         print(f' the error is on the line {line_numbers} : {line}')

# create a menu 
# menu = ["Burger","cola cola","orange"]
# for index, menus in enumerate(menu,start=1):
#     print(f'{index} : {menus}')

# check student's answer
# registered = ["Alice", "Bob", "Eve", "David", "Charlie"]
# attended = ["Alice", "Charlie", "Eve"]
# for index,particpants in enumerate(registered):
#       if particpants not in attended:
#         print(f'Participant at position {index + 1} : {particpants} is missing.')



# #Challenge: Marking Students Who Passed
# You are given two lists:

# A list of student names.
# A list of their corresponding scores.
# Your task is to print:

# Each student's name and whether they passed or failed.
# Consider a passing score to be 50 or above.
# Instructions:
# Use enumerate to loop through the list of student names and their scores.
# Check if the score is greater than or equal to 50.
# Print a message for each student, showing:
# Their name.
# Their score.
# Whether they passed or failed.
# Example Input:
# python
# Copy code
# students = ["Alice", "Bob", "Charlie", "David", "Eve"]
# scores = [85, 42, 73, 30, 60]
# Expected Output:
# markdown
# Copy code
# 1. Alice (85): Passed
# 2. Bob (42): Failed
# 3. Charlie (73): Passed
# 4. David (30): Failed
# 5. Eve (60): Passed

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
scores = [85, 42, 73, 30, 60]
for index,(student, score) in enumerate (zip(students,scores)):
    if len(students) != len(scores):
        print ("warning : the student's and the score do not match")
    else:
      status = "Passed" if score > 50 else "failed"
      print (f'{index + 1:<3} | {student:<10} | ({score:>2}): {status}')