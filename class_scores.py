# class_scores.py
count_students = int(input("Enter number of students: "))
total = 0
i = 1
while i <= count_students:
    score = float(input(f"Enter score for student {i}: "))
    total += score
    i += 1

average = total / count_students
print(f"\nTotal Scores: {total}")
print(f"Average Score: {average:.2f}")