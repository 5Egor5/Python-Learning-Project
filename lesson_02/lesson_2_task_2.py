def dev_by_three(x):
    x = int(x)
    if (x % 4 == 0):
        print("год", x, ": ", True)
    else:
        print("год", x, ": ", False)


dev_by_three(input())
