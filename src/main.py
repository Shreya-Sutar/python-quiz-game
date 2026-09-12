import json

with open("data/questions.json", "r") as file:
    questions = json.load(file)

score = 0

for question in questions:
    print("\n" + question["question"])

    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")

    answer = input("Enter your answer (1-4): ")

    if question["options"][int(answer) - 1] == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz completed!")
print("Your score:", score, "/", len(questions))