# def can_win(number):
#     """Returns True if the current player is guaranteed a win
#     starting from the given state. It is impossible to win a game
#     from an invalid game state.

#     >>> can_win (-1) # invalid game state
#     False
#     >>> can_win (3) # take all three !
#     True
#     >>> can_win (4)
#     False
#     """
 
#     if number <= 0:
#         return False
#     action = 1
#     while action <= 3:
#         if not can_win( number - action ):
#             return True
#         action += 1
#     return False
    
    
    
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# ans = factorial(2)
# print(ans)

# def foo(n):
#     i = 0
#     if n == 0:
#         return 0
#     result = foo(n - 2)
#     i += 1
#     return i + result

# result = foo(4)


def bar(f):
    def g(x):
        if x == 1:
            return f(x)
        else:
            return f(x) + g(x - 1)
    return g

f = 4
result2 = bar(lambda x: x + f)(2)
print(result2)


# recursion 
def change(n, coins):
    """Return whether a subset of coins adds up to n.
    >>> change(10, [2, 7, 1, 8, 2]) # e.g., 2 + 8
    True
    >>> change(20, [2, 7, 1, 8, 2]) # e.g., 2 + 7 + 1 + 8 + 2
    True
    >>> change(6, [2, 7, 1, 8, 2]) # Impossible; only two 2's in coins
    False
    """
    if n == 0:
        return True
    elif not(coins):
    #elif len(coins) == 0:
        return False
    coin = coins.pop() # remove the end of coins and name it "coin"
    # inclube or not include the coin
    return change(n - coin,coins) or change(n, coins)
    
# # Tree ADT

# def tree(label, branches=[]):
#     """Construct a tree with the given label value and a list of branches."""

#     for branch in branches:
#         assert is_tree(branch), 'branches must be trees'
#     return [label] + list(branches)


# def label(tree):
#     """Return the label value of a tree."""
#     if change_abstraction.changed:
#         return tree['label']
#     else:
#         return tree[0]


# def branches(tree):
#     """Return the list of branches of the given tree."""
#     if change_abstraction.changed:
#         return tree['branches']
#     else:
#         return tree[1:]


# def is_tree(tree):
#     """Returns True if the given tree is a tree, and False otherwise."""
#     if change_abstraction.changed:
#         if type(tree) != dict or len(tree) != 2:
#             return False
#         for branch in branches(tree):
#             if not is_tree(branch):
#                 return False
#         return True
#     else:
#         if type(tree) != list or len(tree) < 1:
#             return False
#         for branch in branches(tree):
#             if not is_tree(branch):
#                 return False
#         return True


# def is_leaf(tree):
#     """Returns True if the given tree's list of branches is empty, and False
#     otherwise.
#     """
#     return not branches(tree)


# def print_tree(t, indent=0):
#     """Print a representation of this tree in which each node is
#     indented by two spaces times its depth from the root.

#     >>> print_tree(tree(1))
#     1
#     >>> print_tree(tree(1, [tree(2)]))
#     1
#       2
#     >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
#     >>> print_tree(numbers)
#     1
#       2
#       3
#         4
#         5
#       6
#         7
#     """
#     print('  ' * indent + str(label(t)))
#     for b in branches(t):
#         print_tree(b, indent + 1)
    
def fruited_branch(t):
    """Return whether Tree t has exactly one child that is a fruit (a leaf with no siblings).
    >>> fruited_branch(Tree(4))
    False
    >>> fruited_branch(Tree(4, [Tree(5)]))
    True
    >>> fruited_branch(Tree(4, [Tree(5, [Tree(6)])]))
    False
    """
    return len(branches(t)) == 1 and is_leaf(branches(t)[0])
    
def sum_fruit_labels(t):
    """Return the sum of the labels of the fruits of Tree t.
    >>> apple = Tree(5, [Tree(6, [Tree(7)]), Tree(8), Tree(9, [Tree(10)])])
    >>> sum_fruit_labels(apple) # 7 + 10
    17
    >>> pineapple = Tree(3, [Tree(4), apple, apple, Tree(1, [Tree(2)])])
    >>> sum_fruit_labels(pineapple) # 7 + 10 + 7 + 10 + 2
    36
    >>> sum_fruit_labels(Tree(3, [Tree(4), Tree(5)])) # No fruits!
    0
    """
    if fruited_branch(t):
        return label(branches(t)[0])
    
    else:
        return sum([sum_fruit_labels(b) for b in branches(t)])
        

def pruned(t):
    """Return a Tree with only the nodes of t that are on a path to a fruit.
    >>> t = Tree(5, [Tree(6, [Tree(7)]), Tree(8), Tree(9, [Tree(10)])])
    >>> pruned(t)
    Tree(5, [Tree(6, [Tree(7)]), Tree(9, [Tree(10)])])
    >>> t # t is not modified by calling pruned(t)
    Tree(5, [Tree(6, [Tree(7)]), Tree(8), Tree(9, [Tree(10)])])
    >>> pruned(Tree(2, [Tree(3), Tree(4)])) is None # No fruit!
    True
    """
    if fruited_branch(t):
        return t
    cut = [pruned(b) for b in branches(t)]
    #print(cut)
   # Some items in cut might be None
    if any(cut):
        return Tree(label(t), [b for b in cut if b])

