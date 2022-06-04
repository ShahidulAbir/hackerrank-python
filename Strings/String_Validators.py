if __name__ == '__main__':
    s = input()

    flag = 0
    for i in s:
        if i.isalnum():
            print("True")
            flag = 1
            break

    if flag == 0:
        print("False")

    flag = 0
    for i in s:
        if i.isalpha():
            print("True")
            flag = 1
            break

    if flag == 0:
        print("False")

    flag = 0
    for i in s:
        if i.isdigit():
            print("True")
            flag = 1
            break

    if flag == 0:
        print("False")

    flag = 0
    for i in s:
        if i.islower():
            print("True")
            flag = 1
            break

    if flag == 0:
        print("False")

    flag = 0
    for i in s:
        if i.isupper():
            print("True")
            flag = 1
            break

    if flag == 0:
        print("False")
