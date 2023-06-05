# Object-oriented programmming

# 1 spring 2022 MT2 Q8 cs61a presents the game of hoop
class HoopPlayer:
    def __init__(self, strategy):
        """Initialize a player with STRATEGY, and a starting SCORE of 0. The
        STRATEGY should be a function that takes this player's score and a list
        of other players' scores.
        """
        self.strategy = strategy
        self.score = 0


class HoopDice:
    def __init__(self, values):
        """Initialize a dice with possible values VALUES, and a starting INDEX
        of 0. The INDEX indicates which value from VALUES to return when the
        dice is rolled next.
        """
        self.values = values
        self.index = 0
    def roll(self):
        """Roll this dice. Advance the index to the next step before
        returning.
        >>> five_six = HoopDice([5, 6])
        >>> five_six.roll()
        5
        >>> five_six.index
        1
        >>> five_six.roll()
        6
        >>> five_six.index
        0
        """
        value = self.values[self.index]
        self.index = (self.index + 1) / len(self.values)
        return value
    
class HoopGame:
    def __init__(self, players, dice, goal):
        """Initialize a game with a list of PLAYERS, which contains at least one
        HoopPlayer, a single HoopDice DICE, and a goal score of GOAL.
        """
        self.players = players
        self.dice = dice
        self.goal = goal
    def next_player(self):
        """Infinitely yields the next player in the game, in order."""
        >>> player_gen = game.next_player()
        >>> next(player_gen) is player1
        True
        >>> next(player_gen) is player3
        False
        >>> next(player_gen) is player3
        True
        >>> next(player_gen) is player1
        True
        >>> next(player_gen) is player2
        True
        >>> new_player_gen = game.next_player()
        >>> next(new_player_gen) is player1
        True
        >>> next(player_gen) is player3
        True

        yield from self.players
        yield from self.next_player()
    def get_scores(self):
        """Collects and returns a list of the current scores for all players
        in the same order as the SELF.PLAYERS list.
        """
        # Implementation omitted. Assume this method works correctly.


    def get_scores_except(self, player):
        """Collects and returns a list of the current scores for all players
        except PLAYER.
        >>> game.get_scores_except(player2)
        [0, 0]
        """
        return [pl.score for pl in self.players if pl is not player]
    
    def roll_dice(self, num_rolls):
        """Simulate rolling SELF.DICE exactly NUM_ROLLS > 0 times. Return sum of
        the outcomes unless any of the outcomes is 1. In that case, return 1.
        >>> game.roll_dice(4)
        20
        """
        outcomes = [self.dice.roll() for x in range(num_rolls)]
        ones = [outcome == 1 for outcome in outcomes]
        return 1 if any(ones) else sum(outcomes)
    
    def play(self):
        """Play the game while no player has reached or exceeded the goal score.
        After the game ends, return all players' scores.
        >>> game.play()
        [20, 10, 60]
        """
        player_gen = self.next_player()
        while max(self.get_scores()) < self.goal:
            player = next(player_gen)
            
            other_scores = self.get_scores_except(player)
            num_rolls = player.strategy(player.score, other_scores)
            
            outcome = self.roll_dice(num_rolls)
            player.score += outcome
            
            return self.get_scores()

class BrokenHoopDice(HoopDice):
    def __init__(self, values, when_broken):
        super().__init__(values)
        self.when_broken = when_broken
        self.is_broken = False
    def roll(self):
        """
        >>> broken = BrokenHoopDice([5, 6, 7], 11)
        >>> broken.roll()
        5
        >>> [broken.roll() for _ in range(6)]
        [11, 6, 11, 7, 11, 5]
        """
        if self.is_broken:
            self.is_broken = not self.is_broken
            return self.when_broken
        
        else:
            self.is_broken = not self.is_broken
            return super().roll()
# 2020 FALL mt2 q3 sparse lists

def most_common(s):
    """Return the most common element in non-empty list s. In case of a tie,
    return the most common element that appears first in s.
    >>> most_common([3, 1, 4, 1, 5, 9])
    1
    >>> most_common([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    5
    >>> most_common([2, 7, 1, 8, 2, 8, 1, 8, 2, 8])
    8
    >>> most_common([3, 5, 7, 7, 7, 5, 5])
    5
    >>> most_common([3, 7, 5, 5, 7, 7])
    7
    """

class SparseList:
    """Represent a non-empty list as a most common value and a dictionary from
    indices to values that contains only values that are not the most common.
    >>> pi = SparseList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    >>> pi.common
    5
    >>> pi.others
    {0: 3, 1: 1, 2: 4, 3: 1, 5: 9, 6: 2, 7: 6, 9: 3}
    >>> [pi.item(0), pi.item(1), pi.item(2), pi.item(3), pi.item(4)]
    [3, 1, 4, 1, 5]
    >>> pi.item(10)
    5
    >>> pi.item(11)
    'out of range'
    >>> pi.items()
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    """
    def __init__(self,s):
        assert s, 's cannot be empty'
        self.n = len(s)
        self.common = most_common(s)
        self.others = { i: s[i] for i in range(self.n) if s[i] != self.common}
    
    def item(self, i):
        """Return s[i] or 'out of range' if i is not smaller than the length of s."""
        assert i >= 0, 'index i must be non-negative'
        if i >= self.n:
            return 'out of range'
        elif i in self.others: # judge if i is the dictionary's key
            return self.others[i]
        else:
            return self.common
    
    def items(self):
        """Return a list with the same elements as s in the same order as s."""
        return [self.item(i) for i in range(self.n)]
    
