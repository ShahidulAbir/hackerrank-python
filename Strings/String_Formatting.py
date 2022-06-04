def print_formatted(number):
    # your code goes here
    max_length = len(bin(number)[2:])
    for i in range(number):
        value = i + 1

        decimal = str(value)
        octal = oct(value)[2:]
        hexadecimal = (hex(value)[2:]).upper()
        binary = bin(value)[2:]

        print("{} {} {} {}".format(decimal.rjust(max_length), octal.rjust(max_length), hexadecimal.rjust(max_length),
                                   binary.rjust(max_length)))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
