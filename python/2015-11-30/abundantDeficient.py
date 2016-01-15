import sys

def getDivisors(z):
    '''
    Inefficient for huge numbers.
    '''
    for i in range(1, int(z/2)+1):
        if z % i == 0:
            yield i

# First argument is count of numbers to analyze
for x in range(2, int(sys.argv[1]) + 2):
    divisorSum = 0
    number = int(sys.argv[x])
    for y in getDivisors(number):
        divisorSum += y

    message = ''
    if(divisorSum < number):
        message = ' deficient'
    elif (divisorSum > number):
        message = ' abundant by ' + str(divisorSum - number)
    else:
        message = ' perfect'
    print(str(number) + message)