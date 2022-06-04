import textwrap


def wrap(string, max_width):
    start = 0
    length = len(string)
    new_string = ""

    while start < length:
        if start + max_width > length - 1:
            new_string += (string[start:] + "\n")
        else:
            new_string += (string[start:start + max_width] + "\n")

        start += max_width

    return new_string


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
