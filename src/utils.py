import json


def load_questions(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)

            if not isinstance(data, list):
                print("Error: Questions data must be a list.")
                return []

            return data

    except FileNotFoundError:
        print("Error: Questions file was not found.")
        return []

    except json.JSONDecodeError:
        print("Error: Questions file contains invalid JSON.")
        return []

    except OSError:
        print("Error: Could not read questions file.")
        return []


def save_result(file_path, result):
    try:
        try:
            with open(file_path, "r") as file:
                results = json.load(file)

                if not isinstance(results, list):
                    results = []

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
            results = json.load(file)

            if not isinstance(results, list):
                print("Error: Results data must be a list.")
                return []

            return results

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: Results file contains invalid JSON.")
        return []

    except OSError:
        print("Error: Could not read results file.")
        return []