import json
import sys

def validate_json(file_path):
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        print(f"JSON file at {file_path} is valid.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON file at {file_path}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading JSON file at {file_path}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    validate_json('ser-datasets.json')
