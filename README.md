# 🧠 Python Quiz Game

A console-based **Python Quiz Game** that tests programming knowledge through categorized and difficulty-based questions. The application includes randomized questions, time limits, scoring, performance analysis, answer review, quiz history, and high-score tracking.

## 🚀 Features

* 🎯 Category-based quiz selection
* 📊 Difficulty levels: Easy, Medium, and Hard
* 🔀 Randomized questions
* 🔢 Custom number of questions
* ⏱️ Difficulty-based time limits
* ✅ Instant correct/wrong answer feedback
* 📈 Score and percentage calculation
* 🏆 Grade calculation
* 💬 Performance feedback
* 📋 Session summary
* 📊 Difficulty-wise performance statistics
* 📚 Category-wise performance statistics
* 🔍 Answer review after the quiz
* 💾 Quiz results saved to JSON
* 📜 Previous quiz attempt history
* 🏆 Best score / high-score tracking
* 🔁 Replay functionality
* 🛡️ Input and JSON error handling

## 🛠️ Tech Stack

* **Language:** Python
* **Data Storage:** JSON
* **Concepts Used:**

  * Object-Oriented Programming
  * Functions
  * Lists and Dictionaries
  * File Handling
  * Exception Handling
  * Randomization
  * Time Management
  * Data Processing

## 📂 Project Structure

```text
python-quiz-game/
│
├── data/
│   ├── questions.json
│   └── results.json
│
├── src/
│   ├── main.py
│   ├── quiz.py
│   └── utils.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Shreya-Sutar/python-quiz-game.git
```

### 2. Open the project folder

```bash
cd python-quiz-game
```

### 3. Run the quiz

```bash
python src/main.py
```

No external Python packages are required.

## 🎮 How the Game Works

### Step 1 — Choose a Category

The player can select a specific category or play questions from all categories.

### Step 2 — Choose Difficulty

The player can select:

```text
1. Easy
2. Medium
3. Hard
4. All Difficulties
```

### Step 3 — Choose Number of Questions

The player selects how many questions they want to answer.

### Step 4 — Answer Questions

Each question has a difficulty-based time limit:

| Difficulty | Time Limit |
| ---------- | ---------- |
| Easy       | 20 seconds |
| Medium     | 15 seconds |
| Hard       | 10 seconds |

### Step 5 — View Results

After completing the quiz, the application displays:

* Total questions
* Correct answers
* Wrong answers
* Score
* Percentage
* Grade
* Performance message

### Step 6 — Analyze Performance

The application also displays:

* Session summary
* Difficulty performance
* Category performance
* Answer review

### Step 7 — Save Results

Quiz results are automatically stored in:

```text
data/results.json
```

Previous attempts and the highest score can then be viewed.

## 📊 Example

```text
================================
          QUIZ RESULT
================================
Total Questions : 5
Correct Answers : 4
Wrong Answers   : 1
Score           : 4/5
Percentage      : 80%
Grade           : B
Performance     : Great job!
================================
```

## 💾 Result History

The application stores quiz attempts in JSON format:

```json
[
    {
        "score": 4,
        "total_questions": 5,
        "percentage": 80.0,
        "grade": "B"
    }
]
```

This allows the application to maintain quiz history and calculate the user's best score.

## 🧩 Project Architecture

The project is divided into three main Python modules:

### `main.py`

Responsible for:

* Loading questions
* Creating the Quiz object
* Starting the quiz
* Handling replay

### `quiz.py`

Contains the main quiz logic:

* Category selection
* Difficulty selection
* Question selection
* Timer
* Answer checking
* Scoring
* Statistics
* History
* High score

### `utils.py`

Contains reusable utility functions for:

* Loading questions
* Saving results
* Loading previous results
* JSON error handling

## 🔮 Future Improvements

Possible future enhancements include:

* 🌐 Web-based interface
* 🗄️ Database integration
* 👤 User accounts
* 📊 Graphical performance dashboard
* 🥇 Leaderboard
* ➕ Larger question bank
* 🧠 AI-generated questions
* 📱 Responsive UI
* ☁️ Cloud-based result storage

## 👩‍💻 Author

**Shreya Sutar**

Computer Science Engineering Student

---

⭐ If you find this project useful, consider giving the repository a star!
