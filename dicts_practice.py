user = {
    "name": "Александр",
    "age": 42,
    "city": "Москва",
    "skills": ["Python", "Git", "Linux"]
}
for key, value in user.items():
    print(f"{key}: {value}")

user["goal"] = "AI Automation Engineer"

print(user.get("email", "не указан"))

N = len(user["skills"])
print(f"Навыков: {N}")