def print_rangoli(size):
    # your code goes here
    base = 97
    lines = 2 * size - 1
    mid = lines // 2
    columns = 4 * size - 3

    strings = []
    k = -2
    for i in range(lines):
        string = ""
        if i <= mid:
            for j in range(2 * i + 1):
                base_character = base + size - 1 - j
                second_mid = (2 * i + 1) // 2
                if j < second_mid:
                    string += chr(base_character) + "-"
                    base_character -= 1
                elif j == second_mid:
                    string += chr(base_character) + "-"
                    last_character = base_character
                else:
                    last_character += 1
                    string += chr(last_character) + "-"
            if i == mid:
                string = string[:-1]

            strings.append(string.center(columns, "-"))
            print(string.center(columns, "-"))

        else:
            print(strings[k])
            k -= 1


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
