# 16 BIT S/W ONLY
# Tissan Kugathas
# May 27 2019

n = int(input())
product_numbers = []

if 1 <= n <= 1000:
    for n in range(n):
        product_numbers.append(input())
    for product in product_numbers:
        numbers = product.split(" ")
        status = False
        if (-2**31) <= int(numbers[0]):
            if int(numbers[1]) < (2**31):
                if (-2**63) <= int(numbers[2]) < (2**63):
                    status = True
        if status == True:
            if int(numbers[0])*int(numbers[1]) == int(numbers[2]):
                print("POSSIBLE DOUBLE SIGMA")
            else:
                print("16 BIT S/W ONLY")
