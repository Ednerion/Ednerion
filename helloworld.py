#Простой калькулятор на 4 функции. Реализован с помощью if-else и цикл for
print(" 1: + ")
print(" 2: - ")
print(" 3: * ")
print(" 4: / ")
number = int(input("ввыберите функцию "))
if number == 1:
    print("Введите числа для суммирование: ")
    a = int(input("a "))
    b = int(input("b "))
    print(a+b)
            
if number == 2:
    print("Введите числа для вычетания: ")
    a = int(input("a "))
    b = int(input("b "))
    print(a-b)

if number == 3:
    print("Введите числа для умножения: ")
    a = int(input("a "))
    b = int(input("b "))
    print(a*b)

if number == 4:
    print("Введите числа для деления: ")
    a = int(input("a "))
    b = int(input("b "))
    print(a/b)

else:
   quit
   a = [1, 2, 3, 4, 5, 6]
   for x in a: 
       print(x)
  