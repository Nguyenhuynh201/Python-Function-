
def is_prime(n):
    """Function to check for prime number"""
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for testnumber in range (2,n):
            if (n % testnumber ) == 0:
                return False
        return True

import random
def six_random_number():
    number1 = random.randrange(1, 100)
    number2 = random.randrange(1, 100)
    number3 = random.randrange(1, 100)
    number4 = random.randrange(1, 100)
    number5 = random.randrange(1, 100)
    number6 = random.randrange(1, 100)
    return (number1, number2, number3, number4, number5, number6)
    
number1, number2, number3, number4, number5, number6 = six_random_number()

if is_prime(number1) == True:
    print(f"The randome number {number1} is a prime number" )
else:
    print(f"The randome number {number1} is not a prime number")

if is_prime(number2) == True:
    print(f"The randome number {number2} is a prime number" )
else:
    print(f"The randome number {number2} is not a prime number")


if is_prime(number3) == True:
    print(f"The randome number {number3} is a prime number" )
else:
    print(f"The randome number {number3} is not a prime number")


if is_prime(number4) == True:
    print(f"The randome number {number4} is a prime number" )
else:
    print(f"The randome number {number4} is not a prime number")


if is_prime(number5) == True:
    print(f"The randome number {number5} is a prime number" )
else:
    print(f"The randome number {number5} is not a prime number")

if is_prime(number6) == True:
    print(f"The randome number {number6} is a prime number" )
else:
    print(f"The randome number {number6} is not a prime number")


    
    
