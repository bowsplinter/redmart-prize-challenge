# Redmart 1,000,000th Customer Prize

This is my attempt at a solution for the [Redmart coding challenge](http://geeks.redmart.com/2015/10/26/1000000th-customer-prize-another-programming-challenge/). This is a variant of the knapsack problem, with an extra parameter (weight).

## Problem
* Maximise value
* Minimise weight on draws
* Only 1 of each items
* Total Volume of items <= Volume of Tote
* Assume items can be packed if they can fit individually

## Implementation

I initially tried a top down dynamic programming approaching using memoization. While it worked for the toy data I used to test, it was unable to handle the memory requirements of the larger dataset due to the recursive function calls made to the stack.

Therefore, I switched to a bottom-up approach using tabulation. It is slightly more wasteful, as it fills up the table for all values of items and volumes. However, it works better with large datasets as it does not require memory in the stack to store the recursive function alls.

## Complexity

The algorithm has a running time complexity of `O(IV)` and space complexity of `O(IV)`, where `I` in the number of items that fit the tote and `V` is volume of the tote.