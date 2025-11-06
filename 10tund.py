def read_from_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
    return content

read_from_file("todo.txt")