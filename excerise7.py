
# Ask user to enter the number of students.
number_of_students = int(input("Enter a number : "))

for i in range(number_of_students):
    score = int(input(f"Enter the score  of student {i+1}: "))

    if(score<50):
        print(f"Student {i+1} passed  ✅")
    else:
        print(f"student {i+1} failed ❌")