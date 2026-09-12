import json

from quiz import Quiz


with open("data/questions.json", "r") as file:
    questions = json.load(file)


quiz = Quiz(questions)

quiz.start()