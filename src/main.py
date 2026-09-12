import json

from quiz import Quiz


try:
    with open("data/questions.json", "r") as file:
        questions = json.load(file)

except FileNotFoundError:
    print("Error: Questions file was not found.")
    exit()

except json.JSONDecodeError:
    print("Error: Questions file contains invalid JSON.")
    exit()


quiz = Quiz(questions)


while True:
    quiz.start()

    if not quiz.play_again():
        print("\nThank you for playing!")
        break