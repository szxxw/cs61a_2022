
#61a-su21-midterm Q4 Maximum Exponen-tree-ation
def exp_tree(values):
    """
    Returns the exponential tree that can be made from VALUES
    with the greatest possible root label
    >>> print_tree(exp_tree([5]))
    5
    >>> print_tree(exp_tree([3, 2]))
    9
      3
      2
    >>> print_tree(exp_tree([2, 3, 2]))
    512
      2
      9
        3
        2     
    >>> lst = [3, 1, 2, 3]
    >>> print_tree(exp_tree(lst))
    6561
      3
        3
        1
      8
        2
        3
    """
    if len(values) == 1:
    # (a)
        return tree(values[0])
    # (b)
    else:
        def tree_at_split(i):
            base = exp_tree(values[0:i])
            # (c)
            exponent = exp_tree(values[i:])
            # (d)
            return tree(label(base) ** label(exponent), [base, exponent])
            # (e)
        
        trees = [tree_at_split(i) for i in range(1, len(values))]
        return max(trees, key= lambda t: label(t))
        
# Summer 2019 MT Q8: Leaf It To Me

def max_path(t, k):
    """ Return a list of the labels on any path in tree t of length at most k with the greatest sum
    >>> t1 = tree(6, [tree(3, [tree(8)]), tree(1, [tree(9), tree(3)])])
    >>> max_path(t1, 3)
    [6, 3, 8]
    >>> max_path(t1, 2)
    [3, 8]
    >>> t2 = tree(5, [t1, tree(7)])
    >>> max_path(t2, 1)
    [9]
    >>> max_path(t2, 2)
    [5, 7]
    >>> max_path(t2, 3)
    [6, 3, 8]
    """
    def helper(t, k, on_path):
        if k == 0:
            return []
        elif is_leaf(t):
            return [label(t)]
        a = [[label(t)] + helper(b, k-1 , True) for b in branches(t)]
        if on_path:
            return max(a, key = sum)
        else:
            b = [helper(b,k,False) for b in branches(t)]
            return max(a + b, key = sum)
    return helper(t, k, False)
    
# Summer 2017 MT Q9: Temmie Flakes   
def count_ways(t, total):
    """Return the number of ways that any sequence of consecutive nodes in a root-to-leaf path
    can sum to total.
    >>> t1 = tree(5, [tree(1, [tree(2, [tree(1)]),
    ... tree(1, [tree(4, [tree(2, [tree(2)])])])]),
    ... tree(3, [tree(2, [tree(2),
    ... tree(3)])]),
    ... tree(3, [tree(1, [tree(3)])])])
    >>> count_ways(t1, 7)
    4
    >>> count_ways(t1, 4)
    6
    >>> t2 = tree(2, [tree(-10, [tree(12)]),
    ... tree(1, [tree(1),
    ... tree(-1, [tree(2)])])])
    >>> count_ways(t2, 2)
    6
    >>> count_ways(t2, 4)
    3
    """
    def paths(t, can_skip, total):
        ways = 0
        if total == label(t):
            ways += 1
        ways += sum([paths(b, False, total - label(t)) for b in branches(t)])
        if can_skip:
            ways += sum([paths(b, True, total) for b in branches(t)])
        return ways
    return paths(t, True, total)
