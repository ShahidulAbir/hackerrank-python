if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr2 = list(arr)
    arr2 = list(dict.fromkeys(arr2))
    arr2.sort()
    print(arr2[-2])
