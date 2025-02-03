import json

def read_json_from_file(filepath):
    """
    Reads JSON data from a file.

    Args:
        filepath: The path to the JSON file.

    Returns:
        A Python object (usually a dictionary or list) representing the JSON data,
        or None if an error occurs (e.g., file not found, invalid JSON).
        Prints an error message to the console if there's a problem.
    """

    try:
        with open(filepath, 'r', encoding='utf-8') as f:  # Use 'r' for reading, utf-8 encoding
            data = json.load(f) # Parse the JSON data
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filepath}")
        return None
    except Exception as e: # Catching a broader range of potential errors
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    file_path = "data.json"  # Replace with your file path
    json_data = read_json_from_file(file_path)

    if json_data:
        print("JSON data loaded successfully:")
        # Process the data as needed. Here are some examples:
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                print(f"{key}: {value}")
        elif isinstance(json_data, list):
            for item in json_data:
                print(item)
        else:  # Handle other JSON structures if needed
            print("JSON data is not a dictionary or a list.")

        # Example of accessing specific data (if it's a dictionary)
        # if isinstance(json_data, dict) and "name" in json_data:
        #     name = json_data["name"]
        #     print(f"Name: {name}")
    else:
        print("Failed to load JSON data.")