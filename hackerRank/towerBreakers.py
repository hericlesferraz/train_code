def towerBreakers(n, m):
    if m == 1:
        return 2
    if m > 1:
        if n%2 == 0:
            print('2')
            return 2
        else:
            print('1')
            return 1
    
towerBreakers(n=2, m=2)