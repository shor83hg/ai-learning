num = int(input())

if num % 2 == 0 and num > 0:
    print("Четное, положительное")
elif num % 2 != 0 and num > 0:
    print("Нечетное, положительное")
elif num % 2 == 0 and num < 0:
    print("Четное, отрицательное")
elif num % 2 != 0 and num < 0:
    print("Нечетное, отрицательное")
else:
    print("Ноль")