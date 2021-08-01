def dec_to_bin(x):
    count = 0
    maxi = 0
    a = bin(x)[2:]
    for value in a:
        if value == '1':
            count += 1
        else:
            maxi = max(maxi, count)
            count = 0
    print(max(maxi, count))


dec_to_bin(int(input()))

