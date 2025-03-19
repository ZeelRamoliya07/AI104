# Length function
def len_(s):
    count = 0
    for x in s:
        count += 1
    return count


# Count occurrences of a substring
def count_(s, sub):
    len_s = len_(s)
    len_sub = len_(sub)
    count = 0

    for i in range(len_s - len_sub + 1):
        if s[i: i + len_sub] == sub:   # String Slicing to compare with substring
            count += 1
    return count


# rsplit function
def rsplit_(s, sep=" ", maxsplit=-1):
    if sep == "":
        raise ValueError("Empty separator")

    result = []  
    temp = ""
    s_len = len_(s)
    sep_len = len_(sep)
    split_count = 0   
    i = s_len - 1   # Start from the end of the string

    while i >= 0:
        if maxsplit != -1 and split_count >= maxsplit:
            result.append(s[:i + 1])  # Add the remaining part of the string
            break

        if i - sep_len + 1 >= 0 and s[i - sep_len + 1: i + 1] == sep:
            result.append(temp[::-1])  # Append current temp in reverse
            temp = ""
            i -= sep_len
            split_count += 1
        else:
            temp += s[i]
            i -= 1

    result.append(temp[::-1])  # Append the remaining part
    return result[::-1]


# rindex (raises ValueError if not found)
def rindex_(s, sub, start=0, end=None):
    if end is None:
        end = len_(s)

    len_sub = len_(sub)

    for i in range(end - len_sub, start - 1, -1):
        if s[i: i + len_sub] == sub:
            return i

    raise ValueError("substring not found")


# rfind (returns -1 if not found)
def rfind_(s, sub, start=0, end=None):
    if end is None:
        end = len_(s)

    len_sub = len_(sub)

    for i in range(end - len_sub, start - 1, -1):
        if s[i: i + len_sub] == sub:
            return i
    return -1


# Replace occurrences of a substring with another substring
def replace_(s, old, new):
    result = ""
    len_s = len_(s)
    len_old = len_(old)
    i = 0

    while i < len_s:
        if s[i:i + len_old] == old:
            result += new  # Append the new substring
            i += len_old   # Skip the length of the old substring
        else:
            result += s[i]  # Append the current character
            i += 1
    return result


# Menu-driven interface
def main():
    while True:
        print("\n=+=+=+=+=+=+=+=+=+=+= STRING FUNCTION MENU =+=+=+=+=+=+=+=+=+=+=")
        print("1. Count occurrences of a substring")
        print("2. Find last occurrence (rfind)")
        print("3. Split string from right (rsplit)")
        print("4. Find last occurrence (rindex)")
        print("5. Replace a substring")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            s = input("Enter the string: ")
            sub = input("Enter the substring: ")
            print("Count:", count_(s, sub))

        elif choice == '2':
            s = input("Enter the string: ")
            sub = input("Enter the substring: ")
            try:
                start = int(input("Enter start index (default is 0): ") or 0)
                end = input("Enter end index (default is end of string): ")
                end = int(end) if end else len_(s)
                print("Last occurrence index (or -1 if not found):", rfind_(s, sub, start, end))
            except ValueError:
                print("Invalid input. Please enter a valid integer for start or end.")

        elif choice == '3':
            s = input("Enter the string: ")
            sep = input("Enter the separator (default is space): ") or " "
            try:
                maxsplit = input("Enter max splits (-1 for all): ")
                maxsplit = int(maxsplit) if maxsplit.isdigit() or maxsplit == "-1" else -1
                print("Split result:", rsplit_(s, sep, maxsplit))
            except ValueError:
                print("Invalid input. Please enter a valid integer for maxsplit.")

        elif choice == '4':
            s = input("Enter the string: ")
            sub = input("Enter the substring: ")
            try:
                start = int(input("Enter start index (default is 0): ") or 0)
                end = input("Enter end index (default is end of string): ")
                end = int(end) if end else len_(s)
                try:
                    print("Last occurrence index:", rindex_(s, sub, start, end))
                except ValueError as e:
                    print(e)
            except ValueError:
                print("Invalid input. Please enter a valid integer for start or end.")

        elif choice == '5':
            s = input("Enter the string: ")
            old = input("Enter the substring to replace: ")
            new = input("Enter the new substring: ")
            print("Replaced string:", replace_(s, old, new))

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


# Run the program
main()
