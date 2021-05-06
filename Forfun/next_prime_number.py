def next_prime_number(number):
    def check_prime(num):
        count = 2
        while(count <= int(num/2)):
            if(num % count == 0):
                return True
            count += 1
        else:
            return False

    number += 1
    while(check_prime(number)):
        number += 1

    return number
