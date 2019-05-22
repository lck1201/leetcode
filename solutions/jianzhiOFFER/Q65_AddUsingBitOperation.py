def add(num1, num2):
    '''
    num1/num2 must be positive
    '''
    if not num1 or not num2:
        return num1 or num2

    while num2!=0:
        sum = num1 ^ num2
        carry = (num1&num2)<<1

        num1 = sum
        num2 = carry

    return num1
