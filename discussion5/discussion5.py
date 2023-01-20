# recursion
# su mt 22022 q4
#least resistance

def least_resistance(m, n, f):
    """
    >>> f = lambda x, y: x ** 2 + y ** 2
    >>> least_resistance(5, 5, f)
    195
    >>> g = lambda x, y: y
    >>> least_resistance(5, 5, g)
    15
    """
    if m==0 and n==0:

        return f(0,0)
    
    elif m<0 or n<0:
   
        return float('inf')
    else:
        r1 = least_resistance(m-1, n, f)
  
        r2 = least_resistance(m, n-1, f)
    
        return min(r1, r2) + f(m,n)

# su 2022 mt q6
# bold sum
# question a
def count_digits(n):
    """
    >>> count_digits(0) # 0 has no digits
    0
    >>> count_digits(618)
    3
    >>> count_digits(2022)
    4
    """
    if n == 0:
    
        return 0
    
    return 1 + count_digits(n//10)

# question b
def blob_sum(n, k):
    """
    >>> blob_sum(123, 15) # 12 + 3 = 15
    True
    >>> blob_sum(123, 6) # 1 + 2 + 3 = 6
    True
    >>> blob_sum(123, 33) # digits of `n` must be read left-to-right
    False
    >>> blob_sum(123, 24) # 1 + 23 = 24
    True
    >>> blob_sum(123, 12) # every digit of `n` must be used
    False
    >>> blob_sum(123, 35) # every digit of `n` can only be used once
    False
    """
    def helper(n, k, blob):
        if n == 0:
    
            return  k == blob
    
        if k <= 0
   
            return False
        rest, last = n//10, n%10
    
        new_blob = blob +(last *10 **count_digits(blob) )
    
        return helper(rest, k - new_blob, 0) or helper(rest, k, new_blob)
    
    return helper(n, k, 0)
    
# qq5
 
 def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    # if is_leaf(t):
    #     return label(t)
    # highest_sum = 0
    # for b in branches(t):
    #     highest_sum = max(max_path_sum(b), highest_sum)
    # return label(t) + highest_sum
    
    if is_leaf(t):
        return label(t)
    return label(t) + max([max_path_sum(b) for b in branches(t)],default = 0)
       
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [label(t)]
    for i in branches(t):
        path = find_path(i, x)
        if path:
            return [label(t)] + path
            
            
            
def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
    return label(t)+ sum([sum_tree(i) for i in branches(t)])
    # total = 0
    # for i in branches(t):
    #     total += sum_tree(i)
    # return label(t) + total
    
    
    
def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return True
    for i in branches(t):
        if sum_tree(i) != sum_tree(branches(t)[0]) or not balanced(i):
            return False
    return True
    



    
    
    

