import pandas as pd
from matplotlib import pyplot as plt

# Пункт 1
# Створіть DataFrame з ім'ям "students", який містить такі стовпці:
# "Name" (ім'я студента)
# "Age" (вік студента)
# "Gender" (стать студента)
# "Score" (оцінка студента за певний предмет)
data = {
    "Name": ["Дар'я", "Марія", "Петро", "Олена", "Анна"],
    "Age": [20, 22, 21, 19, 23],
    "Gender": ["Чоловік", "Жінка", "Чоловік", "Жінка", "Жінка"],
    "Score": [85, 92, 78, 88, 95]
}

students = pd.DataFrame(data)

# print(students)

# Пункт 2
# Підготуйте дані для графіку (наприклад, кількість продаж за місяць або результати тестування студентів).
# Використовуючи бібліотеку Matplotlib, створіть графік для відображення цих даних. Виберіть відповідний
# тип графіку (лінійний, стовпчиковий, круговий тощо), підпишіть осі, додайте заголовок та легенду.

# name_students = students["Name"]
# score_students = students["Score"]
#
# # Створення стовпчикового графіку
# plt.figure(figsize=(8, 5))
# plt.bar(name_students, score_students, color='green')
# plt.xlabel("Ім'я студента")
# plt.ylabel("Оцінка")
# plt.title("Середні бали студентів")
# plt.xticks(rotation=45)
# plt.tight_layout()
#
# plt.legend(["Оцінки"])
#
# plt.show()

# Пункт 3
# Виведіть перші 5 рядків з DataFrame "students".
# students_head = students.head(5)
# print(students_head)

# Пункт 4
# Створіть графік для відображення залежності між двома змінними.
# Наприклад, це може бути діаграма розсіювання (scatter plot), де по одній вісі буде відображена одна змінна,
# а по іншій - інша змінна. Додайте легенду та підпишіть осі.

# age = students["Age"]
# score = students["Score"]
#
# plt.figure(figsize=(8, 5))
# plt.scatter(age, score, color='skyblue', marker='o')
# plt.xlabel("Вік студента")
# plt.ylabel("Оцінка")
# plt.title("Залежність між віком та оцінками студентів")
# plt.grid(True)
#
# plt.legend(["Залежність"])
#
# plt.show()

# Пункт 5
# Створіть графік для відображення категоріальних даних, наприклад, розподілу кількості
# об'єктів за певною категорією. Використайте стовпчиковий графік або кругову діаграму для цього завдання.
# Підпишіть категорії, осі та додайте заголовок.

data = {
    "Name": ["Іван", "Марія", "Петро", "Олена", "Анна", "Оксана", "Вова"],
    "Спеціальність": ["Психологія", "Медицина", "Медицина", "Психологія", "Економіка", "Хімія", "Соціалогія"]
}

students = pd.DataFrame(data)

# Підрахунок кількості студентів за кожною спеціальністю
specialization = students["Спеціальність"].value_counts()

# Дані для графіку
category = specialization.index
students_quantity = specialization.values

# Створення кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(students_quantity, labels=category, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Забезпечення кругової форми діаграми
plt.title("Розподіл студентів за спеціальностями")

# Відображення графіку
plt.show()
