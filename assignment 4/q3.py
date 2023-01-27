import random

i, correct_answers = 0, 0

while (i < 10):
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)

    print(number1, " * ", number2, " = ?")

    multiplication_answer = int(input())

    if (multiplication_answer == (number1 * number2)):
        print("Your answer is correct.")
        correct_answers += 1
    else:
        print("The answer is incorrect.")

    i += 1

print("The game is over! You scored: ", correct_answers, " / 10")