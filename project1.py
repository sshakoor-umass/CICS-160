#Sheik Shakoor

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
def are_relatively_prime(x, y):
    smallest = min(x, y)

    for i in range(2, smallest + 1):
        if x % i == 0 and y % i == 0:
            return False

    return True
print(is_prime(10))  
print(is_prime(17))  
print(are_relatively_prime(10, 17))  
print(are_relatively_prime(21, 10))  
