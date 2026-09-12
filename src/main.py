import json

with open("data/questions.json", "r") as file:
    questions = json.load(file)

score = 0

for question in questions:
    print("\n" + question["question"])

    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")

    while True:
        answer = input("Enter your answer (1-4): ")

        if answer in ["1", "2", "3", "4"]:
            break

        print("Invalid choice. Please enter a number from 1 to 4.")

    selected_answer = question["options"][int(answer) - 1]

    if selected_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", question["answer"])

print("\nQuiz completed!")
print("Your score:", score, "/", len(questions))
