from persia.riddle import error_messages
import persia
# imports the error_messages from persia.riddle

text = persia.var # gets a variable in the persia init module
print(text) # prints it

def main():
    try:
        raise ValueError("Invalid input") #  raise an error
    except Exception as e:
        error_message = error_messages.get(type(e), lambda e: "Unknown error") # get an error message from the .riddle module
        print(error_message)

if __name__ == "__main__":
    main()