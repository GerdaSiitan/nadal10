def task_number(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        nr  = 1
        for line in file:
            print(str(nr) + ". " + line.strip())
            nr += 1

task_number("todo.txt")

# loend = ["wrw", "sf", "femk", 432, 243, 543]
# for i in loend:
#     print(i)