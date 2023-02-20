text = 1
while text == 1:
    n = int(input('введите размер шаколадки m*n : '))
    m = int(input('введите размер шаколадки m*n : '))
    k = int(input('введите размер долек :'))
    if k < n * m and (k % n == 0 or k % m == 0):
        print("YES")
    else:
        print("NO")
    text = int(input('введите "1" если хотите повторить операицю |_____| иначе "0"  '))
