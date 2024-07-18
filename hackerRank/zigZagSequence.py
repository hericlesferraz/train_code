def findZigZagSequence(a, n):
    a.sort()
    mid = (n - 1) // 2
    print(mid)
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2 
    while st < ed:
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')

findZigZagSequence(a=[1, 2, 3, 4, 5, 6, 7, 8], n=8)

def towerBreakers(n, m):
    # Write your code here
    if m == 1:
        return 2
    if m > 1:
        if n%2 == 0:
            return 2
        else:
            return 1