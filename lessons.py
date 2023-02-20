text = 1
while text == 1:
    number = int(input("введите трехзначное число :"))
    if number < 1000 and number > 99:
        value_1 = number // 100
        value_2 = number // 10 % 10
        value_3 = number % 10
        print(f' сумма цифер равна :  {value_1 + value_2 + value_3}')
        text = int(input('введите "1" если хотите повторить операицю \n  иначе "0"  '))
    else:
        print("ошибка не правильный ввод !")
