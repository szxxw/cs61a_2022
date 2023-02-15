# Summer 2018 Final Q7a,b: Streams and Jennyrators


def generate_constant(x):
    """A generator function that repeats the same value X forever.
    >>> two = generate_constant(2)
    >>> next(two)
    2
    >>> next(two)
    2
    >>> sum([next(two) for _ in range(100)])
    200
    """
    while True:
        yield x
        

    
def black_hole(seq, trap):
    """A generator that yields items in SEQ until one of them matches TRAP, in
    which case that value should be repeatedly yielded forever.
    >>> trapped = black_hole([1, 2, 3], 2)
    >>> [next(trapped) for _ in range(6)]
    [1, 2, 2, 2, 2, 2]
    >>> list(black_hole(range(5), 7))
    [0, 1, 2, 3, 4]
    """
    for i in seq:
        if  i == trap:
          yield from generate_constant(i)
        else:
            yield i
            
            
# Spring 2019 Final Q1: Iterators are inevitable

def love():
    yield 1000
    yield from [2000, 3000]
x = love()
L = list(x)

def alternate(real, ity):
    i1, i2 = iter(real), iter(ity)
    try:
        while True:
            yield next(i1)
            yield next(i2)
    except StopIteration:
        yield 'inevitable'
thanos = ['power', 'space', 'reality']
tony = ['mind', 'soul', 'time']
i = iter(tony)
next(i)
tony.extend(list(i))
thanos = tony[2::-2]


# Spring 2021 MT2 Q8: The Tree of L-I-F-E
def word_finder(letter_tree, words_list):
    """ Generates each word that can be formed by following a path
    in TREE_OF_LETTERS from the root to a leaf,
    where WORDS_LIST is a list of allowed words (with no duplicates).
    # Case 1: 2 words found
    >>> words = ['SO', 'SAT', 'SAME', 'SAW', 'SOW']
    >>> t = Tree("S", [Tree("O"), Tree("A", [Tree("Q"), Tree("W")]), Tree("C", [Tree("H")])])
    >>> gen = word_finder(t, words)
    >>> next(gen)
    'SO'
    >>> next(gen)
    'SAW'
    >>> list(word_finder(t, words))
    ['SO', 'SAW']
    # Case 2: No words found
    >>> t = Tree("S", [Tree("I"), Tree("A", [Tree("Q"), Tree("E")]), Tree("C", [Tree("H")])])
    >>> list(word_finder(t, words))
    []
    # Case 3: Same word twice
    >>> t = Tree("S", [Tree("O"), Tree("O")] )
    >>> list(word_finder(t, words))
    ['SO', 'SO']
    # Case 4: Words that start the same
    >>> words = ['TAB', 'TAR', 'BAT', 'BAR', 'RAT']
    >>> t = Tree("T", [Tree("A", [Tree("R"), Tree("B")])])
    >>> list(word_finder(t, words))
    ['TAR', 'TAB']
    # Case 5: Single letter words
    >>> words = ['A', 'AN', 'AH']
    >>> t = Tree("A")
    >>> list(word_finder(t, words))
    ['A']
    # Case 6: Words end in leaf
    >>> words = ['A', 'AN', 'AH']
    >>> t = Tree("A", [Tree("H"), Tree("N")])
    >>> list(word_finder(t, words))
    ['AH', 'AN']
    # Case 7: Words start at root
    >>> words = ['GO', 'BEARS', 'GOB', 'EARS']
    >>> t = Tree("B", [Tree("E", [Tree("A", [Tree("R", [Tree("S")])])])])
    >>> list(word_finder(t, words))
    ['BEARS']
    # Case 8: This special test ensures that your solution does *not*
    # pre-compute all the words before yielding the first one.
    # If done correctly, your solution should error only when it
    # tries to find the second word in this tree.
    >>> words = ['SO', 'SAM', 'SAT', 'SAME', 'SAW', 'SOW']
    >>> t = Tree("S", [Tree("O"), Tree("A", [Tree("Q"), Tree(1)]), Tree("C", [Tree(1)])])
    >>> gen = word_finder(t, words)
    >>> next(gen)
    'SO'
    >>> try:
    ...     next(gen)
    ... except TypeError:
    ...     print("Got a TypeError!")
    ... else:
    ...     print("Expected a TypeError!")
    Got a TypeError!
    """
    def helper(t, so_far_word):
        so_far_word += label(t)
        #print(so_far_word)
        if is_leaf(t) and (so_far_word in words_list):
            yield so_far_word
        for b in branches(t):
            yield from helper(b, so_far_word)
    yield from helper(letter_tree, so_far_word = '')
    
    
def integers ( n ):
    while True :
        yield n
        n += 1
def drop (n , s ):
    for _ in range ( n ):
        next ( s )
    for elem in s :
        yield elem
def powers_of_two ( ints = integers(1)):
    """
    >>> p = powers_of_two ()
    >>> [ next (p) for _ in range (10)]
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    """
    curr = next(ints)
    #print(curr)
    yield curr
    yield from powers_of_two (drop(curr-1,  ints))
    
    
# Spring 2018 Final Q4a: Apply Yourself

def times(f, x):
    """Return a function g(y) that returns the number of f's in f(f(...(f(x)))) == y.
    >>> times(lambda a: a + 2, 0)(10) # 5 times: 0 + 2 + 2 + 2 + 2 + 2 == 10
    5
    >>> times(lambda a: a * a, 2)(256) # 3 times: square(square(square(2))) == 256
    3
    """
    def repeat(z):
        """Yield an infinite sequence of z, f(z), f(f(z)), f(f(f(z))), f(f(f(f(z)))), ...."""
        yield z
        yield from repeat(f(z))
    def g(y):
        n = 0
        for w in repeat(x):
            if w == y:
                return n
            n += 1
    return g

