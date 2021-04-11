# Zadanie 1
chislo_1 = int(input("Введите целое число: "))
chislo_2 = int(input("Введите целое число 2: "))

stroka_1 = input("Введите текст: ")
stroka_2 = input("Введите текст 2: ")

print(f'chislo_1 =  {chislo_1}, chislo_2 = {chislo_2}, stroka_1 = {stroka_2}, stroka_2 = {stroka_2} ')

# Zadanie 2
sekundi = int(input("Введите количество секунд:"))
print(f"{sekundi // 3600}:{sekundi % 3600 // 60}:{sekundi % 60}")

# Zadanie 3
n = int(input("Введите число n:"))
print(f'n + nn + nnn = {n + n * 10 + n + n * 100 + n * 10 + n}')

# Zadanie 4
ostatok = 1
delenie_na = 0
celoe_chislo = int(input("Введите целое число:"))
while (ostatok > 0):
    ostatok = celoe_chislo // 10
    if delenie_na < (celoe_chislo % 10):
        delenie_na = celoe_chislo % 10
    celoe_chislo = celoe_chislo // 10
print(f'Самая большая цифра в числе: {delenie_na}')

# Zadanie 5
viruchka = float(input("Введите выручку:"))
izderzhki = float(input("Введите издержки:"))

if viruchka > izderzhki:
    sotrudniki = int(input("Введите количество сотрудников:"))
    print(f"Прибыль на сотрудника: {(viruchka - izderzhki) / sotrudniki}")
else:
    print("Издержки больше выручки")

# Zadanie 6
a = int(input("Введите сколько пробежали в км в первый день:"))
b = int(input("Сколько хотите в итоге пробежать? "))
c = 1
print(f'{c}-й день: {a}')
while (a < b):
    c += 1
    a *= 1.1
    print(f'{c}-й день: {a}')
