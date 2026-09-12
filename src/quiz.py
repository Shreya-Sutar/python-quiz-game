import random


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print("\nCategory:", question["category"])
        print(question["question"])

        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

    def get_answer(self):
        while True:
            answer = input("Enter your answer (1-4): ")

            if answer in ["1", "2", "3", "4"]:
                return int(answer)

            print("Invalid choice. Please enter a number from 1 to 4.")

    def check_answer(self, question, answer):
        selected_answer = question["options"][answer - 1]

        if selected_answer == question["answer"]:
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
            print("Correct answer:", question["answer"])

    def start(self):
        random.shuffle(self.questions)

        for question in self.questions:
            self.display_question(question)

            answer = self.get_answer()

            self.check_answer(question, answer)

        self.show_result()

    def show_result(self):
        total_questions = len(self.questions)
        wrong_answers = total_questions - self.score
        percentage = (self.score / total_questions) * 100

        print("\n================================")
        print("          QUIZ RESULT")
        print("================================")
        print(f"Total Questions : {total_questions}")
        print(f"Correct Answers : {self.score}")
        print(f"Wrong Answers   : {wrong_answers}")
        print(f"Score           : {self.score}/{total_questions}")
        print(f"Percentage      : {percentage:.0f}%")
        print("================================")