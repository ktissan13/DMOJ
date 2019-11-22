N = int(input())
integer = input()
integers = integer.split(' ')

if 1 <= N <= 1000000:
    highest_num = integers[0]
    lowest_num = integers[0]
    for index in range(1,len(integers)):
        if -10**9 <= int(integers[index]) <= 10**9:
            if int(highest_num) < int(integers[index]):
                highest_num = int(integers[index])
            if int(lowest_num) > int(integers[index]):
                lowest_num = int(integers[index])
    r = int(highest_num) - int(lowest_num)
    print(r)
