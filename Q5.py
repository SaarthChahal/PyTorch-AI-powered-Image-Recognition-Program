class FloatStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

def main():
    stack = FloatStack()

    while True:
        print("\nOptions:")
        print("1. Push an element")
        print("2. Pop an element")
        print("3. Print all elements")
        print("4. Exit \n")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            value = float(input("Enter the value to push: "))
            stack.push(value)
            print(f"Pushed {value:.4f} onto the stack.")
        elif choice == "2":
            popped_value = stack.pop()
            if popped_value is not None:
                print(f"Popped {popped_value:.4f} from the stack.")
            else:
                print("Underflow")
        elif choice == "3":
            if not stack.is_empty():
                print("Stack Contents:")
                for item in reversed(stack.stack):
                    print(f"{item:.4f}")
            else:
                print("Stack is empty.")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

main()