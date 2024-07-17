def lonelyinteger(a):
    for index in range(0, len(a), 1):
        current_number = a[index]
        array_tmp = a[0:index] + a[index+1:]
        n = 0

        while n < len(a)-1:
            if current_number == array_tmp[n]:
                break
            else:
                n += 1

        if n == len(a) - 1:
            return current_number
        
lonelyinteger([1, 2, 3, 5, 3, 2, 1])