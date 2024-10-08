from libraries.NeverUsedStuff import *
from libraries.findInFile import *

# def create(filename):
#     with open(filename, 'w') as file:
#         text = input("Введите текст заметки: ")
#         file.write(text)
#     print(f"Заметка '{filename}' была создана.")
#
# def delete(filename):
#     if os.path.exists(filename):
#         os.remove(filename)
#         print(f"Заметка '{filename}' была удалена.")
#     else:
#         print(f"Заметка '{filename}' не найдена.")
#
# def find_by_word(filename, word):
#     if os.path.exists(filename):
#         with open(filename, 'r') as file:
#             content = file.read()
#             if word in content:
#                 print(f"Слово '{word}' найдено в заметке '{filename}'.")
#             else:
#                 print(f"Слово '{word}' не найдено в заметке '{filename}'.")
#     else:
#         print(f"Заметка '{filename}' не найдена.")

def main():
    while True:
        command = input("Введите команду (create, delete, find) или 'exit' для выхода: ")

        if command.lower() == 'exit':
            break

        text = command.split()
        if len(text) == 0:
            print("Некорректная команда. Попробуйте снова.")
            continue

        cmd = text[0].lower()

        if cmd == 'create' and len(text) == 2:
            create(text[1])
        elif cmd == 'delete' and len(text) == 2:
            delete(text[1])
        elif cmd == 'find' and len(text) == 3:
            print(find_by_word(text[1], text[2]))
        else:
            print("Некорректная команда. Используйте: create <filename>, delete <filename>, find <filename> <word>.")


main()
