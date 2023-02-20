text = 1
while text == 1:
    ticket = int(input('ввеите номер билета :'))
    number = ticket // 1000
    number_1 = number // 100
    number_2 = (number // 10) % 10
    number_3 = number % 10
    number = ticket % 1000
    number_4 = number // 100
    number_5 = (number // 10) % 10
    number_6 = number % 10
    if (number_1 + number_2 + number_3) == (number_4 + number_5 + number_6):
        print('поздравляю это счатливый билет ')
    else:
        print('увы вам не повезло ')
    text = int(input('введите "1" если хотите повторить операицю |_____| иначе "0"  '))
