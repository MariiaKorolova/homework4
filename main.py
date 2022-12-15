1)У вас есть строка my_string = '0123456789'.
Сгенерировать целые числа (тип int) от 0 до 99 и распечатать их.
Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
Генерирование через range или другие "фишки" я засчитывать не буду ))

my_string = '0123456789'
result = []

for number_1 in my_string:
    for number_2 in my_string:
        result.append(int(number_1 + number_2))

print(result)

my_int = 200_300_400
something = 100

print(my_int)



2) При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
A
            *
          *   *
        *       *
      *           *
    *               *
  *                   *
* * * * * * * * * * * * *

n = int(input('Enter the high of triangle: '))
for rows in range(1, n + 1):
    for cols in range(1, 2 * n):
        if rows == n or rows + cols == n + 1 or cols - rows == n - 1:
            print('*', end='')
        else:
            print(end=' ')
    print()

B
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *

a = int(input('Enter the high of triangle: '))
for i in range(a):
    print(i, end='\t')
    for j in range((a - i)-1):
        print(end=" ")
    for j in range(i + 1):
        print("* ", end="")
    print()


C
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *                   *
    *               *
      *           *
        *       *
          *   *
            *
n=int(input("Enter the high of triangle :"))
for i in range(0,n+1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
if i==n:
    for i in range(n-1,0,-1):
        for j in range(0,n-i):
            print(end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print()


D
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *         *         *
    *       *       *
      *     *     *
        *   *   *
          * * *
            *
*