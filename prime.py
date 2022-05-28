def is_prime(number: int) -> bool:

    if(number <= 0):
        return False

    if(number == 1):
        return True

    i: int
    i = 2
    while i < number:
        if (number % i == 0):
            return False
        i +=1
    return True


if __name__ == "__main__":

    print('Enter a number: ')
    number = input()
    number = int(number)

    if(is_prime(number)):
        print('The number', number, 'is prime.')
    else:
        print('The number', number, 'is not prime.') 