#1 is_prime(n) – Check if a number is prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#2 digit_sum(k) – Sum of the digits of a number

def digit_sum(k):
    return sum(int(d) for d in str(k))


#3 Print all powers of 2 not exceeding N

def powers_of_two(N):
    power = 1
    while power <= N:
        print(power, end=" ")
        power *= 2


def powers_of_two(N):
    power = 2
    while power <= N:
        print(power, end=" ")
        power *= 2
