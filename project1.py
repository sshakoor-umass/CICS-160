#Sheik Shakoor

def is_prime(n):
    if n <= 1:
        return False
    #divisible numbers in between 2 and "n"
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def are_relatively_prime(x, y):
    #number cant a factor bigger than itself
    smallest = min(x, y)

    #any shared factors?
    for i in range(2, smallest + 1):
        if x % i == 0 and y % i == 0:
            return False

    return True

if __name__ == '__main__':
    print(is_prime(10))  
    print(is_prime(17))
    print(are_relatively_prime(10, 17))
    print(are_relatively_prime(21, 10))
