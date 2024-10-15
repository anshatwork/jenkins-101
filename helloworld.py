import sys

def validate_params():
    if len(sys.argv) != 3:
        raise ValueError("Name and age must be provided as arguments.")

    name = sys.argv[1]
    age = sys.argv[2]

    if not name:
        raise ValueError("Name is required.")
    if not age:
        raise ValueError("Age is required.")
    
    # Optional: Validate that age is a number
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Age must be a number.")

    print(f"Name: {name}, Age: {age}")

if __name__ == "__main__":
    try:
        validate_params()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)  # Non-zero exit code to indicate failure
