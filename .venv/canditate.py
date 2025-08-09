test1 = float(input("Enter your Test 1 score: "))
test2 = float(input("Enter your Test 2 score: "))


average = (test1 + test2) / 2
print("Your average score is:", average)


if test1 > 75 and test2 > 75 and average >= 80:
    print("You have been picked for the interview.")
else:
    print("Sorry, you have not passed the requirement.")
