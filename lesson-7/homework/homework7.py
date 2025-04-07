#1.
def is_prime(n):
    if n > 0:
        for i in range(2, n):
            if (n % i) == 0:
                print("False")
                break
        else:
            print("True")
    else:
        print("True")

is_prime(4)
is_prime(7)

#2.
def digit_sum(k):
    sum = 0
    for digit in str(k):
        sum +=int(digit)
    return sum

k = int(input('Enter number to get sum: '))

print(digit_sum(k))

#3.
def Ikkininig_daraja(n):
    Mening_royxatim = []
    for j in range(0, n):
        number = 2 ** j
    Mening_royxatim.append(number)
    return Mening_royxatim

Ikkininig_daraja(12)
