HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos // 10 > 0:
        if pos % 10 == 8:
            return 1 + num_eights(pos // 10)
        else:
            return num_eights(pos // 10)
    else:
        if pos == 8 :
            return 1
        else: 
            return 0


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    
    
    """
    "*** YOUR CODE HERE ***"
        # total = 0 
    # value = 0
    # i = 1
    # while i <= n:
    #     if total % 2 == 0:
    #         value += 1
    #     else:
    #         value -= 1
    #     if i % 8 == 0 or num_eights(i)>0:
    #         total += 1
    #     i += 1
    # return value

    # def helper(result, i, total):
    #     if i == n :
    #         return result
    #     if i % 8 == 0 or num_eights(i)>0:
    #         total += 1
    #     if total % 2 == 0:
    #         return helper(result, i + 1, total) + 1
    #     else:
    #         return helper(result, i + 1, total) - 1
        
        
    # return helper(1 , 1 , 0)
    def helper(result, i, step):
        if i == n:
            return result
        elif i % 8 == 0 or num_eights(i) > 0:
            return helper(result - step, i + 1, -step)
        else:
            return helper(result + step, i + 1, step)
    return helper(1, 1, 1)
            

def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20) # 
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    # def count_coin(change, unit):
    #     if change == 0:
    #         return 1
    #     elif change < 0:
    #         return 0
    #     elif unit == None:
    #         return 0
    #     else:
    #         with_m = count_coin(change - unit, unit)
    #         without_m = count_coin(change, next_larger_coin(unit))
    #         return with_m + without_m
    # return count_coin(change, 1)

    def count_coin(change, unit):
        if change == 0:
            return 1
        elif change < 0:
            return 0
        elif unit == None:
            return 0
        else:
            with_m = count_coin(change - unit, unit)
            without_m = count_coin(change, next_smaller_coin(unit))
            return with_m + without_m
    return count_coin(change, 25)

   


anonymous = False  # Change to True if you would like to remain anonymous on the final leaderboard.


def beaver(f):
    "*** YOUR CODE HERE ***"
    return (lambda g: g(g(g(g(g(g(g(f))))))))(lambda f: lambda: f() or f() or f())()


def beaver_syntax_check():
    """
    Checks that definition of beaver is only one line.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> source = inspect.getsource(beaver)
    >>> num_comments = source.count('\\n    #')
    >>> contains_default_line = '"*** YOUR CODE HERE ***"' in source
    >>> num_lines = source.count('\\n') - num_comments
    >>> (num_lines == 2) or (num_lines == 3 and contains_default_line)
    True
    """
    # You don't need to edit this function. It's just here to check your work.


def beaver_run_test():
    """
    Checks to make sure f gets called at least 1000 times.

    >>> counter = 0
    >>> def test():
    ...     global counter
    ...     counter += 1
    >>> beaver(test)
    >>> counter >= 1000
    True
    """
    # You don't need to edit this function. It's just here to check your work.


def collapse(n):
    """ For non-negative N, the result of removing all digits that are equal
    to the digit on their right, so that no adjacent digits are the same.
    >>> collapse(1234)
    1234
    >>> collapse(12234441)
    12341
    >>> collapse(0)
    0
    >>> collapse(3)
    3
    >>> collapse(11200000013333)
    12013
    """
    left, last = n // 10, n % 10
    if left == 0:
        return last
    elif left % 10 == last:
        return collapse(left)
    else:
        return collapse(left) * 10 + last


def find_pair(p):
    """Given a two-argument function P, return a function that takes a
    non-negative integer and returns True if and only if two adjacent digits
    in that integer satisfy P (that is, cause P to return a true value).
    >>> z = find_pair(lambda a, b: a == b) # Adjacent equal digits
    >>> z(1313)
    False
    >>> z(12334)
    True
    >>> z = find_pair(lambda a, b: a > b)
    >>> z(1234)
    False
    >>> z(123412)
    True
    >>> find_pair(lambda a, b: a <= b)(9753)
    False
    >>> find_pair(lambda a, b: a == 1)(1) # Only one digit; no pairs.
    False
    """
    def find(n):
        while n // 10 > 0:
            if p((n//10) % 10, n % 10):
                return True
            else:
                n = n // 10
        return False
    return find
            

def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234)
    11223344
    """
    last, rest = n % 10, n // 10
    if rest == 0:
        return last*10 + last 
    return last*10 + last + 100 * repeat_digits(rest) 

def pal(n):
    """Return a palindrome starting with n.
    >>> pal(12430)
    1243003421
    """
    m = n
    while m // 10 >= 0:
        n, m = 10 * n + m % 10, m // 10
    return 10*n + m % 10

def contains(a, b):
    """Return whether the digits of a are contained in the digits of b.
    >>> contains(357, 12345678)
    True
    >>> contains(753, 12345678)
    False
    >>> contains(357, 37)
    False
    """
    if a == b:
        return True
    if a > b:
        return False
    if a % 10 == b % 10:
        return contains( a // 10 , b // 10 )
    else:
        return contains( a , b // 10)

def biggest_palindrome(n):
    """Return the largest even-length palindrome in n.
    >>> biggest_palindrome(3425534)
    4554
    >>> biggest_palindrome(126130450234125)
    21300312
    """
    return big(n, 0)
def big(n, k):
    """A helper function for biggest_palindrome."""
    if n == 0:
        return 0
    choices = [big(n//10 , k), big(n // 10 , 10*k + n % 10 )]
    if contains(k, n):
        choices.append(pal(k))
    return max(choices)
    


def palinkdrome(n):
    """Return a function that returns a palindrome starting with the args of n repeated calls.
    >>> print(palinkdrome(3)(5)(6)(7))
    <5 6 7 7 6 5>
    >>> print(palinkdrome(1)(4))
    <4 4>
    """
    return outer(Link.empty, n)
    def outer(r, n):
        def inner(k):
            s = Link(k, r)
            if n == 1:
                t = s
                while s is not Link.empty:
                    t, s = Link(s.first,t) , s.rest
                return t
            else:
                return outer(s, n-1)
        return inner