'''Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

minimum = int(input("enter minimum: "))
maximum = int(input("enter maximum: "))

n = int(input("enter number of elements (N): "))
my_list = []
res_list = []
print("enter elements of a list: ")
for i in range(n):
    new_number = int(input())
    my_list += [new_number]
    if new_number in range(minimum, maximum+1):
        res_list+=[i]

print("Вы ввели следующий список: ", my_list)
print("Элементы, находящиеся в заданном диапазоне: ", res_list)