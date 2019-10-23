# APIO 18 P2 Circle Selection
# Tissan Kugathas
# Ocotber 5 2019

circle = []
n = int(input())

if 1 <= n <= (3*10**5):
    for current in range(n):
        user_input = input()
        temp = user_input.split()
        if (-10**9) <= temp[0] and temp[1] <= (10**9) and temp[2] <= (10**9):
            circle.append(user_input)
