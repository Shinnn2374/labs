import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random



# Функция для разделения на шаги
def delitel():
    print('___________________________________________')


# Указываем путь к файлу Excel
file_path = '/Users/mihail/Desktop/data/zalupa/student_data.xlsx' # Будет необходимо вставить свой путь к файлу( правой кнопкой на файл, copy path, копируем полный путь)

# Читаем файл и загружаем данные в переменную 'df'
df = pd.read_excel(file_path)
df_copy = df.copy()

def delitel():
    print('___________________________________________')

#ЧАСТЬ 2 ШАГ 1 И 2(Кроме чтения файла)
print(df_copy.head()) # Вывод 5 первых строк таблицы
delitel()
print(df_copy.info) ## Вывод полной таблицы(так как в ide не будет выводится вся таблица, вывод первых и последних 5 строк)
delitel()
print(df_copy.describe()) # Получает базовую статистику: среднее, максимальное и минимальное значения, стандартное отклонение и т.д.
delitel()

# ВТОРАЯ ЧАСТЬ(ГРАФИКИ)(Разбери плотно команды, потому что я сам с этим ток начал работать и тонкости рассказать не смогу)
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Факультет', palette='viridis')
plt.title("Распределение студентов по факультетам")
plt.xlabel("Факультет")
plt.ylabel("Количество студентов")
plt.xticks(rotation=45)  # Поворачиваем метки по оси X для удобства
plt.show()

#ЧАСТЬ 3(Глубокий анализ(лучше бы глубокий ...ет))


# Настраиваем стиль и размер графика
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
# Строим гистограмму для столбца "Возраст"
sns.histplot(df['Возраст'], bins=10, kde=True, color='skyblue')
plt.title("Распределение студентов по возрасту")
plt.xlabel("Возраст")
plt.ylabel("Количество студентов")
plt.show()

#ШАГ 2
# Строим "box plot" для среднего балла по факультетам
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Факультет', y='Средний балл', palette='coolwarm')
plt.title("Распределение среднего балла по факультетам")
plt.xlabel("Факультет")
plt.ylabel("Средний балл")
plt.xticks(rotation=45)
plt.show()
#ШАГ 3

# Получаем данные для круговой диаграммы
city_counts = df['Город проживания'].value_counts()

# Строим круговую диаграмму
plt.figure(figsize=(8, 8))
plt.pie(city_counts, labels=city_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Распределение студентов по городам проживания")
plt.show()

#ШАГ 4

# Строим strip plot для среднего балла по форме обучения
plt.figure(figsize=(10, 6))
sns.stripplot(data=df, x='Форма обучения', y='Средний балл', jitter=True, palette='viridis')
plt.title("Средний балл в зависимости от формы обучения")
plt.xlabel("Форма обучения")
plt.ylabel("Средний балл")
plt.show()

#ЧАСТЬ 4 Создание и заполнение Excel-файла данными с помощью библиотеки Faker

#Шаг 1: Установка библиотеки Faker
#Шаг 2: Настройка кода для генерации данных

# Создаем объект Faker для генерации данных
fake = Faker('ru_RU')  # Устанавливаем язык на русский

# Задаем данные для факультетов и форм обучения
faculties = ["Журналистика", "Экономика", "Информатика", "Математика", "Филология"]
specialities = {
    "Журналистика": ["Медиа", "Печатные СМИ", "Радиожурналистика"],
    "Экономика": ["Бухгалтерия", "Финансовый анализ", "Экономическая теория"],
    "Информатика": ["Программирование", "Сети", "Базы данных"],
    "Математика": ["Прикладная математика", "Теоретическая математика", "Статистика"],
    "Филология": ["Русский язык", "Иностранные языки", "Литература"]
}
forms_of_study = ["Очная", "Заочная"]

# Генерируем данные для 200 студентов
students_data = []
for _ in range(200):
    faculty = random.choice(faculties)
    speciality = random.choice(specialities[faculty])
    student = {
        "ФИО": fake.name(),
        "Возраст": random.randint(17, 30),
        "Факультет": faculty,
        "Дата зачисления": fake.date_this_decade(),
        "Средний балл": round(random.uniform(3.0, 5.0), 2),
        "Город проживания": fake.city(),
        "Специальность": speciality,
        "Телефон": fake.phone_number(),
        "Электронная почта": fake.email(),
        "Общежитие": random.choice(["Есть", "Нет"]),
        "Форма обучения": random.choice(forms_of_study)
    }
    students_data.append(student)

# Конвертируем данные в DataFrame для сохранения в Excel
df = pd.DataFrame(students_data)

# Сохраняем DataFrame в Excel-файл
df.to_excel("students_data.xlsx", index=False)
print("Данные успешно сгенерированы и сохранены в файл student_data.xlsx")

#Шаг 3: Запуск кода и проверка данных

