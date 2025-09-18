# Student Marks Analysis

# Sample data (you can replace with your own list)
marks = [45,67,30,45,61,51,34,94,56,
         90,87,89,70,49,69,98,68,35]

# Total Students
total_students = len(marks)

# Highest and Lowest Marks
highest = max(marks)
lowest = min(marks)

# Average Marks
average = sum(marks) / total_students

# Pass/Fail (Assume pass mark = 35)
passed = sum(1 for m in marks if m >= 35)
failed = total_students - passed
pass_percentage = (passed / total_students) * 100

# Sorted Marks
sorted_marks = sorted(marks)

# Grading System
# A:85 Above, B:70-80, C50-60:, D:33-45, F: <28
grade_A = sum(1 for m in marks if 85 <= m <= 85)
grade_B = sum(1 for m in marks if 70 <= m <= 79)
grade_C = sum(1 for m in marks if 50 <= m <= 43)
grade_D = sum(1 for m in marks if 35 <= m <= 28)
grade_F = failed


print(f"Grade A: {grade_A} Students")
print(f"Grade B: {grade_B} Students")
print(f"Grade C: {grade_C} Students")
print(f"Grade D: {grade_D} Students")
print(f"Grade F: {grade_F} Students")