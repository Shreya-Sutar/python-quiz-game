import random


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_categories(self):
        categories = sorted(
            set(question["category"] for question in self.questions)
        )

        print("\n==============================")
        print("       QUIZ CATEGORIES")
        print("==============================")

        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        print(f"{len(categories) + 1}. All Categories")

        return categories

    def choose_category(self):
        categories = self.display_categories()

        while True:
            choice = input(
                f"Choose a category (1-{len(categories) + 1}): "
            )

            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= len(categories):
                    selected_category = categories[choice - 1]

                    return [
                        question
                        for question in self.questions
                        if question["category"] == selected_category
                    ]

                if choice == len(categories) + 1:
                    return self.questions

            print(
                f"Invalid choice. Please enter a number from 1 to {len(categories) + 1}."
            )

    def display_difficulties(self):
        difficulties = ["Easy", "Medium", "Hard"]

        print("\n==============================")
        print("       QUIZ DIFFICULTY")
        print("==============================")

        for i, difficulty in enumerate(difficulties, start=1):
            print(f"{i}. {difficulty}")

        print("4. All Difficulties")

        return difficulties

    def choose_difficulty(self, questions):
        difficulties = self.display_difficulties()

        while True:
            choice = input("Choose a difficulty (1-4): ")

            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= 3:
                    selected_difficulty = difficulties[choice - 1]

                    filtered_questions = [
                        question
                        for question in questions
                        if question["difficulty"] == selected_difficulty
                    ]

                    if filtered_questions:
                        return filtered_questions

                    print("No questions available for this difficulty.")
                    continue

                if choice == 4:
                    return questions

            print("Invalid choice. Please enter a number from 1 to 4.")

    def display_question(self, question):
        print("\nCategory:", question["category"])
        print("Difficulty:", question["difficulty"])
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
        selected_questions = self.choose_category()

        selected_questions = self.choose_difficulty(selected_questions)

        random.shuffle(selected_questions)

        for question in selected_questions:
            self.display_question(question)

            answer = self.get_answer()

            self.check_answer(question, answer)

        self.show_result(len(selected_questions))

    def show_result(self, total_questions):
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