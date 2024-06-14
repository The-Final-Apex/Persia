from puns import error_messages

def main():
    try:
        raise ValueError("Invalid input")
    except Exception as e:
        error_message = error_messages.get(type(e), lambda e: "Unknown error")
        print(error_message)

if __name__ == "__main__":
    main()