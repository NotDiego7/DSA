"""
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

- Start at the 1st friend.
- Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
- The last friend you counted leaves the circle and loses the game.
- If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
- Else, the last friend in the circle wins the game.
- Return the winner of the game.

Constraints:

1 <= k <= n <= 500
"""
# ---------------------------------------------------------------------------- #
n = 6
k = 2

#TODO For each iteration we need to check Base-Case 1

def algorithm():
    if n == 1: # Base-case 1: only one person in the circle
        return n

    else:
        people_list = [i for i in range(1, n + 1)] # Creates the list of n people
        pointer = 0

        for i in range(k):
            if k > n:
                pass #TODO
        





print(algorithm())

# O(n * b) Time complexity 84.98% | O(n) Space complexity Beats 65.29%