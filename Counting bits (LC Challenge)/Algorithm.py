"""
Given an integer n, return an array ans of length n + 1
Such that for each i (0 <= i <= n)
ans[i] is the number of 1's in the binary representation of i.
# ---------------------------------------------------------------------------- #
0: [0]
1: [1]
2: [10]
3: [11]
4: [100]
5: [101]
6: [110]
7: [111]
8: [1000]
9: [1001]
10: [1010]
# ---------------------------------------------------------------------------- #
"""
#TODO: Start from 0
#TODO: ans[i] == to how many 1's in the binary representation
#TODO: 

n = 5
# --------------------------------- First Try -------------------------------- #

def algorithm():
    ans = [(bin(i)[2:].count("1")) for i in range(n + 1)] #NOTE: A bit hard to read; really sacrificed readibility for Big O here
    return ans

print(algorithm())


# O(n * b) Time complexity 84.98% | O(n) Space complexity Beats 65.29%