def add_to_file(file_path):
    with open(file_path, 'a', encoding="utf-8") as file:
        new_task = "dear god I found a thing in kv.ee for 1 euro"
        file.write("\n" + new_task)

add_to_file("todo.txt")