n = int(input("Check this number: "))
# is_prime = True


def prime_checker(number):
    is_prime = True

    for i in range(2,9):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print('Tis a prime number')
    else:
        print('Not a prime')
            

         
                

        
              






     

prime_checker(number=n)