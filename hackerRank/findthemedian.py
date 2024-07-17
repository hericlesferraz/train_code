
def findMedian(arr):
    arr.sort()
    
    # Encontrar o índice do elemento mediano
    median_index = (len(arr) - 1) // 2
    
    # Retornar o elemento mediano
    
    return arr[median_index]

# def findMedian(arr):
#     avg = int(sum(arr)/len(arr))
    
#     print(avg)
#     return avg
if __name__ == '__main__':

    #n = int(input().strip())

    #arr = list(map(int, input().rstrip().split()))
    arr = [0, 1, 2, 4, 6, 5, 3]
    result = findMedian(arr)
