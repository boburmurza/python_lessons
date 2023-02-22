def power_of_two(n):
    i = 0
    power = 1
    while 2 * power <= n:
        power *= 2
        i += 1
        print(i, '|\t', power)

N = int(input('введите огроничения : '))
power_of_two(N)
