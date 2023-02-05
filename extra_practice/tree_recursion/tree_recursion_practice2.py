# # Summer 2019 Midterm: Q7(a)  Scrabbled Eggs

# def is_subseq(w1, w2):
#     """ Returns True if w1 is a subsequence of w2 and False otherwise.
#     >>> is_subseq("word", "word")
#     True
#     >>> is_subseq("compute", "computer")
#     True
#     >>> is_subseq("put", "computer")
#     True
#     >>> is_subseq("computer", "put")
#     False
#     >>> is_subseq("sin", "science")
#     True
#     >>> is_subseq("nice", "science")
#     False
#     >>> is_subseq("boot", "bottle")
#     False
#     """
#     if w1 == w2:
#         return True
#     elif len(w1) > len(w2):
#         return False
#     elif w1[0] not in w2:
#         return False
#     else:
#         if len(w1) > 1:
#             index = w2.find(w1[0]) + 1
#             return is_subseq(w1[1:],w2[index:])
#         else:
#             return True
           

        
        
# Summer 2019 Midterm: Q7(b)  Scrabbled Eggs
        
def is_subseq(w1, w2):
    """ Returns True if w1 is a subsequence of w2 and False otherwise.
    >>> is_subseq("word", "word")
    True
    >>> is_subseq("compute", "computer")
    True
    >>> is_subseq("put", "computer")
    True
    >>> is_subseq("computer", "put")
    False
    >>> is_subseq("sin", "science")
    True
    >>> is_subseq("nice", "science")
    False
    >>> is_subseq("boot", "bottle")
    False
    """
    if len(w1) == 0:
        return True
    elif len(w2) == 0:
        return False
    elif len(w1) > len(w2):
        return False
    elif w1 == w2 :
        return True
    else:
        with_elem = (w1[0] == w2[0]) and is_subseq(w1[1:], w2[1:])
        without_elem = is_subseq(w1, w2[1:])
        return with_elem or without_elem


# def is_subseq(w1, w2):
#     """ Returns True if w1 is a subsequence of w2 and False otherwise.
#     >>> is_subseq("word", "word")
#     True
#     >>> is_subseq("compute", "computer")
#     True
#     >>> is_subseq("put", "computer")
#     True
#     >>> is_subseq("computer", "put")
#     False
#     >>> is_subseq("sin", "science")
#     True
#     >>> is_subseq("nice", "science")
#     False
#     >>> is_subseq("boot", "bottle")
#     False
#     >>> is_subseq("a", "bottle")
#     False
#     """
#     i = j = 0
#     while i < len(w1) and j < len(w2):
#         if w1[i] == w2[j]:
#             i += 1
#         j += 1
#     return i == len(w1)



def scrabbler(chars, words, values):
    """ Given a list of words and point values for letters, returns a
    dictionary mapping each word that can be formed from letters in chars
    to their point value. You may not need all lines
    >>> words = ["easy", "as", "pie"]
    >>> values = {"e": 2, "a": 2, "s": 1, "p": 3, "i": 2, "y": 4}
    >>> scrabbler("heuaiosby", words, values)
    {'easy': 9, 'as': 3}
    >>> scrabbler("piayse", words, values)
    {'pie': 7, 'as': 3}
    """
    result = {}
    for word in words:
        if is_subseq(word, chars):
            value = 0
            for letter in word:
                value += values[letter]
            result[word] = value
    return result

# offical solution
def scrabbler(chars, words, values):
    """ Given a list of words and point values for letters, returns a
    dictionary mapping each word that can be formed from letters in chars
    to their point value. You may not need all lines
    >>> words = ["easy", "as", "pie"]
    >>> values = {"e": 2, "a": 2, "s": 1, "p": 3, "i": 2, "y": 4}
    >>> scrabbler("heuaiosby", words, values)
    {'easy': 9, 'as': 3}
    >>> scrabbler("piayse", words, values)
    {'as': 3, 'pie': 7}
    """
    result = {}
    for w in words:
        if is_subseq(w, chars):
            total = sum([values[c] for c in w])
            result[w] = total
    return result
    
    
    
# Summer 2019 Midterm: Q8

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
        a = [[label(t)] + helper(c, k-1, True) for c in branches(t)]
        if on_path:
            return max(a, key = sum)
        else:
            b = [helper(j, k, False) for j in branches(t)]
            return max( a + b, key = sum)
    return helper(t, k, False)


# Summer 2019 Final: 
# Q4(a)
def is_combo(n, k):
    """Is k a combo of n?
    >>> [k for k in range(1000) if is_combo(357, k)]
    [0, 7, 12, 15, 22, 35, 56, 105]
    """
    assert n >= 0 and k >= 0
    if k == 0:
        return True
    if n == 0 and k != 0:
        return False
    rest, last = n // 10, n % 10
    added = k >= last and is_combo(rest, k-last)
    multiplied = k % last == 0 and is_combo(rest, k / last)
    return added or multiplied
# Q4(b) 
def apply_tree(fn_tree, val_tree):
    """ Mutates val_tree by applying each function stored in fn_tree
    to the corresponding labels in val_tree
    >>> double = lambda x: x*2
    >>> square = lambda x: x**2
    >>> identity = lambda x: x
    >>> t3 = Tree(double)
    >>> t4 = Tree(6)
    >>> apply_tree(t3, t4)
    >>> t4
    Tree(12)
    >>> t1 = Tree(double, [Tree(square), Tree(identity)])
    >>> t2 = Tree(6, [Tree(2), Tree(10)])
    >>> apply_tree(t1, t2)
    >>> t2
    Tree(12, [Tree(4), Tree(10)])
 
    """
    val_tree.label = fn_tree.label(val_tree.label)

    for i in range(len(val_tree.branches)):
        apply_tree(fn_tree.branches[i], val_tree.branches[i])
# Q4(c)
def make_checker_tree(t, so_far=0):
    """ Returns a function tree that, when applied to another tree, will mutate its labels to be
    True if the label is a combination of the path in t from the root to its corresponding node.
    >>> t1 = Tree(5, [Tree(2), Tree(1)])
    >>> fn_tree = make_checker_tree(t1)
    >>> t2 = Tree(5, [Tree(10), Tree(7)])
    >>> apply_tree(fn_tree, t2) #5 is a combo of 5, 10 is a combo of 52, 7 isn't a combo of 51
    >>> t2
    Tree(True, [Tree(True), Tree(False)])
        """
    new_path = so_far*10 + t.label
    branches =  [make_checker_tree(b, new_path) for b in t.branches]
    fn = lambda x : is_combo(new_path, x)
    return Tree(fn, branches)

def make_tree(t, val):
    """ Returns a function tree that, when applied to another tree, will mutate its labels to be
    True if the label is a combination of the path in t from the root to its corresponding node.
    >>> t1 = Tree(5, [Tree(2), Tree(1)])
    >>> make_tree(t1, 2)
    Tree(7, [Tree(4), Tree(3)])
        """
    t.label = t.label + val
    branches =  [make_tree(b, val) for b in branches(t)]
    return Tree(t.label, branches)      
        




