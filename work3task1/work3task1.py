text = input("Введіть рядок з кількістью символів більше 15: ")
while len(text) <= 15:
    text = str(input("Введіть ще раз рядок з кількістью символів більше 15: "))
slice_text = text[11:14] 
print("Вибраний зріз:", slice_text)
