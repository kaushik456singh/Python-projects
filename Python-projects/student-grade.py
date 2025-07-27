name = input("Enter student name: ")
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]
avg = sum(marks) / len(marks)
grade = 'A' if avg >= 90 else 'B' if avg >= 70 else 'C'
print(f"{name}'s Average: {avg}, Grade: {grade}")