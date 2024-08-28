import os


def create(filename: str):
    # name = input('note name:\n')
    with open(f"{filename}.txt", "w") as edit:
        input_text_saves = input('start typing:\n')
        edit.write(input_text_saves)
        edit.close()


def delete(filename: str):
    # name = input('enter name of note, you want to delete:\n')
    os.remove(f'{filename}.txt')
