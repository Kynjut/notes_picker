import os


def create():
    name = input('note name:\n')
    with open(f"{name}.txt", "w") as edit:
        input_text_saves = input('start typing:\n')
        edit.write(input_text_saves)
        edit.close()


def delete():
    name = input('enter name of note, you want to delete:\n')
    os.remove(f'C:\\Users\\admin\\Documents\\GitHub\\notes_picker\\pythonProject30\\{name}.txt')


create()
delete()
