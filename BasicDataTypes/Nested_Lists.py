if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    lowest = 999999
    second_lowest = 999999
    names = []

    for record in records:
        if record[1] < lowest:
            lowest = record[1]

    for record in records:
        if lowest < record[1] < second_lowest:
            second_lowest = record[1]

    for record in records:
        if record[1] == second_lowest:
            names.append(record[0])

    names.sort()

    for name in names:
        print(name)
