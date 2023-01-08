def is_prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True   


def successor(n):
    return n + 1    

if __name__ == '__main__':
    for i in range(20):
        print(i, 'is prime? ', is_prime(successor(i)))    
