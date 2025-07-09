import os

class MessageWriter:
    def __init__(self, file_path="messages.txt"):
        self.file_path = file_path

    def send_message(self, message):
        """Appends a message to the text file."""
        try:
            with open(self.file_path, "a", encoding="utf-8") as file:
                file.write(message + "\n")
            print("Message written successfully.")
        except IOError as e:
            print(f"Error writing message: {e}")

    def read_messages(self):
        """Reads all messages from the file."""
        if not os.path.exists(self.file_path):
            print("No messages found.")
            return

        with open(self.file_path, "r", encoding="utf-8") as file:
            print("Messages:")
            for line in file:
                print(line.strip())

if __name__ == "__main__":
    writer = MessageWriter()

    while True:
        print("\nOptions:")
        print("1. Send a message")
        print("2. View messages")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            msg = input("Enter your message: ")
            writer.send_message(msg)
        elif choice == "2":
            writer.read_messages()
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")
