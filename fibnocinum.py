def fibonacci(n):
    #your code he
    if n <= 0:
        return "Invalid input"  
    elif n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
