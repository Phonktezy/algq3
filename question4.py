# #1
# class Student:
#
#
#  def __init__(self, n, a, ag):
#   self.n = n
#   self.a = a
#   self.ag = ag
#
#
# def set_n(self, n):
#  self.n = n
#
#
# def get_a(self):
#  return self.a
#
#
# def set_a(self, a):
#  self.a = a
#
#
# def get_ag(self):
#  return self.ag
#
#
# def set_ag(self, ag):
#  self.ag = ag
#
#
# x = Student("Иван", 20, 4.5)
# print(x.a) #методы для вывода данных: "a", "n", "average_grade"
# print(x.n)
# print(x.ag)

#2

#
# class Rectangle:


# def __init__(self, l, w):
#   self.l = l
#   self.w = w
#
#  def s(self):
#   return self.l * self.w
#
#  def p(self):
#   return 2 * (self.l + self.w)
#
# x = Rectangle(2 , 5.3)
# print(f"Площадь прямоугольника: {x.s()}")
# print(f"Периметр прямоугольника: {x.p()}")
# 3

# class Auto:
#
#  def __init__(self, n, m, y, c):
#   self.n = n
#   self.m = m
#   self.y = y
#   self.c = c
#
#  def display(self):
#   print(f'Brand: {self.n}')
#   print(f'Model: {self.m}')
#   print(f'Year: {self.y}')
#   print(f'Mileage: {self.c}')
#
# x = Auto ('Mazda', 'Rx-7', 1998, 52046)
# x.display()

#4

# class Bank:
#     def __init__(self, cn, bal):
#         self.cn = cn
#         self.bal = bal
#     def username(self):
#         print(f'Имя пользователя: {self.cn}')
#     def dep(self, a):
#         self.bal += a
#
#     def w(self, a):
#         if a > self.bal:
#             print("Недостаточно средств")
#         else:
#             self.bal -= a
#
#     def get_bal(self):
#         return self.bal
#
#
#
# x = Bank("Вася Пупкин", 1000)
# x.username()
# print(f"Текущий баланс: {x.get_bal()}")
#
# x.dep(200)
# print(f"После пополнения: {x.get_bal()}")
#
# x.w(54)
# print(f"Статус после обналичивания: {x.get_bal()}")

#5
# class Rectangle:
#     def __init__(self,fs,ss,ts):
#         self.fs = fs
#         self.ss = ss
#         self.ts = ts
#
#     def display(self):
#       if self.fs == self.ss == self.ts:
#           print(f"Данный треугольник является равносторонним", int((self.fs + self.ts + self.ss) / 2 ))
#       if self.fs == self.ss != self.ts:
#           print(f"Данный треугольник является равнобедренным", int((self.fs + self.ts + self.ss) / 2))
#       if self.fs != self.ss != self.ts:
#           print(f"Данный треугольник является разносторонним", int((self.fs + self.ts + self.ss) / 2))
#
# x = Rectangle(3, 3, 5)
# x.display()
