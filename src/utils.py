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