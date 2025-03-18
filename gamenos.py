def game_with_number (arr,  n) : 
    #Complete the fun
    n = len(arr)
    if n == 0:
        return []

    result = []
    
    for i in range(n - 1):
        result.append(arr[i] ^ arr[i + 1])
    

    result.append(arr[-1])
    
    return result