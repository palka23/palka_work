import math
def function_name():
  print("какое действие желаете выполнить?")
  print("1.сложение")
  print("2.вычетание")
  print("3.умножение")
  print("4.деление")
  plan = int(input("введите число от 1 до 4"))
  if plan==1:
    a = int(input("введите первое число"))
    b = int(input("введите второе число"))
    print(a + b)
  if plan==2:
    a = int(input("введите первое число"))
    b = int(input("введите второе число"))
    print(a - b)
  if plan==3:
    a = int(input("введите первое число"))
    b = int(input("введите второе число"))
    print(a * b)
  if plan==4:
    a = int(input("введите первое число"))
    b = int(input("введите второе число"))
    print(a/b)
function_name()
