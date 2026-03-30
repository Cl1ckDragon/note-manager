import json

class NoteManager:
    def __init__(self):
        self.notes =[]
        self.file_name = "notes.json"

    def load_notes(self):
        try:
            with open(self.file_name, "r") as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []

    def save_notes(self):
        with open(self.file_name, "w") as file:
            json.dump(self.notes, file)

    def add_note(self, note):
        if not note.strip():
            print("Note cannot be empty")
            return
        self.notes.append(note)
        print("Note added!")

    def view_notes(self):
        if not self.notes:
            print("No notes available!")
            return
        
        for index, note in enumerate(self.notes, start = 1):
            print(f"{index}. {note}")

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            removed = self.notes.pop(index)
            print(f"Deleted: {removed}")
        else:
            print("Invalid note number!")

    
def main():
    manager = NoteManager()
    manager.load_notes()

    while True:
        print("\n--- Note Manager ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            note = input("\nEnter note: ")
            manager.add_note(note)

        elif choice == "2":
            manager.view_notes()

        elif choice == "3":
            try:
                index = int(input("Enter note number to delete: ")) - 1
                manager.delete_note(index)
            except ValueError:
                print("\nPlease enter a valid number!")

        elif choice == "4":
            manager.save_notes()
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please try again!")

if __name__ == "__main__":
    main()