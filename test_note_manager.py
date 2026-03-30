import os
from main import NoteManager


def setup_function():
    # Clean up test file before each test
    if os.path.exists("notes.json"):
        os.remove("notes.json")


def test_add_note():
    manager = NoteManager()
    manager.add_note("Test note")

    assert len(manager.notes) == 1
    assert manager.notes[0]["text"] == "Test note"


def test_add_empty_note():
    manager = NoteManager()
    manager.add_note("")

    assert len(manager.notes) == 0


def test_delete_note():
    manager = NoteManager()
    manager.add_note("Delete me")

    manager.delete_note(0)

    assert len(manager.notes) == 0


def test_load_notes():
    manager = NoteManager()
    manager.add_note("Saved note")

    new_manager = NoteManager()
    new_manager.load_notes()

    assert len(new_manager.notes) == 1
    assert new_manager.notes[0]["text"] == "Saved note"