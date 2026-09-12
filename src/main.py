from quiz import Quiz
from utils import load_questions


questions = load_questions("data/questions.json")


if not questions:
    exit()


quiz = Quiz(questions)


while True:
    quiz.start()

    if not quiz.play_again():
        print("\nThank you for playing!")
        break