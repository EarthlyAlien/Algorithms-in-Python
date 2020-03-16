# Author: Chaitanya Vankadaru
# Selection Sort in Python

# Explanation::
# • Step-1: Find the smallest element in the array and swap it with the first element.
# • Step-2: Find the second smallest element and swap with with the second element in the array.
# • Step-3: Find the third smallest element and swap wit with the third element in the array.
# • Step-4: Repeat the process of finding the next smallest element and swapping it into the correct position until the entire array is sorted. 

# Time Complexity::
# Best(Ω), Average(Θ) and Worst(O) case time complexity: N^2 which is independent of distribution of data.

# Space Complexity::
# Worst Case => O(1)

# Properties::
# Θ(n2) comparisons
# Θ(n) swaps

# Pros::
# Minimizes the number of swaps comparitively to other sorting algorithms. 

# Cons::
# Unstable
# Not Adaptive of Data

# Best Use Cases::
# Can be used in applications where the cost of swapping items is high.

# Helpful Link: https://www.toptal.com/developers/sorting-algorithms/selection-sort
# Example Visualization Link: https://miro.medium.com/max/270/1*2a0cRzZpoN7e7vS0sE8_rw.gif

# Reference Link for Algos: https://www.bigocheatsheet.com


# Code::

def seletion_sort(arr):
         if not arr:
         return arr
    for i in range(len(arr)):
         min_i = i
         for j in range(i + 1, len(arr)):
              if arr[j] < arr[min_i]:
                  min_i = j
         arr[i], arr[min_i] = arr[min_i], arr[i]
