# Enter your code here. Read input from STDIN. Print output to STDOUT

size_of_family = int(input())
rooms = list(map(int, input().split()))

dictionary = dict()

for item in rooms:
    if item in dictionary:
        dictionary[item] += 1
    else:
        dictionary[item] = 1

for item in dictionary:
    if dictionary[item] == 1:
        print(item)
        break
