"""Рассчитать месячные выплаты (m) и суммарную выплату (s) по кредиту.
О кредите известно, что он составляет n рублей, берется на y лет, под p процентов.
n, y, p - вводятся с клавиатуры. Месячные выплаты находятся по формуле:
m = (n * p * (1 + p)y) / (12 * ((1 + p)y – 1)),
где p выражается в долях единицы, а не процентах.
Суммарная выплата представляет собой выплаты за все месяцы каждого года:
s = (m * 12) * y
"""

loan_sum = input("Enter sum: ")
loan_sum = int(loan_sum)
years = input("Enter years: ")
years = int(years)
percent = input("Enter percent: ")
percent = float(percent)
m = ((loan_sum * percent * ((1 + percent) ** years)) / (12 * (((1 + percent) ** years) - 1)))
s = m * 12 * years
print(f"Месячная выплата {m} Суммарная выплата {s}")