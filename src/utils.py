import json


def load_questions(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: Questions file was not found.")
        return []

    except json.JSONDecodeError:
        print("Error: Questions file contains invalid JSON.")
        return []


def save_result(file_path, result):
    try:
        try:
            with open(file_path, "r") as file:
                results = json.load(file)

        except FileNotFoundError:
            results = []

        except json.JSONDecodeError:
            results = []

        results.append(result)

        with open(file_path, "w") as file:
            json.dump(results, file, indent=4)

        print("\nQuiz result saved successfully.")

    except OSError:
        print("\nError: Could not save quiz result.")


def load_results(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: Results file contains invalid JSON.")
        return []