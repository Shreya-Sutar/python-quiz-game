import json

from quiz import Quiz


with open("data/questions.json", "r") as file:
    questions = json.load(file)


quiz = Quiz(questions)


while True:
    quiz.start()

    if not quiz.play_again():
        print("\nThank you for playing!")
        break