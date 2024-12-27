
# ### **Challenge: Attendance Tracker**
# You are given a list of **student names** and a corresponding 
# list of their attendance records. Each attendance record is a string of letters:
# - `'P'` means Present.
# - `'A'` means Absent.

# Your task is to:
# 1. Calculate the **total number of classes attended** by each student.
# 2. Identify if any student has an **attendance rate below 75%**, and print a warning for them.

# ---

# ### **Example Input**:
# ```python
# students = ["Alice", "Bob", "Charlie", "David"]
# attendance = ["PPAPP", "PAPAA", "PPPPP", "AAPPP"]
# ```

# ### **Expected Output**:
# ```
# 1. Alice: Attended 3/5 classes (60%) - Warning: Low Attendance
# 2. Bob: Attended 2/5 classes (40%) - Warning: Low Attendance
# 3. Charlie: Attended 5/5 classes (100%) - Good Attendance
# 4. David: Attended 3/5 classes (60%) - Warning: Low Attendance
# ```

# ---

# ### **Instructions**:
# 1. Use `enumerate` to loop through the `students` and their corresponding `attendance` records.
# 2. Count the number of `'P'` in each attendance record.
# 3. Calculate the attendance percentage for each student.
# 4. Print the result in the specified format.
# 5. Include a **warning** if the attendance percentage is below 75%.

# ---

# ### **Challenge (Optional)**:
# - Handle cases where the `students` and `attendance` lists are of different lengths by printing a warning.
# - Sort the output by attendance percentage in descending order.





students = ["Alice", "Bob", "Charlie", "David"]
attendance = ["PPAPP", "PAPAA", "PPPPP", "AAPPP"]
if len(students) != len(attendance):
        print("Warning ! there's mismatch between the the studdents and the attendance")
        exit()
for index, (student, attendant) in enumerate(zip(students,attendance)):

    total_class = len(attendant)
    attended_classes = attendant.count("P")
    attendance_percentage = attended_classes / total_class *100
    warning = "Low Attendance"if attendance_percentage < 75 else  "Good Attendance"
    print(f'{index + 1 }. {student} attended {attended_classes}/{total_class} classes ({attendance_percentage:.2f}%) - {warning}')
    
