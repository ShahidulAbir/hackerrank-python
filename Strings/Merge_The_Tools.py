def merge_the_tools(string, k):
    # your code goes here
    substrings = []
    position = 0

    for i in range(len(string) // k):
        substrings.append(string[position: position + k])
        position = position + k

    modified_substrings = []
    for substring in substrings:
        temp = ""
        for character in substring:
            if not character in temp:
                temp += character

        modified_substrings.append(temp)

    for substring in modified_substrings:
        print(substring)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
