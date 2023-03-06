def main():
    a = int(input('a: '))
    b = int(input('b: '))
    print(f'{a} + {b} = {recursion(a, b)}')


def recursion(a, b):
    if b !=0:
        return recursion(a,b-1)+1
    if b == 0:
        return a               \
            # + recursion(a, b - 1)


if __name__ == '__main__':
    main()