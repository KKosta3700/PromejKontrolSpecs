import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

COMMANDS = {
    "add": ["добавить", "add"],
    "read": ["показать", "read"],
    "update": ["обновить", "update"],
    "delete": ["удалить", "delete"],
    "edit": ["редактировать", "edit"],
    "exit": ["выход", "exit"]
}


def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r", encoding='utf-8') as file:
            return json.load(file)
    else:
        return []


def save_notes(notes):
    with open(NOTES_FILE, "w", encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)


def add_note():
    notes = load_notes()
    title = input("Введите заголовок заметки: ").strip()
    body = input("Введите текст заметки: ").strip()
    note = {
        "id": str(datetime.now().timestamp()),  # Просто для примера
        "title": title,
        "body": body,
        "created_at": str(datetime.now())
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")


def read_notes():
    notes = load_notes()
    print("Список заметок:")
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['body']}, Создана: {note['created_at']}")


def update_note():
    notes = load_notes()
    note_id = input("Введите ID заметки для обновления: ").strip()
    for note in notes:
        if note['id'] == note_id:
            new_body = input("Введите дополнение к тексту заметки: ").strip()
            note['body'] += "\n" + new_body
            note['last_modified_at'] = str(datetime.now())
            save_notes(notes)
            print("Заметка успешно обновлена.")
            return
    print("Заметка с таким ID не найдена.")


def edit_note():
    notes = load_notes()
    note_title = input("Введите заголовок заметки для редактирования: ").strip()
    for note in notes:
        if note['title'] == note_title:
            new_body = input("Введите новый текст заметки: ").strip()
            note['body'] = new_body
            note['last_modified_at'] = str(datetime.now())
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с таким заголовком не найдена.")


def delete_note():
    notes = load_notes()
    note_id = input("Введите ID заметки для удаления: ").strip()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена.")


def process_command(command):
    for cmd, aliases in COMMANDS.items():
        if command.lower() in aliases:
            return cmd
    return None


def main():
    while True:
        print("\nВведите команду (добавить/показать/обновить/редактировать/удалить/выход):")
        command = input().strip()
        command = process_command(command)
        if command == "add":
            add_note()
        elif command == "read":
            read_notes()
        elif command == "update":
            update_note()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "exit":
            print("Программа завершена.")
            break
        else:
            print("Некорректная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
