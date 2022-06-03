if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        commands = list(input().split())

        if commands[0] == "insert":
            my_list.insert(int(commands[1]), int(commands[2]))
        elif commands[0] == "print":
            print(my_list)
        elif commands[0] == "remove":
            my_list.remove(int(commands[1]))
        elif commands[0] == "append":
            my_list.append(int(commands[1]))
        elif commands[0] == "sort":
            my_list.sort()
        elif commands[0] == "pop":
            my_list.pop()
        elif commands[0] == "reverse":
            my_list.reverse()
