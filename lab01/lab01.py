def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    mul = 1
    while k > 0 :
        mul *= n
        k -= 1
        n -= 1
    return mul


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    for i in str(y):
        sum += int(i)
    return sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    >>> double_eights(8888)
    True
    """
    "*** YOUR CODE HERE ***"
    # x = str(n)
    # if x.count('88') > 0:
    #     return True
    # else:
    #     return False
  

    # for z in range(len(x) - 1):
    #     if x[z] == '8' and x[z+1] == '8':
    #         return True
    #         break
    # return False

    # prev_eight = False
    # while n > 0:
    #     last_digit = n % 10
    #     if last_digit == 8 and prev_eight:
    #         return True
    #     elif last_digit == 8:
    #         prev_eight = True
    #     else:
    #         prev_eight = False
    #     n = n // 10
    # return False
    if type(n) != int or n < 0:
        return False
    return "88" in str(n)
            