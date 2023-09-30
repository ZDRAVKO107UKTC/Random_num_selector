import random

with open("Students.txt") as file:
    content = file.readlines()

chosen_students = []

while True:
    if content:
        if len(content) == 1:
            random_index = 0 
        else:
            random_index = random.randint(0, len(content) - 1)

        student = content.pop(random_index).strip()
        chosen_students.append(student)
        print(f"Chosen student: {student}")
    else:
        print("Everyone was chosen.")
        break

    again = input("Do you want to chose anoder number (y/n): ")
    if again.lower() != 'y':
        break

# Запис на избраните ученици във файл "Chosen.txt"
with open("Chosen.txt", "w") as chosen_file:
    chosen_file.write("\n".join(chosen_students))

print("END")
