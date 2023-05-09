"""ано число. Найти сумму и произведение его цифр.
"""

number = input("Enter number: ")
arr = list(number)
sum = 0
product = 1
for i in arr:
    sum += int(i)
    product *= int(i)
print(f"sum {sum}, product {product}")