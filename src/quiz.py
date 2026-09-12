def display_question(question):
    print("\n" + question["question"])

    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")


def get_answer():
    while True:
        answer = input("Enter your answer (1-4): ")

        if answer in ["1", "2", "3", "4"]:
            return int(answer)

        print("Invalid choice. Please enter a number from 1 to 4.")


def check_answer(question, answer):
    selected_answer = question["options"][answer - 1]

    if selected_answer == question["answer"]:
        print("Correct!")
        return True

    print("Wrong!")
    print("Correct answer:", question["answer"])
    return False