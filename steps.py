import json

class BackendDeveloperChecklist:
    def __init__(self):
        self.checklist = []

    def add_item(self, item):
        self.checklist.append(item)

    def remove_item(self, item):
        if item in self.checklist:
            self.checklist.remove(item)
    
    def display_checklist(self):
        print("\nBackend Developer Checklist:")
        for i, item in enumerate(self.checklist, start=1):
            print(f"{i}. {item}")
    
    def save_to_file(self):
        with open("backend_checklist.json", "w") as file:
            json.dump(self.checklist, file)

    def load_from_file(self):
        try:
            with open("backend_checklist.json", "r") as file:
                self.checklist = json.load(file)
        except FileNotFoundError:
            print("No checklist file found. Starting with an empty checklist.")

# Initialize the checklist
checklist = BackendDeveloperChecklist()

# Load existing checklist items from file
checklist.load_from_file()

while True:
    print("\nOptions:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display checklist")
    print("4. Save checklist to file")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter the item to add: ")
        checklist.add_item(item)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        checklist.remove_item(item)
    elif choice == "3":
        checklist.display_checklist()
    elif choice == "4":
        checklist.save_to_file()
        print("Checklist saved to file.")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select a valid option.")

print("Exiting the checklist application.")