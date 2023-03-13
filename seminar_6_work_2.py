# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
from random import randint
def main():
    size = int(input('введите размер массива: '))
    min_value = int(input('min-значение: '))
    max_value = int(input('max-значение: '))
    lst=[randint(min_value, max_value) for _ in range(size)]
    print(lst)
    sort_lst(lst)

def sort_lst(lst, lst_2=None):
    min_element= int(input('min-диопазон: '))
    max_element= int(input('max-диопазон: '))
    list_2 = []
    for i in range(len(lst)):
       if min_element <= lst[i] <= max_element:
           list_2.append(i)
    print(f'итоговый список \t {list_2}')


if __name__ == '__main__':
    main()