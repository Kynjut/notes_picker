def find_by_text_part(filename, text_part: str):
    lines = read_file_lines(filename)
    text = ''.join(lines)
    return text_part in text


def find_by_word(filename, word: str):
    lines = read_file_lines(filename)
    separated_files = [i.split() for i in lines]

    words = []
    for words_part in separated_files:
        words += words_part

    return word in words


def read_file_lines(filename: str):
    with open(filename, 'r') as f:
        return f.readlines()
