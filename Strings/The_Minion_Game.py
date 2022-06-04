def minion_game(string):
    # your code goes here
    length = len(string)
    kevin_points = 0
    stuart_points = 0

    for i in range(length):
        if string[i] in "AEIOU":
            kevin_points += (length - i)
        else:
            stuart_points += (length - i)

    if kevin_points > stuart_points:
        print("Kevin {}".format(kevin_points))
    elif kevin_points < stuart_points:
        print("Stuart {}".format(stuart_points))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
