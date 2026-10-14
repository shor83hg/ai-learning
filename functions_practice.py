def is_even(n):
    return n % 2 == 0

result = is_even(8)
print(result)
result = is_even(55)
print(result)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print(calculate_average([56, 93, 5, 2]))
print(calculate_average([7, 90, 3, 51]))


def describe_user(name, age, city="не указан"):
    return f"{name}, {age} года, город: {city}"

print(describe_user("Александр", 42))    
print(describe_user("Александр", 42, "Москва"))

