"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
# ---------------------------------------------------------------------------- #
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned.
"""

#NOTE: Need to return kth distinct string, if none, return empty string
# ---------------------------------------------------------------------------- #
#TODO: If array len is less than 2, return empty string
#TODO: As we move along the array, we check if an element is unique IF it hasn't been encountered before

#TODO: If it is unique, we add it to our unique array
#TODO: We drop element from unique_arr if we find an identical

#TODO: Once we get to the end of arr, we check if we have k elements in unique_arr -> if so, we return the kth element
# ---------------------------------------------------------------------------- #
#TODO: sec_pointer can't be -1, needs to be len of array so we can check when it matches first pointer to hault operation
#TODO: If in the iteration, we find a nonunique, we remove from unique_arr and add to nonunique_arr
#TODO: If i in nonunique_arr, we simply skip over
# ---------------------------------------------------------------------------- #
#TODO:
# --------------------------------- First Try -------------------------------- #

def algorithm():
    if len(arr) < 2:
        return ""
    # ---------------------------------------------------------------------------- #
    first_pointer = 0
    sec_pointer = len(arr)
    unique_arr = []
    nonunique_arr = []
    

    if arr[first_pointer or sec_pointer] in unique_arr and not unique_arr[first_pointer or sec_pointer]

    if arr[first_pointer or sec_pointer] in nonunique_arr or arr[first_pointer or sec_pointer] in unique_arr:
        unique_arr.remove(arr[first_pointer])
        nonunique_arr.append(arr[first_pointer])
        first_pointer += 1
    else:
        unique_arr.append(arr[first_pointer])
        first_pointer += 1



print(algorithm())


# O(n * b) Time complexity 84.98% | O(n) Space complexity Beats 65.29%