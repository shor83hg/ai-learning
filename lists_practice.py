num = [3, 17, 32, 6, 59]

for n in num:
    print(f'{n} в квадрате = {n**2}') 

print(sum(num))
print(sum(num) / len(num))

num.append(40)
print(num)
