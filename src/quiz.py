import random
import time
import msvcrt


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.review = []
        self.difficulty_stats = {}
        self.category_stats = {}

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

    def choose_question_count(self, questions):
        total_available = len(questions)

        print("\n==============================")
        print("     NUMBER OF QUESTIONS")
        print("==============================")
        print(f"Available questions: {total_available}")

        while True:
            choice = input(
                f"How many questions do you want? (1-{total_available}): "
            )

            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= total_available:
                    return random.sample(questions, choice)

            print(
                f"Invalid choice. Please enter a number from 1 to {total_available}."
            )

    def get_time_limit(self, difficulty):
        time_limits = {
            "Easy": 20,
            "Medium": 15,
            "Hard": 10
        }

        return time_limits.get(difficulty, 15)

    def display_question(self, question, question_number, total_questions):
        print("\n--------------------------------")
        print(f"Question {question_number} of {total_questions}")
        print("--------------------------------")
        print("Category:", question["category"])
        print("Difficulty:", question["difficulty"])
        print(question["question"])

        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        time_limit = self.get_time_limit(question["difficulty"])

        print(f"\nYou have {time_limit} seconds to answer.")

    def get_answer(self, time_limit):
        print("Enter your answer (1-4): ", end="", flush=True)

        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time

            if elapsed_time >= time_limit:
                print("\nTime's up!")
                return None

            if msvcrt.kbhit():
                key = msvcrt.getwch()

                if key in ["1", "2", "3", "4"]:
                    print(key)
                    return int(key)

                print("\nInvalid choice. Please enter a number from 1 to 4.")
                print("Enter your answer (1-4): ", end="", flush=True)

    def check_answer(self, question, answer):
        difficulty = question["difficulty"]
        category = question["category"]

        if difficulty not in self.difficulty_stats:
            self.difficulty_stats[difficulty] = {
                "total": 0,
                "correct": 0
            }

        if category not in self.category_stats:
            self.category_stats[category] = {
                "total": 0,
                "correct": 0
            }

        self.difficulty_stats[difficulty]["total"] += 1
        self.category_stats[category]["total"] += 1

        if answer is None:
            print("Correct answer:", question["answer"])

            self.review.append({
                "question": question["question"],
                "selected": "Time's Up",
                "correct": question["answer"],
                "is_correct": False
            })

            return

        selected_answer = question["options"][answer - 1]

        if selected_answer == question["answer"]:
            print("Correct!")

            self.score += 1
            self.difficulty_stats[difficulty]["correct"] += 1
            self.category_stats[category]["correct"] += 1

            is_correct = True

        else:
            print("Wrong!")
            print("Correct answer:", question["answer"])

            is_correct = False

        self.review.append({
            "question": question["question"],
            "selected": selected_answer,
            "correct": question["answer"],
            "is_correct": is_correct
        })

    def start(self):
        self.score = 0
        self.review = []
        self.difficulty_stats = {}
        self.category_stats = {}

        selected_questions = self.choose_category()

        selected_questions = self.choose_difficulty(selected_questions)

        selected_questions = self.choose_question_count(selected_questions)

        total_questions = len(selected_questions)

        for question_number, question in enumerate(
            selected_questions, start=1
        ):
            time_limit = self.get_time_limit(question["difficulty"])

            self.display_question(
                question,
                question_number,
                total_questions
            )

            answer = self.get_answer(time_limit)

            self.check_answer(question, answer)

        self.show_result(total_questions)
        self.show_difficulty_stats()
        self.show_category_stats()
        self.show_review()

    def get_grade(self, percentage):
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"

    def show_result(self, total_questions):
        wrong_answers = total_questions - self.score
        percentage = (self.score / total_questions) * 100
        grade = self.get_grade(percentage)

        print("\n================================")
        print("          QUIZ RESULT")
        print("================================")
        print(f"Total Questions : {total_questions}")
        print(f"Correct Answers : {self.score}")
        print(f"Wrong Answers   : {wrong_answers}")
        print(f"Score           : {self.score}/{total_questions}")
        print(f"Percentage      : {percentage:.0f}%")
        print(f"Grade           : {grade}")
        print("================================")

    def show_difficulty_stats(self):
        print("\n================================")
        print("     DIFFICULTY PERFORMANCE")
        print("================================")

        for difficulty in ["Easy", "Medium", "Hard"]:
            if difficulty in self.difficulty_stats:
                stats = self.difficulty_stats[difficulty]

                print(
                    f"{difficulty:<8}: "
                    f"{stats['correct']}/{stats['total']}"
                )

        print("================================")

    def show_category_stats(self):
        print("\n================================")
        print("       CATEGORY PERFORMANCE")
        print("================================")

        for category in sorted(self.category_stats):
            stats = self.category_stats[category]

            print(
                f"{category:<20}: "
                f"{stats['correct']}/{stats['total']}"
            )

        print("================================")

    def show_review(self):
        print("\n================================")
        print("         ANSWER REVIEW")
        print("================================")

        for i, item in enumerate(self.review, start=1):
            print(f"\nQuestion {i}: {item['question']}")
            print(f"Your Answer    : {item['selected']}")
            print(f"Correct Answer : {item['correct']}")

            if item["is_correct"]:
                print("Result         : Correct")
            else:
                print("Result         : Wrong")

        print("\n================================")

    def play_again(self):
        while True:
            choice = input("\nDo you want to play again? (y/n): ").lower()

            if choice == "y":
                return True

            if choice == "n":
                return False

            print("Invalid choice. Please enter y or n.")