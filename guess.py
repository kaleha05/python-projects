# Guess the number
import random

temp = 0
num = random.randint(1, 10)
marks = 10
while temp != num and marks != 0:
    print("Your points: ", marks)
    print("Hint: the number is even") if num % 2 == 0 else print("Hint: The number is odd")
    print("Hint: Number is less than 5") if num < 5 else print("Hint: Number is greater than or equal to 5")

    userGuess = int(input("Your guess: "))
    temp = userGuess
    if userGuess == num:
        print("Hooray, you guessed correctly")
    else:
        print("Oops,try again next time")
        marks = marks - 2
        print("You now have ", marks, "points")