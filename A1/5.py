name = [""] * 10

for i in range(10):
    while True:
        name[i] = input(f"Enter name of student {i + 1}: ")
        name[i] = name[i][:15][::-1]  # Limit to 15 characters and reverse the name
        break

print(name)