# 2019 fall mt2 q7: version 2.0
class Version:
    """A version of a string after an edit.
    >>> s = Version('No power?', Delete(3, 6))
    >>> print(Version(s, Insert(3, 'class!')))
    No class!
    >>> t = Version('Beary', Insert(4, 'kele'))
    >>> print(t)
    Bearkeley
    >>> print(Version(t, Delete(2, 1)))
    Berkeley
    >>> print(Version(t, Delete(4, 5)))
    Bear
    """
    def __init__(self, previous, edit):
        self.previous, self.edit = previous, edit
    def __str__(self):
        return self.edit.apply(str(self.previous))
class Edit:
    def __init__(self, i, c):
        self.i, self.c = i, c
class Insert(Edit):
    def apply(self, t):
        "Return a new string by inserting string c into t starting at position i."
        return t[0:self.i] + self.c + t[self.i:]
class Delete(Edit):
    def apply(self, t):
        "Return a new string by deleting c characters from t starting at position i."
        return t[0:self.i] + t[self.i + self.c:]
    
# Linked Lists
# 2020 fall final q3: college party

class State:
    electors = {}
    def __init__(self, code, electors):
        self.code = code
        self.electors = electors
        State.electors[code] = electors
battleground = [State('AZ', 11), State('PA', 20), State('NV', 6),
    State('GA', 16), State('WI', 10), State('MI', 16)]
def print_all(s):
    for x in s:
        print(x)
def wins(states, k):
    """Yield each linked list of two-letter state codes that describes a win by at least k.
    >>> print_all(wins(battleground, 50))
    <AZ PA NV GA WI MI>
    <AZ PA NV GA MI>
    <AZ PA GA WI MI>
    <PA NV GA WI MI>
    >>> print_all(wins(battleground, 75))
    <AZ PA NV GA WI MI>
    """
    if k<= 0 and not states:
        yield Link.empty
    if states:
        first = states[0].electors
        for win in wins(states[1:], k - first):
            yield Link(states[0].code, win)
        yield from wins(states[1:], k + first)


def must_win(states, k):
    """List all states that must be won in every scenario that wins by k.
    >>> must_win(battleground, 50)
    ['PA', 'GA', 'MI']
    >>> must_win(battleground, 75)
    ['AZ', 'PA', 'NV', 'GA', 'WI', 'MI']
    """
    def contains(s, x):
        """Return whether x is a value in linked list s."""
        return x == s.first or contains(s.rest, x)
    # all() return true all True or return false to make sure that every scenario that wins by k
    return  [ s.code for s in states if all([contains(w, s.code) for w in wins(states, k)])]


def is_minimal(state_codes, k):
    """Return whether a non-empty list of state_codes describes a minimal win by
    at least k.
    >>> is_minimal(['AZ', 'NV', 'GA', 'WI'], 0) # Every state is necessary
    True
    >>> is_minimal(['AZ', 'GA', 'WI'], 0) # Not a win
    False
    >>> is_minimal(['AZ', 'NV', 'PA', 'WI'], 0) # NV is not necessary
    False
    >>> is_minimal(['AZ', 'PA', 'WI'], 0) # Every state is necessary
    True
    """
    assert state_codes, 'state_codes must not be empty'
    votes_in_favor = [State.electors[code] for code in state_codes]
    # (a)
    total_possible_votes = State.electors.values()
    
    def win_margin(n):
        "Margin of victory if n votes are in favor and the rest are against."
        return n - (total_possible_votes - n)
    if win_margin(sum(votes_in_favor)) < k:
        return False # Not a win
    in_favor_no_smallest = sum(votes_in_favor) - min(votes_in_favor) 
    return win_margin(in_favor_no_smallest) < k


# 2018 fall mt2 q6: Dr.Frankenlink


def replace(s, t, i, j):
    """Replace the slice of s from i to j with t.
    >>> s, t = Link(3, Link(4, Link(5, Link(6, Link(7))))), Link(0, Link(1, Link(2)))
    >>> replace(s, t, 2, 4)
    >>> print(s)
    <3, 4, 0, 1, 2, 7>
    >>> t.rest.first = 8
    >>> print(s)
    <3, 4, 0, 8, 2, 7>
    """
    assert s is not Link.empty and t is not Link.empty and i > 0 and i < j
    if i > 1:
        replace(s.rest, t, i-1, j-1)
    else:
        for k in range(j-i):
            s.rest = s.rest.resst
        end = t
        while end.rest is not Link.empty:
            end = end.rest
        s.rest, end.rest = t, s.rest


# spring 2017 mt1 q5 insert
if s is Link.empty:
    return Link.empty
else:
    Link(f(s.first) , map(f, s.rest))

if s is Link.empty:
    return s
filtered_rest = filter_link(f, s.rest)
if f(s.first):
    return Link(f(s.first), filtered_rest)
else:
    return filtered_rest

   
def add(s,v):
    '''
    add v to an ordered list s with no repeats, returning modified s
    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))
    '''

    assert s is not List.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    else:
        add(s.rest, v)
    return s
   
