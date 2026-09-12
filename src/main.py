import json

from quiz import display_question, get_answer, check_answer


with open("data/questions.json", "r") as file:
    questions = json.load(file)


score = 0


for question in questions:
    display_question(question)

    answer = get_answer()

    if check_answer(question, answer):
        score += 1


print("\nQuiz completed!")
print("Your score:", score, "/", len(questions))