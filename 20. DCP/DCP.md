Given K sorted lists. Return a new sorted merged list from K sorted lists, each with size N

Input: `[[10, 15, 30], [12, 15, 20], [17, 20, 32]]`,
Output: `[10, 12, 15, 15, 17, 20, 20, 30, 32]`

[Merge lists](dcp_000.py)

----

1.  ### Amazon

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.  

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

Example, given the string `the quick brown fox jumps over the lazy dog` and `k = 10`, you should return: `["the quick", "brown fox", "jumps over", "the lazy", "dog"]`. No string in the list has a length of more than 10.

[Sentence Break](dcp_001.py)

----

2. ### Uber

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example,

input: `[1, 2, 3, 4, 5]`, output: `[120, 60, 40, 30, 24]`.
input: `[3, 2, 1]`, output: `[2, 3, 6]`

[Product except self](dcp_002.py)

----

4. ### Stripe

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

You can modify the input array in-place.

[First missing positive number](dcp_004.py)

----

5. ### Mozilla

A bridge in a connected (undirected) graph is an edge that, if removed, causes the graph to become disconnected. Find all the bridges in a graph.

[Bridges](dcp_005.py)

----

6. ### Google

Implement an `LFU` (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

`set(key, value)`: sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.

`get(key)`: gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.

Similar [leetcode, Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/)

[LFU](dcp_006.py)

----

7. ### Facebook
Given the mapping `a = 1, b = 2, … z = 26`, and an encoded message, count the number of ways it can be decoded.  
For example, the message ‘111’ would give 3, since it could be decoded as `‘aaa’, ‘ka’, and ‘ak’`.

You can assume that the messages are decodable. For example, ‘001’ is not allowed.

[Decode Ways](dcp_007.py)

----

8. ### Google
A `unival tree` (which stands for “universal value”) is a tree where all nodes under it have the same value.  
Given the root to a binary tree, count the number of unival subtrees.  
For example, the following tree has `5` unival subtrees:  
```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```
[Unival Trees](dcp_008.py)


----

9. ### Airbnb
Given a list of integers, write a function that returns the largest sum of *non-adjacent numbers*. Numbers can be 0 or negative.  
For example, `[2, 4, 6, 8]` should return `12`, since we pick `4 and 8`. `[5, 1, 1, 5]` should return `10`, since we `pick 5 and 5`.

[Non-adjacent Sum](dcp_009.py)

----

11. ### Twitter

Implement an `autocomplete` system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string `de` and the set of strings `[dog, deer, deal]`, return `[deer, deal]`.

[Autocomplete system](dcp_011.py)

----

12. ### Amazon
There exists a staircase with `N` steps, and you can climb up either `1 or 2 steps` at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is `4`, then there are `5` unique ways:
```
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
```
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if `X = {1, 3, 5}`, you could climb `1, 3, or 5` steps at a time.

[Staircase](dcp_012.py)

----

13. ### Amazon
Given an integer `k` and a string `s`, find the length of the longest substring that contains at most k distinct characters.

For example, given `s = “abcba”` and `k = 2`, the longest substring with k distinct characters is `“bcb”`.

[Longest Substring k characters](dcp_013.py)

----

14. ### Google

The area of a circle is defined as `r^2`. **Estimate** `\pi` to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.

[Pi](dcp_014.py)

----

15. ### Facebook

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

[Reservoir Sampling](dcp_015.py)

----

16. ### Twitter

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

`record(order_id)`: adds the order_id to the log.

`get_last(i)`: gets the ith last element from the log. 

i is guaranteed to be smaller than or equal to N. You should be as efficient with time and space as possible.

[Order Log](dcp_016.py)

----

17. ### Google

Suppose we represent our file system by a string in the following manner:

The string `“dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext”` represents:
```
dir
    subdir1
    subdir2
        file.ext
```

The directory `dir` contains an empty sub-directory `subdir1` and a sub-directory `subdir2` containing a file `file.ext`.

The string `“dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext”` represents:
```
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```

The directory `dir` contains two sub-directories `subdir1` and `subdir2`. `subdir1` contains a file `file1.ext` and an *empty* second-level sub-directory `subsubdir1`. `subdir2` contains a second-level sub-directory `subsubdir2` containing a file `file2.ext`.

We are interested in **finding the longest (number of characters) absolute path** to a file within our file system. 
For example, in the second example above, the longest absolute path is `“dir/subdir2/subsubdir2/file2.ext”`, and its length is `32` (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

[Longest Path of File](dcp_017.py)

----

18. ### Google

Given an array of integers and a number k, where `1 <= k <= length of the array`, compute the **maximum** values of each subarray of length k.

For example, given array = `[10, 5, 2, 7, 8, 7]` and `k = 3`, we should get: `[10, 7, 8, 8]`, since:
```
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
```
Do this in `O(n) time and O(k) space`. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

[Window Max Value](dcp_018.py)

----

19. ### Facebook

A builder is looking to build a row of `N` houses that can be of `K` different colors. 
He has a goal of *minimizing cost* while ensuring that *no two neighboring houses are of the same color*.

Given an `N by K matrix` where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

[Paint Houses](dcp_019.py)

----

20. ### Google

Given two singly linked lists that intersect at some point, find the *intersecting node*. The lists are non-cyclical.

For example, given `A = 3 -> 7 -> 8 -> 10` and `B = 99 -> 1 -> 8 -> 10`, return the node with value `8`.

In this example, assume nodes with the same value are the exact same node objects.
Do this in `O(M + N)` time (where M and N are the lengths of the lists) and constant space.

[Intersecting Linked List](dcp_020.py)

----

21. ### Snapchat

Given an array of time `intervals (start, end)` for classroom lectures (possibly overlapping), find the *minimum number of rooms required*.

For example, given `[(30, 75), (0, 50), (60, 150)]`, you should return `2`.

[Min Rooms](dcp_021.py)

----

22. ### Microsoft

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words `'quick', 'brown', 'the', 'fox'`, and the string `"thequickbrownfox"`, you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words `'bed', 'bath', 'bedbath', 'and', 'beyond'`, and the string `"bedbathandbeyond"`, return either `['bed', 'bath', 'and', 'beyond']` or `['bedbath', 'and', 'beyond']`.

[Sentence break](dcp_022.py)

----

23. ### Google

You are given an `M by N matrix` consisting of `booleans` that represents a board. Each `True boolean` represents a **wall**. Each `False boolean` represents a **tile** you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. 

You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:
```
[[f, f, f, f],
 [t, t, f, t],
 [f, f, f, f],
 [f, f, f, f]]
```
and `start = (3, 0)` (bottom left) and `end = (0, 0)` (top left), the minimum number of steps required to reach the end is `7`, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

[Shorted Path in Maze](dcp_023.py)

----

24. ### Google

Implement locking in a binary tree. A binary tree node can be `locked` or `unlocked` only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

`is_locked`, which returns whether the node is locked lock, which attempts to lock the node.
If it cannot be locked, then it should return false. Otherwise, it should lock it and return true. unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true. 

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in `O(h)`, where `h` is the height of the tree.

[Locking Binary Tree](dcp_024.py)

----

25. ### Facebook

Implement regular expression matching with the following special characters:
`. (period)` which matches any single character
`* (asterisk)` which matches zero or more of the preceding element That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression `“ra.”` and the string `“ray”`, your function should return true. The same regular expression on the string `“raymond”` should return false.

Given the regular expression `".*at"` and the string `“chat”`, your function should return true. The same regular expression on the string `“chats”` should return false.

[Regular Expression](dcp_025.py)

----

26. ### Google

Given a singly linked list and an integer k, *remove the kth last element from the list*. 

k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

[Remove kth Element from last](dcp_026.py)

----

27. ### Facebook

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string `“([])”`, you should return `true`.

Given the string `“([)]”` or `“((()”`, you should return `false`.

[Valid Brackets](dcp_027.py)

----

28. ### Palantir

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. 
- There should be at least one space between each word. 
- Pad extra spaces when necessary so that each line has exactly length k.
- Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
- If you can only fit one word on a line, then you should pad the right-hand side with spaces.
- Each word is guaranteed not to be longer than k.

For example, given the list of words `[“the”, “quick”, “brown”, “fox”, “jumps”, “over”, “the”, “lazy”, “dog”]` and `k = 16`, you should return the following:

[“the quick brown”, # 1 extra space on the left “fox jumps over”, # 2 extra spaces distributed evenly “the lazy dog”] # 4 extra spaces distributed evenly

[Text Justification](dcp_028.py)

----

29. ### Amazon

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. 

For example, the string `“AAAABBBCCDAA”` would be encoded as `“4A3B2C1D2A”`.

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

[String encoding](dcp_029.py)

----

30. ### Facebook

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in `O(N)` time and `O(1)` space.

For example, given the input `[2, 1, 2]`, we can hold 1 unit of water in the middle.

Given the input `[3, 0, 1, 3, 0, 5]`, we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap `8 units` of water.

[Trapped Water](dcp_030.py)

----

31. ### Google

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other.

For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

[Edit Distance](dcp_031.py)

----

32. ### Jane Street

Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.

[Bellman Ford](dcp_032.py)

----

33. ### Microsoft

Compute the *running median* of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence `[2, 1, 5, 7, 2, 0, 5]`, your algorithm should print out:
```
2
1.5
2
3.5
2
2
2
```

[Running Median](dcp_033.py)

----

34. ### Quora

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word.

If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string “race”, you should return “ecarace”, since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from “race” by adding three letters, but “ecarace” comes first alphabetically.

As another example, given the string “google”, you should return “elgoogle”.

[Minimum Insertion](dcp_034_a.py)

[Nearest Palindrome](dcp_034_b.py)

----

35. ### Google

Given an array of strictly the characters ‘R’, ‘G’, and ‘B’, segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array `[‘G’, ‘B’, ‘R’, ‘R’, ‘B’, ‘R’, ‘G’]`, it should become `[‘R’, ‘R’, ‘R’, ‘G’, ‘G’, ‘B’, ‘B’]`.

[Dutch Flag](dcp_035.py)

----

36. ### Dropbox

Given the root to a binary search tree, find the second largest node in the tree.

[Second Largest Node in BST](dcp_036.py)

----

37. ### Google

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set `{1, 2, 3}`, it should return `{ {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3} }`.

You may also use a list or array to represent a set.

[Power Set](dcp_037.py)

----

38. ### Microsoft

You have an N by N board. Write a function that, given N, returns *the **number** of possible arrangements* of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

[N queens count](dcp_038.py)

----

39. ### Dropbox

Conway’s Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

- Any live cell with less than two live neighbours dies.

- Any live cell with two or three live neighbours remains living.

- Any live cell with more than three live neighbours dies.

- Any dead cell with exactly three live neighbours becomes a live cell. 

A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway’s Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it’s an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

[Game of Life](dcp_039.py)

----

40. ### Google

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example,

- `[6, 1, 3, 3, 3, 6, 6]`, return `1`
- `[13, 19, 13, 13]`, return `19`

Do this in `O(N)` time and `O(1)` space.

[Single Number](dcp_040.py)

----

41. ### Facebook

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person’s itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights `[(‘SFO’, ‘HKO’), (‘YYZ’, ‘SFO’), (‘YUL’, ‘YYZ’), (‘HKO’, ‘ORD’)]` and starting airport `‘YUL’`, you should return the list `[‘YUL’, ‘YYZ’, ‘SFO’, ‘HKO’, ‘ORD’]`.

Given the list of flights `[(‘SFO’, ‘COM’), (‘COM’, ‘YYZ’)]` and starting airport `‘COM’`, you should return `null`.

Given the list of flights `[(‘A’, ‘B’), (‘A’, ‘C’), (‘B’, ‘C’), (‘C’, ‘A’)]` and starting airport `‘A’`, you should return the list `[‘A’, ‘B’, ‘C’, ‘A’, ‘C’]` even though `[‘A’, ‘C’, ‘A’, ‘B’, ‘C’]` is also a valid itinerary. However, the first one is lexicographically smaller.

[Flight Itinerary](dcp_041.py)

----

42. ### Google

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.

If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given `S = [12, 1, 61, 5, 9, 2]` and `k = 24`, return `[12, 9, 2, 1]` since it sums up to 24.

[Subset Sum](dcp_042.py)

----

43. ### Amazon

Implement a stack that has the following methods:

`push(val)`: pushes an element onto the stack  
`pop()`: pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.  
`max()`: which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

[Max Stack 1](dcp_043_a.py)

[Max Stack 2](dcp_043_b.py)

----

44. ### Google

We can determine how `out of order` an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if `A[i] > A[j]` but `i < j`. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array `[2, 4, 1, 3, 5]` has three inversions: `(2, 1), (4, 1), and (4, 3)`. The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

[Inversions](dcp_044.py)

----

45. ### Two Sigma

Using a function `rand5()` that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function `rand7()` that returns an integer from 1 to 7 (inclusive).

[Uniform Probability](dcp_045.py)

----

46. ### Amazon

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of `aabcdcb` is `bcdcb`.  
The longest palindromic substring of `bananas` is `anana`.

[Palindromic Substring](dcp_046.py)

----

47. ### Facebook

Given a array of numbers representing the stock prices of a company in  order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given `[9, 11, 8, 5, 7, 10]`, you should return `5`, since you could **buy** the stock at `5` dollars and **sell** it at `10` dollars.

[Buy Sell Stock](dcp_047.py)

----

48. ### Google

Given **pre-order** and **in-order** traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following

Preorder traversal: `[a, b, d, e, c, f, g]`

Inorder traversal: `[d, b, e, a, f, c, g]`

You should return the following tree:
```
    a
   / \
  b   c
 / \ / \
d  e f  g
```

[Reconstruct Tree from Preorder and Inorder](dcp_048.py)

----

49. ### Amazon

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array `[34, -50, 42, 14, -5, 86]`, the maximum sum would be `137`, since we would take elements `42, 14, -5, and 86`.

Given the array `[-5, -1, -8, -9]`, the maximum sum would be `0`, since we would not take any elements.

Do this in `O(N)` time.

[Max Subarray](dcp_049.py)

----

50. ### Microsoft

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of `‘+’, ‘−’, ‘∗’, or ‘/’`.

Given the root to such a tree, write a function to evaluate it.
```
    *
   / \
  +    +
 / \  / \
3  2  4  5
```

You should return `45`, as it is `(3 + 2) * (4 + 5)`.

[Evaluate Expression](dcp_050.py)

----

51. ### Facebook

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.

[Fisher-Yates Algorithm](dcp_051.py)

----

52. ### Google

Implement an `LRU (Least Recently Used)` cache. It should be able to be initialized with a cache size n, and contain the following methods:

`set(key, value)`: sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.

`get(key)`: gets the value at key. If no such key exists, return null.

Each operation should run in `O(1)` time.

[LRU Cache](dcp_052.py)

----

53. ### Apple

Implement a queue using two stacks. Recall that a queue is a `FIFO` (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

[Queue using Stacks](dcp_053.py)

----

54. ### Dropbox

Sudoku is a puzzle where you’re given a partially-filled 9 by 9 grid with digits.

The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.

[Sudoku](dcp_054_a.py)

[Sudoku with caching](dcp_054_b.py)

----

55. ### Microsoft

Implement a URL shortener with the following methods:

- `shorten(url)`, which shortens the url into a six-character alphanumeric string, such as zLg6wl.

- `restore(short)`, which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?

[URL Shortner](dcp_055.py)

----

56. ### Google

Given an undirected graph represented as an adjacency matrix and an integer k, determine whether each node in the graph can be colored such that no two adjacent nodes share the same color using at most k colors.

[Graph Coloring](dcp_056.py)

----

57. ### Amazon

Same as 1

----

58. ### Amazon

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn’t exist in the array, return null.

For example, given the array `[13, 18, 25, 2, 8, 10]` and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.

[Search in rotated array](dcp_058.py)

----

59. ### Google

Implement a file syncing algorithm for two computers over a low-bandwidth network.

What if we know the files in the two computers are mostly the same?

[Merkel Tree](dcp_059.py)

----

60. ### Facebook

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can’t split it up into two subsets that add up to the same sum.

[Equal Partition](dcp_060.py)

----

61. ### Google

Implement integer exponentiation. That is, implement the `pow(x, y)` function, where `x` and `y` are integers and returns `x^y`.

Do this faster than the naive method of repeated multiplication.

For example, `pow(2, 10)` should return `1024`.

[Power](dcp_061.py)

----

62. ### Facebook

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

- Right, then down

- Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

[Number of Paths](dcp_062.py)

----

63. ### Microsoft

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:
```
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
```
and the target word `‘FOAM’`, you should return `true`, since it’s the leftmost column.

Similarly, given the target word `‘MASS’`, you should return true, since it’s the last row.

[Word search](dcp_063.py)

----

64. ### Google

A knight’s tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight’s tours on an N by N chessboard.

[Knight Tour](dcp_064.py)

----

65. ### Amazon

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:
```
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
```
You should print out the following:

`1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12`

[Spiral Matrix](dcp_065.py)

----

66. ### Square
    
Assume you have access to a function `toss_biased()` which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.

[Biased Coin](dcp_066.py)

----

67. ### Google

Implement an LFU (Least Frequently Used) cache.

Same as Que 006

[LFU Cache](dcp_067.py)

----

68. ### Google

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn’t matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:
```
(0, 0)
(1, 2)
(2, 2)
(4, 0)
```

The board would look like this:
```
[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
```
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.

[Bishop Attack](dcp_068.py)

----

69. ### Facebook

Given a list of integers, return the largest product that can be made by multiplying any three integers.  
For example, if the list is `[-10, -10, 5, 2]`, we should return `500`, since that's `-10 * -10 * 5`.  
You can assume the list has at least three integers.  

[Max Product](dcp_069.py)

----

70. ### Microsoft

A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

[Nth Perfect Number](dcp_070.py)

----

71. ### Two Sigma

(repeated question - Problem 45)

----

72. ### Google

In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through `ABACA`, the value of the path is 3, since there are 3 occurrences of `A` on the path.  

Given a graph with `n` nodes and `m` directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.  

The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list `(i, j)` means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.  

For example, the following input graph:  
```
ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
```  
Would have maximum value 3 using the path of vertices `[0, 2, 3, 4], (A, A, C, A)`.

The following input graph:  
```
A
[(0, 0)]
```
Should return null, since we have an infinite loop.

[Longest Path](dcp_072.py)

----

73. ### Google

Given the head of a singly linked list, reverse it in-place.

[Reverse Linked List](dcp_073.py)

----

74. ### Apple

Suppose you have a multiplication table that is N by N.
That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given `N = 6 and X = 12`, you should return `4`, since the multiplication table looks like this:

```
1	2	3	4	5	6
2	4	6	8	10	12
3	6	9	12	15	18
4	8	12	16	20	24
5	10	15	20	25	30
6	12	18	24	30	36
```

And there are **4** 12’s in the table.

[Multiple Count](dcp_074.py)

----

75. ### Microsoft

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example,

given the array `[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]`,

longest increasing subsequence has length `6`: it is `0, 2, 6, 9, 11, 15`.

----

76. ### Google

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:
```
cba
daf
ghi
```

This is not ordered because of the a in the center. We can remove the second column to make it ordered:
```
ca
df
gi
```

So your function should return `1`, since we only needed to remove 1 column.

As another example, given the following table:

```
abcdef
```

Your function should return `0`, since the rows are already ordered (there’s only one row).

As another example, given the following table:
```
zyx
wvu
tsr
```

Your function should return `3`, since we would need to remove all the columns to order it.

[Delete Columns to Make Sorted](dcp_076.py)

----

77. ### Snapchat

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.

For example, given `[(1, 3), (5, 8), (4, 10), (20, 25)]`, you should return `[(1, 3), (4, 10), (20, 25)]`.

[Merge Intervals](dcp_077.py)

----

78. ### Google

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

[Merge Linked Lists](dcp_078.py)

----

79. ### Facebook

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array `[10, 5, 7]`, you should return `true`, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array `[10, 5, 1]`, you should return `false`, since we can’t modify any one element to get a non-decreasing array.

[Non-decreasing array](dcp_079.py)

----

80. ### Google

Given the root of a binary tree, return a deepest node. 

For example, in the following tree, return d.

```
    a
   / \
  b   c
 /
d
```

[Deepest Node](dcp_080.py)

----

81. ### Yelp

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent.

You can assume each valid number in the mapping is a single digit.

For example if `{'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], }` then `"23"` should return `['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']`.

[Letter Combinations](dcp_081.py)

----

82. ### Microsoft

Using a `read7()` method that returns `7` characters from a file, implement `readN(n)` which reads `n` characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

[Read File](dcp_082.py)

----

83. ### Google

Invert a binary tree.

For example, given the following tree:
```
    a
   / \
  b   c
 / \  /
d   e f
```

should become:
```
  a
 / \
 c  b
 \  / \
  f e  d
```

[Invert Binary Tree](dcp_083.py)

----

84. ### Amazon

Given a matrix of 1s and 0s, return the number of “islands” in the matrix.

A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring and their perimeter is surrounded by water.

For example, this matrix has `4` islands.
```
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
```

[Number of Islands](dcp_084.py)

----

### 85. Facebook

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. 

You can assume b can only be 1 or 0.

[A or B](dcp_085)

----

86. ### Google

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string `()())()`, you should return `1`. 

Given the string `)(`, you should return `2`, since we must remove all of them.

[Minimum Remove to Make Valid Parentheses](dcp_086.py)

----

88. ### ContextLogic

Implement division of two positive integers without using the division, multiplication, or modulus operators.

Return the quotient as an integer, ignoring the remainder.

[Division](dcp_088.py)

----

89. ### LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.

[Valid Binary Search Tree](dcp_089.py)

----

90. ### Google

Given an `integer n` and a `list of integers l`, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

[Random Number](dcp_090.py)

----

91. ### Dropbox

What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

```
functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
```

[Code Fix](dcp_091.py)

----

92. ### Airbnb

We’re given a hashmap with a key `courseId` and value a list of courseIds, which represents that the prerequsite of courseId is courseIds.

Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given `{'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}`, should return `['CSC100', 'CSC200', 'CSCS300']`.

[Topological Ordering](dcp_092.py)

----

93. ### Apple

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.

[Largest subtree BST](dcp_093.py)

----

94. ### Google

Given a binary tree of integers, find the maximum path sum between two nodes.

The path must go through at least one node, and does not need to go through the root.

[Max Path Sum](dcp_094.py)

----

95. ### Palantir

Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list `[1,2,3]` should return `[1,3,2]`. The list `[1,3,2]` should return `[2,1,3]`. The list `[3,2,1]` should return `[1,2,3]`.

Can you perform the operation without allocating extra memory (disregarding the input memory)?

[Next Permutation](dcp_095.py)

----

96. ### Microsoft

Given a number in the form of a list of digits, return all possible permutations.

For example, given `[1,2,3]`, return `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`.

[Permutations](dcp_096.py)

----

97. ### Stripe

Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

`set(key, value, time)`: sets key to value for t = time.
`get(key, time)`: gets the key at t = time.

The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

Consider the following examples:
```
d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 2)  # set key 1 to value 2 at time 2
d.get(1, 1)     # get key 1 at time 1 should be 1
d.get(1, 3)     # get key 1 at time 3 should be 2
d.set(1, 1, 5)  # set key 1 to value 1 at time 5
d.get(1, 0)     # get key 1 at time 0 should be 1
d.get(1, 10)    # get key 1 at time 10 should be 1
d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 0)  # set key 1 to value 2 at time 0
d.get(1, 0)     # get key 1 at time 0 should be 2
```

[Time Map](dcp_097.py)

----

98. ### Coursera

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those `horizontally` or `vertically` neighboring. The same letter cell may not be used more than once.

For example, given the following board:
```
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```
`exists(board, "ABCCED")` returns `true`, `exists(board, "SEE")` returns `true`, `exists(board, "ABCB")` returns `false`.

[Word Search](dcp_098.py)

----

99. ### Microsoft

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given `[100, 4, 200, 1, 3, 2]`, the longest consecutive element sequence is `[1, 2, 3, 4]`. Return its length: `4`.

Your algorithm should run in **O(n)** complexity.

[Longest Consecutive Elements](dcp_099.py)

----

100. ### Google

You are in an infinite 2D grid where you can move in any of the 8 directions:
```
 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
```

You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: `[(0, 0), (1, 1), (1, 2)]`
Output: `2`

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

[Minimum steps to coordinates](dcp_100.py)

----

101. ### Alibaba

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See [Goldbach’s conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture).

Example:
```
Input: 4
Output: 2 + 2 = 4
```
If there are more than one solution possible, return the lexicographically smaller solution.

[Prime Numbers](dcp_101.py)

----

102. ### Lyft

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is `[1, 2, 3, 4, 5]` and K is `9`, then it should return `[2, 3, 4]`, since `2 + 3 + 4 = 9`.

[Continguous elements sum](dcp_102.py)

----

103. ### Square

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string `"figehaeci"` and the set of characters `{a, e, i}`, you should return `"aeci"`.

If there is no substring containing all the characters in the set, return `null`.

[Smallest substring for pattern](dcp_103.py)

----

104. ### Google

Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, `1 -> 4 -> 3 -> 4 -> 1` returns `True` while `1 -> 4` returns `False`.

[Palindrome Linked List](dcp_104.py)

----

106. ### Pinterest

Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, `[2, 0, 1, 0]` returns `True` while `[1, 1, 0, 1]` returns `False`.

[Jump to reach end](dcp_106.py)

----

107. ### Microsoft

Print the nodes in a binary tree level-wise. For example, the following should print `1, 2, 3, 4, 5`.

```
  1
 / \
2   3
   / \
  4   5
```

[Level Order traversal](dcp_107.py)

----

108. ### Google

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is `abcde` and B is `cdeab`, return `true`. If A is `abc` and B is `acb`, return `false`.

[Same string after shifting](dcp_108.py)

----

109. ### Cisco

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, `10101010` should be `01010101`. `11100010` should be `11010001`.

Bonus: Can you do this in one line?

[Swap bits](dcp_109.py)

----

110. ### Facebook

Given a binary tree, return all paths from the root to leaves.

For example, given the tree
```
   1
  / \
 2   3
    / \
   4   5
```
it should return `[[1, 2], [1, 3, 4], [1, 3, 5]]`.

[All root to leaf paths](dcp_110.py)

----

111. ### Google

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is `“ab”`, and S is `“abxaba”`, return `0, 3, and 4`.

[Find anagrams](dcp_111.py)

----

112. ### Twitter

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

[Lowest Common Ancestor](dcp_112.py)

----

113. ### Google

Given a string of words delimited by spaces, reverse the words in string.

For example, given `“hello world here”`, return `“here world hello”`

Follow-up: given a mutable string representation, can you perform this operation in-place?

[Reverse Sentence](dcp_113.py)

----

114. ### Facebook

Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters.

For example, given `hello/world:here`, return `here/world:hello`

Follow-up: Does your solution work for the following cases: `hello/world:here/`, `hello//world:here`

[Reverse sentence with delimiters](dcp_114.py)

----

115. ### Google

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node’s descendants. The tree s could also be considered as a subtree of itself.

[Subtree](dcp_115.py)

----

116. ### Jane Street

Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, `generate()` should return a tree whose size is unbounded but finite.

[Huge Tree](dcp_116.py)

----

117. ### Facebook

Given a binary tree, return the level of the tree with minimum sum.

[Level of the tree with minimum sum](dcp_117.py)

----

118. ### Google

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given `[-9, -2, 0, 2, 3]`, return `[0, 4, 4, 9, 81]`.

[Square the elements](dcp_118.py)

----

119. ### Google

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals `[0, 3], [2, 6], [3, 4], [6, 9]`, one set of numbers that covers all these intervals is `{3, 6}`.

[Smallest Interval](dcp_119.py)

----

120. ### Microsoft

Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. And in every `even call of getInstance()`, *return the first instance* and in `every odd call of getInstance()`, *return the second instance*.

[Singleton Pattern](dcp_120.py)

----

121. ### Google

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given `‘waterrfetawx’` and a k of 2, you could delete f and x to get `‘waterretaw’`.

[Palindrome string](dcp_121.py)

----

122. ### Zillow

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix
```
0 3 1 1
2 0 0 4
1 5 3 1
```

The most we can collect is `0 + 2 + 1 + 5 + 3 + 1 = 12` coins.

[BFS on matrix](dcp_122.py)

----

123. ### LinkedIn

Given a string, return whether it represents a number. Here are the different kinds of numbers:

- `10`, a positive integer
- `-10`, a negative integer
- `10.1`, a positive real number
- `-10.1`, a negative real number
- `1e5`, a number in scientific notation

And here are examples of non-numbers:
```
“a”
“x 1”
“a -2”
”-“
```

[Is a Number](dcp_123.py)

----

124. ### Microsoft

You have 100 fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given `n`, returns the number of rounds you’d expect to play until one coin remains.

[Log](dcp_124.py)

----

125. ### Google

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20
```
    10
   /   \
 5      15
       /  \
     11    15
```
Return the nodes 5 and 15.

[Two sum on BST](dcp_125.py)

----

126. ### Facebook

Write a function that rotates a list by k elements.

For example, `[1, 2, 3, 4, 5, 6] `rotated by two becomes `[3, 4, 5, 6, 1, 2]`.

Try solving this without creating a copy of the list. How many swap or move operations do you need?

[Rotate list](dcp_126.py)

----

127. ### Microsoft

Let’s represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:
`1 -> 2 -> 3 -> 4 -> 5` is the number `54321`.

Given two linked lists in this format, return their sum in the same linked list format.
For example, given
`9 -> 9`, `5 -> 2` return `124 (99 + 25)` as: `4 -> 2 -> 1`

[Linked list sum](dcp_127.py)

----

128. 

The `Tower of Hanoi` is a puzzle game with three rods and n disks, each a different size.

All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the bottom and the smallest one at the top.

The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:

You can only move one disk at a time.
A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
You cannot place a larger disk on top of a smaller disk.
Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the rods are numbered, with the first rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.

For example, with n = 3, we can do this in 7 moves:

```
Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3
```

[Tower of Hanoi](dcp_128.py)

----

129. 

Given a real number n, find the square root of n.
For example, given `n = 9`, return `3`.

[Square root](dcp_129.py)

----

130. ### Facebook

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells.

You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given `k = 2` and the array `[5, 2, 4, 0, 1]`, you should return `3`.

[Buy Sell stock](dcp_130.py)

----

131. ### Snapchat

Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.

[Clone Linked List](dcp_131.py)

----

132. ### Riot Games

Design and implement a `HitCounter class` that keeps track of requests (or hits). It should support the following operations:

`record(timestamp)`: records a hit that happened at timestamp
`total()`: returns the total number of hits recorded
`range(lower, upper)`: returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?

[HitCounter](dcp_132.py)

----

133. ### Amazon
Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.
```
   10
  /  \
 5    30
     /  \
   22    35
```
You can assume each node has a parent pointer.

[Inorder successor](dcp_133.py)

----

134. ### Facebook

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

`init(arr, size)`: initialize with the original large array and size.

`set(i, val)`: updates index at i with val.

`get(i)`: gets the value at index i.

[space-efficient data structure](dcp_134.py)

----

135. ### Apple

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is `[10, 5, 1, -1]`, which has `sum 15`.
```
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
```

[Minimum sum path](dcp_135.py)

----

136. ### Google

Given an N by M matrix consisting only of 1’s and 0’s, find the largest rectangle containing only 1’s and return its area.

For example, given the following matrix:
```
[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
```

Return `4`.

[Largest rectangle](dcp_136.py)

----

137. ### Amazon

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

`init(size)`: initialize the array with size

`set(i, val)`: updates index at i with val where val is either 1 or 0.

`get(i)`: gets the value at index i.

[Bit array](dcp_137.py)

----

138. ### Google

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, `1¢, 5¢, 10¢, and 25¢`.

For example, given `n = 16`, `return 3` since we can make it with a 10¢, a 5¢, and a 1¢

[Minimum coins](dcp_138.py)

----

139. ### Google

Given an iterator with methods `next()` and `hasNext()`, create a wrapper iterator, PeekableInterface, which also implements **peek()**. peek shows the next element that would be returned on next().

Here is the interface:

```
class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
```

[PeekableInterface](dcp_139.py)

----

140. ### Facebook

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array `[2, 4, 6, 8, 10, 2, 6, 10]`, return `4 and 8`. The order does not matter.

Follow-up: Can you do this in linear time and constant space?

[Two single numbers](dcp_140.py)

----

141. ### Microsoft

Implement 3 stacks using a single list:

```
class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
```

[3 stacks using single list](dcp_141.py)

----

142. ### Google

You're given a string consisting solely of `(`, `)`, and `*`. `*` can represent either a `(`, `)`, or an empty string. Determine whether the parentheses are balanced.

For example, `(()*` and `(*)` are balanced. `)*(` is not balanced.

[Balanced Parenthesis](dcp_142.py)

----

143. ### Amazon

Given a pivot x, and a list lst, partition the list into three parts.

- The first part contains all elements in lst that are less than x

- The second part contains all elements in lst that are equal to x

- The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given `x = 10` and `lst = [9, 12, 3, 5, 14, 10, 10]`, one partition may be `[9, 3, 5, 10, 10, 12, 14]`.

[Partition](dcp_143.py)

----

144. ### Google

Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where **distance is measured in array indices**.

For example, given `[4, 1, 3, 5, 6]` and `index 0`, you should return `3`.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?

[Nearest larger number](dcp_144.py)

----

145. ### Google

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given `1 -> 2 -> 3 -> 4`, return `2 -> 1 -> 4 -> 3`.

[Swap nodes in LinkedList](dcp_145.py)

----

146. ### BufferBox

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:
```
   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
```

should be pruned to:

```
   0
  / \
 1   0
    /
   1
```

We do not remove the tree at the root or its left child because it still has a 1 as a descendant.

[Prune tree](dcp_146.py)

----

147. 

Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.

[Pancake Sort](dcp_147.py)

----

148. ### Apple

Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. Gray code is common in hardware so that we don’t see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for `n = 2`, one gray code would be `[00, 01, 11, 10]`.

[Grey code](dcp_148.py)

----

149. ### Goldman Sachs

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given `L = [1, 2, 3, 4, 5]`, `sum(1, 3)` should return `sum([2, 3])`, which is `5`.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.

[Subarray sum](dcp_149.py)

----

150. ### LinkedIn

Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points `[(0, 0), (5, 4), (3, 1)]`, the `central point (1, 2)`, and `k = 2`, return `[(0, 0), (3, 1)]`.

[Closest points](dcp_150.py)

----

151. 

Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

```
B B W
W W W
W W W
B B B
```

Becomes

```
B B G
G G G
G G G
B B B
```

[Floodfill](dcp_151.py)

----

152. ### Triplebyte

You are given `n` numbers as well as `n` probabilities that sum up to `1`. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers `[1, 2, 3, 4]` and probabilities `[0.1, 0.5, 0.2, 0.2]`, your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.

[Arbitrary Probability](dcp_152.py)

----

153. 

Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words `"hello"`, and `"world"` and a text content of `"dog cat hello cat dog dog hello cat world"`, return `1` because there's only one word "cat" in between the two words.

[Min distance between words](dcp_153.py)

----

154. ### Amazon

Implement a `stack API using only a heap`. A stack implements the following methods:

- `push(item)`, which adds an element to the stack

- `pop()`, which removes and returns the most recently added element (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:

- `push(item)`, which adds a new key to the heap

- `pop()`, which removes and returns the max value of the heap

[Stack using heap](dcp_154.py)

----

155. ### MongoDB

Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given `[1, 2, 1, 1, 1, 4, 0]`, return `1`.

[Boyer-Moore voting algorithm](dcp_155.py)

----

156. ### Facebook

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given `n = 13`, return `2` since `13 = 3^2 + 2^2 = 9 + 4`.

Given `n = 27`, return `3` since `27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9`.

[Perfect Squares](dcp_156.py)

----

157. ### Amazon

Given a string, determine whether any permutation of it is a palindrome.

For example, `carrace` should return `true`, since it can be rearranged to form `racecar`, which is a palindrome. `daily` should return `false`, since there's no rearrangement that can form a palindrome.

[Permuatation is Palindrome](dcp_157.py)

----

158. ### Slack

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:
```
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
```

Return two, as there are only two ways to get to the bottom right:

- Right, down, down, right

- Down, right, down, right

The top left corner and bottom right corner will always be 0.

[Number of paths with contraints](dcp_158.py)

----

159. ### Google

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string `"acbbac"`, return `"b"`. Given the string `"abcdef"`, return `null`.

[First repeating character](dcp_159.py)

----

160. ### Uber

Given a tree where each edge has a weight, compute the `length of the longest path` in the tree.

For example, given the following tree:
```
   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
```

and the weights: `a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1`, the longest path would be `c -> a -> d -> f`, with a length of `17`.

The path does not have to pass through the root, and each node can have any amount of children.

[Longest path sum](dcp_160.py)

----

161. ### Facebook
Given a 32-bit integer, return the number with its bits reversed.

For example, given the `binary number 1111 0000 1111 0000 1111 0000 1111 0000`, return `0000 1111 0000 1111 0000 1111 0000 1111`.

[Reverse bits](dcp_161.py)

----

162. ### Square

Given a list of words, return the shortest unique prefix of each word. For example, given the list:
```
dog
cat
apple
apricot
fish
```

Return the list:
```
d
c
app
apr
f
```

[Prefix of each word](dcp_162.py)

----

163. ### Jane Street

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands.

For example: `[5, 3, '+']` should return `5 + 3 = 8`.

For example, `[15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']` should return 5, since it is equivalent to `((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5`.

You can assume the given expression is always valid.

[Evaluate Reverse Polish Notation](dcp_163.py)

----

164. ### Google

You are given an array of length `n + 1` whose elements belong to the set `{1, 2, ..., n}`. 

By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.

[Duplicate element](dcp_164.py)

----

165. ### Google

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array `[3, 4, 9, 6, 1]`, return `[1, 1, 2, 1, 0]`, since:

- There is 1 smaller element to the right of 3

- There is 1 smaller element to the right of 4

- There are 2 smaller elements to the right of 9

- There is 1 smaller element to the right of 6

- There are no smaller elements to the right of 1

[Smaller counts](dcp_165_a.py)
[Smaller counts](dcp_165_b.py)

----

166. ### Uber

Implement a `2D iterator class`. It will be initialized with an array of arrays, and should implement the following methods:

`next()`: returns the next element in the array of arrays. If there are no more elements, raise an exception.

`has_next()`: returns whether or not the iterator still has elements left.

For example, given the input `[[1, 2], [3], [], [4, 5, 6]]`, calling next() repeatedly should output `1, 2, 3, 4, 5, 6`.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.

[2D iterator](dcp_166.py)

----

167. ### Airbnb

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list `["code", "edoc", "da", "d"]`, return `[(0, 1), (1, 0), (2, 3)]`.

[Palindrome Pairs](dcp_167.py)

----

168. ### Facebook

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

you should return:

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

Follow-up: What if you couldn’t use any extra space?

[Rotate Matrix](dcp_168.py)

----

169. ### Google

Given a linked list, sort it in `O(n log n)` time and constant space.

For example, the linked list `4 -> 1 -> -3 -> 99` should become `-3 -> 1 -> 4 -> 99`.

[Sort Linked List](dcp_169.py)

----

170. ### Facebook

Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same length as start and end and is lowercase.

For example, given `start = "dog", end = "cat"`, and `dictionary = {"dot", "dop", "dat", "cat"}`, return `["dog", "dot", "dat", "cat"]`.

Given `start = "dog", end = "cat"`, and `dictionary = {"dot", "tod", "dat", "dar"}`, return `null` as there is no possible transformation from dog to cat.

[Word Ladder Length](dcp_170-a.py)

[Word Ladder](dcp_170-b.py)

----

171. ### Amazon

You are given a list of data entries that represent entries and exits of groups of people into a building.

An entry looks like this:

`{"timestamp": 1526579928, "count": 3, "type": "enter"}`
This means 3 people entered the building.

An exit looks like this:

`{"timestamp": 1526580382, "count": 2, "type": "exit"}`
This means that 2 people exited the building.

Timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.

[Busiest Period in Room](dcp_171.py)

----

172. ### Dropbox

Given a string s and a list of words words, where each word is the same length, find all starting indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given `s = "dogcatcatcodecatdog"` and `words = ["cat", "dog"]`, return `[0, 13]`, since `"dogcat"` starts at index 0 and "catdog" starts at index 13.

Given `s = "barfoobazbitbyte"` and `words = ["dog", "cat"]`, return `[]` since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.

[Words palindrome in Sentence](dcp_172.py)

----

173. ### Stripe

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:
```
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
```
[Flatten Dictionary](dcp_173.py)

----

175. ### Google

You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps `5000`, and the following transition probabilities:

```
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
```

One instance of running this Markov chain `might produce { 'a': 3012, 'b': 1656, 'c': 332 }`.

[Markov chain](dcp_175.py)

----

176. ### Bloomberg

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given `s1 = abc and s2 = bcd`, return `true` since we can map a to b, b to c, and c to d.

Given `s1 = foo and s2 = bar`, return `false` since the o cannot map to two characters.

[Character mapping](dcp_176.py)

----

177. ### Airbnb

Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list `7 -> 7 -> 3 -> 5` and `k = 2`, it should become `3 -> 5 -> 7 -> 7`.

Given the linked list `1 -> 2 -> 3 -> 4 -> 5` and `k = 3`, it should become `3 -> 4 -> 5 -> 1 -> 2`.

[Rotate Linked-list](dcp_177.py)

----

178. ### Two Sigma

Alice wants to join her school’s Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

- The first game: roll a die repeatedly. Stop rolling once you get a `five followed by a six`. Your number of rolls is the amount you pay, in dollars.

- The second game: same, except that the stopping condition is a `five followed by a five`.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.

[Probability Game](dcp_178.py)

----

179. ### Google

Given the sequence of keys visited by a `postorder traversal` of a binary search tree, reconstruct the tree.

For example, given the sequence `2, 4, 3, 8, 7, 5`, you should construct the following tree:

```
    5
   / \
  3   7
 / \   \
2   4   8
```

[Reconstruct binary tree from Postorder](dcp_179.py)

----

180. ### Google

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example,

stack is `[1, 2, 3, 4, 5]`, it should become `[1, 5, 2, 4, 3]`. 

stack is `[1, 2, 3, 4]`, it should become `[1, 4, 2, 3]`.

Hint: Try working backwards from the end state.

[Interleave Stack](dcp_180.py)

----

181. ### Google

Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string `"racecarannakayak"`, return `["racecar", "anna", "kayak"]`.

Given the input string `"abc"`, return `["a", "b", "c"]`.

[Palindrome's in String](dcp_181.py)

----

182. ### Facebook

A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected. For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. You can choose to represent the graph as either an adjacency matrix or adjacency list.

[Critical connections](dcp_182.py)

----

184. ### Amazon

Given n numbers, find the greatest common denominator between them.

For example, given the numbers `[42, 56, 14]`, return `14`.

[GCD](dcp_184.py)

----

185. ### Google

Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don’t intersect, return 0.

For example, given the following rectangles:
```
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
```

and
```
{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
```

return `6`.

[Area of Intersecting rectangles](dcp_185.py)

----

186. ### Microsoft

Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.

For example, given `[5, 10, 15, 20, 25]`, return the sets `{10, 25}` and `{5, 15, 20}`, which has a difference of `5`, which is the smallest possible difference.

[Smallest difference in subset](dcp_186.py)

----

187. ### Google

You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:
```
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
```

return `true` as the first and third rectangle overlap each other.

----

188. ### Google

What will this code print out?
```
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
```

How can we make it print out what we apparently want?

[Code fix](dcp_188.py)

----

189. ### Google

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array `[5, 1, 3, 5, 2, 3, 4, 1]`, return `5` as the longest subarray of distinct elements is `[5, 2, 3, 4, 1]`.

[Longest subarray with distinct elements](dcp_189.py)

----

190. ### Facebook

Given a circular array, compute its maximum subarray sum in O(n) time.

For example, given `[8, -1, 3, 4]`, return `15` as we choose the numbers `3, 4, and 8` where the 8 is obtained from wrapping around.

Given `[-4, 5, 1, 0]`, return `6` as we choose the numbers 5 and 1.


[Maximum subarray sum](dcp_190.py)

----

191. ### Stripe

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can “touch”, such as [0, 1] and [1, 2], but they won’t be considered overlapping.

For example, given the intervals `(7, 9), (2, 4), (5, 8)`, return `1` as the last interval can be removed and the first two won’t overlap.

The intervals are not necessarily sorted in any order.

[Non-overlapping intervals](dcp_191.py)

----

192. ### Google

You are given an array of nonnegative integers. Let’s say you start at the beginning of the array and are trying to advance to the end. You can advance at most, the number of steps that you’re currently on. Determine whether you can get to the end of the array.

For example, given the array `[1, 3, 1, 2, 0, 1]`, we can go from indices `0 -> 1 -> 3 -> 5`, so return `true`.

Given the array `[1, 2, 1, 0, 0]`, we can’t reach the end, so return `false`.

[Reach end](dcp_192.py)

----

193. ### Affirm

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock. You’re also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

For example, given `[1, 3, 2, 8, 4, 10]` and `fee = 2`, you should `return 9`, since you could buy the stock at $1, and sell at $8, and then buy it at $4 and sell it at $10. Since we did two transactions, there is a $4 fee, so we have 7 + 6 = 13 profit minus $4 of fees.

[Best Time to Buy and Sell Stock with Transaction Fee](dcp_193.py)

----

195. ### Google

Let `A` be an `N by M` matrix in which every row and every column is sorted.

Given `i1, j1, i2, and j2`, compute the number of elements of M _smaller_ than `M[i1, j1]` and _larger_ than `M[i2, j2]`.

For example, given the following matrix:
```
[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]
```
And `i1 = 1, j1 = 1, i2 = 3, j2 = 3`, return `14` as there are 14 numbers in the matrix smaller than 6 or greater than 23.

[Count Numbers](dcp_195.py)

----

196. ### Apple

Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

For example, given the following tree:
```
  5
 / \
2  -5
```
Return `2` as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.

[Frequent Tree Sum](dcp_196.py)

----

197. ### Amazon

Given an array and a number k that’s smaller than the length of the array, rotate the array to the right k elements in-place.

[Rotate right array](dcp_197.py)

----

198. ### Google

Given a set of distinct positive integers, find the largest subset such that every pair of elements in the `subset (i, j)` satisfies either `i % j = 0 or j % i = 0`.

For example, given the set `[3, 5, 10, 20, 21]`, you should return `[5, 10, 20]`. Given `[1, 3, 6, 24]`, return `[1, 3, 6, 24]`.

[Largest divisible subset](dcp_198.py)

----

199. ### Facebook

Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.

For example, given `(()`, you could return `(())`. Given `))()(`, you could return `()()()()`.

[Make Parentheses balanced](dcp_199.py)

----

200. ### Microsoft

Let X be a set of n intervals on the real line. We say that a set of points P “stabs” X if every interval in X contains at least one point in P. Compute the smallest set of points that stabs X.

For example, given the intervals `[(1, 4), (4, 5), (7, 9), (9, 12)]`, you should return `[4, 9]`.

[Minimum stab points](dcp_200.py)

----

202. ### Palantir

Write a program that checks whether an integer is a palindrome. For example, `121` is a `palindrome`, as well as 888. 678 is not a palindrome. _Do not convert the integer into a string_.

[Number Palindrome](dcp_202.py)

----

203. ### Uber

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element in `O(log N) time`. You may assume the array does not contain duplicates.

For example, given `[5, 7, 10, 3, 4]`, return `3`.

[Find min element in rotated array](dcp_203.py)

----

212. ### Dropbox

Spreadsheets often use this alphabetical encoding for its columns: `"A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....`

Given a column number, return its alphabetical column id. For example, given `1`, return `A`. Given `27`, return `AA`.

[Column Number](dcp_212.py)

----

213. ### Snapchat

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given `“2542540123”`, you should return `['254.25.40.123', '254.254.0.123']`.

[Restore IP addresses](dcp_213.py)

----

220. ### Square

In front of you is a row of N coins, with values `v1, v1, ..., vn`

You are asked to play the following game. You and an opponent take turns choosing either the first or last coin from the row, removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, if you move first, assuming your opponent plays optimally.

[Coin Game](dcp_220.py)

----

221. ### Zillow

Let's define a `sevenish` number to be one which is either a power of `7`, or the sum of unique powers of `7`. The first few sevenish numbers are `1, 7, 8, 49, and so on`.  
Create an algorithm to find the nth sevenish number.

[Sevenish Number](dcp_221.py)

----

223. ### Palantir

Typically, an implementation of in-order traversal of a binary tree has `O(h)` space complexity, where h is the height of the tree. Write a program to compute the in-order traversal of a binary tree using `O(1)` space.

[Morris Traversal](dcp_223.py)

----

225. ### Bloomberg

There are `N` prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the `k`th person, and removing every successive `k`th person going clockwise until there is no one left.

Given `N` and `k`, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if `N = 5` and `k = 2`, the order of executions would be `[2, 4, 1, 5, 3]`, so you should return `3`.

Bonus: Find an `O(log N)` solution if `k = 2`.

[Josephus Problem](dcp_225.py)

----

228. ### Twitter

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. For example, given `[10, 7, 76, 415]`, you should return `77641510`.

[Largest Number](dcp_228.py)

----

230. ### Goldman Sachs

You are given `N` identical eggs and access to a building with `k` floors. Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks when dropped from the `x`th floor, you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the `minimum number of trial drops` it will take, in the worst case, to identify this floor.

For example, if `N = 1` and `k = 5`, we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor, so our solution will be 5.

[Min Drops](dcp_230.py)

----

235. ### Facebook

Given an array of numbers of length N, find both the minimum and maximum using less than `2 * (N - 2)` comparisons

[Minimum Comparison](dcp_235.py)

----

236. ### Nvidia

You are given a list of `N` points `(x1, y1), (x2, y2), ..., (xN, yN)` representing a _polygon_. You can assume these points are given in order; that is, you can construct the polygon by connecting point 1 to point 2, point 2 to point 3, and so on, finally looping around to connect point N to point 1.

Determine if a new point p lies inside this polygon. (If p is on the boundary of the polygon, you should return False).

[Point in Polygon](dcp_236.py)

----

238. ### MIT

Blackjack is a two player card game whose rules are as follows:

The player and then the dealer are each given two cards.  
The player can then `hit`, or ask for arbitrarily many additional cards, so long as their total does not exceed 21.
The dealer must then hit if their total is 16 or lower, otherwise pass.  
Finally, the two compare totals, and the one with the greatest sum not exceeding 21 is the winner.  
For this problem, cards values are counted as follows: each card between 2 and 10 counts as their face value, face cards count as 10, and aces count as 1.  

Given perfect knowledge of the sequence of cards in the deck, implement a blackjack solver that maximizes the player's score (that is, wins minus losses).  

[Blackjack](dcp_238.py)

----

241. ### Palantir

In academia, the `h-index` is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:

A researcher has index `h` if **at least** `h` of her `N` papers have `h` citations each. If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose `N = 5`, and the respective citations of each paper are `[4, 3, 0, 1, 5]`. Then the `h-index` would be `3`, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their `h-index`.

[H Index](dcp_241.py)

----

244. ### Square

The `Sieve of Eratosthenes` is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

[Sieve of Eratosthenes](dcp_244.py)

----

253. ### PayPal

Given a string and a number of lines k, print the string in zigzag form. 

In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence `"thisisazigzag"` and `k = 4`, you should print:
```
t     a     g
 h   s z   a
  i i   i z
   s     g
```

[Zigzag String Concatenation](dcp_253_a.py)

[Zigzag String Print](dcp_253_b.py)

----

254. ### Yahoo

Recall that a full binary tree is one in which each node is either a leaf node, or has two children. Given a binary tree, convert it to a full one by removing nodes with only one child.

```

         0
      /     \
    1         2
  /            \
3                 4
  \             /   \
    5          6     7
```

You should convert it to:
```
     0
  /     \
5         4
        /   \
       6     7
```

[Truncate Tree](dcp_254.py)

----

272. ### Spotify

Write a function, `throw_dice(N, faces, total)`, that determines how many ways it is possible to throw `N` dice with some number of faces each to get a specific total.

For example, `throw_dice(3, 6, 7)` should equal `15`.

[Throw Dice](dcp_272.py)

----

273. ### Apple

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given `[-6, 0, 2, 40]`, you should return `2`. Given `[1, 5, 7, 8]`, you should return False.

[Fixed Point](dcp_273.py)

----

274. ### Facebook

Given a string consisting of _parentheses, single digits, and positive and negative signs_, convert the string into a mathematical expression to obtain the answer.  

Don't use eval or a similar built-in parser.

For example, given `-1 + (2 + 3)`, you should return `4`.

[Basic Calculator](dcp_274.py)

----

283. ### Google

A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are `2, 3, and 5`.  

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.

[Regular Number](dcp_283.py)

----

289. ### Google

The game of `Nim` is played as follows  
Starting with three heaps, each containing a variable number of items, two players take turns removing one or more items from a single pile. The player who eventually is forced to take the last stone loses.  
For example, if the initial heap sizes are `3, 4, and 5`, a game could be played as shown below:
```
  A  |  B  |  C
-----------------
  3  |  4  |  5
  3  |  1  |  3
  3  |  1  |  3
  0  |  1  |  3
  0  |  1  |  0
  0  |  0  |  0 
```
In other words, to start, the first player takes three items from pile B. The second player responds by removing two stones from pile C. The game continues in this way until player one takes last stone and loses.

Given a list of non-zero starting values `[a, b, c]`, and assuming optimal play, determine whether the first player has a forced win.

[Nim Game](dcp_289.py)

----

301. ### Triplebyte

Implement a data structure which carries out the following operations without resizing the underlying array:

`add(value)` : Add a value to the set of values.  
`check(value)` : Check whether a value is in the set.  
The check method may return occasional false positives (in other words, incorrectly identifying an element as part of the set), but should always correctly identify a true element.  

[Bloom Filter](dcp_301.py)

----

314. ### Spotify

You are the technical director of WSPT radio, serving listeners nationwide. For simplicity's sake we can consider each listener to live along a horizontal line stretching from `0 (west)` to `1000 (east)`.

Given a list of `N` listeners, and a list of `M` radio towers, each placed at various locations along this line, determine what the minimum broadcast range would have to be in order for each listener's home to be covered.

For example, suppose `listeners = [1, 5, 11, 20]`, and `towers = [4, 8, 15]`. In this case the *minimum* range would be `5`, since that would be required for the *tower at position 15* to reach the *listener at position 20*.

[Tower Range](dcp_314.py)

----

336. ### Microsoft

Write a program to determine how many distinct ways there are to create a max heap from a list of N given integers.  
For example, if `N = 3`, and our integers are `[1, 2, 3]`, there are `two ways`, shown below.  
```
  3      3
 / \    / \
1   2  2   1
```
[Number of Heaps](dcp_336.py)

----

338. ### Facebook

Given an integer n, find the next biggest integer with the same number of 1-bits on.  
For example, given the number `6`(`0110` in binary), return `9 (1001)`.

[snoob](dcp_338.py)

----

348. ### Zillow.

A ternary search tree is a trie-like data structure where each node may have up to three children. Here is an example which represents the words code, cob, be, ax, war, and we.

```
       c
    /  |  \
   b   o   w
 / |   |   |
a  e   d   a
|    / |   | \ 
x   b  e   r  e  
```

The tree is structured according to the following rules:

left child nodes link to words lexicographically earlier than the parent prefix  
right child nodes link to words lexicographically later than the parent prefix  
middle child nodes continue the current word  
For instance, since code is the first word inserted in the tree, and cob lexicographically precedes cod, cob is represented as a left child extending from cod.  

Implement insertion and search functions for a ternary search tree.

[Ternary Tree](dcp_348.py)

----

353. ### Square

You are given a histogram consisting of rectangles of different heights. These heights are represented in an input list, such that `[1, 3, 2, 5]` corresponds to the following diagram:
```
      x
      x  
  x   x
  x x x
x x x x
```
Determine the area of the largest rectangle that can be formed only from the bars of the histogram. For the diagram above, for example, this would be **six**, representing the `2 x 3` area at the bottom right.

[Largest Rectangle](dcp_353.py)

----

359. ### Slack

You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

For example, the input could be `niesevehrtfeev`, which is an anagram of `threefiveseven`.  
_Note that there can be multiple instances of each integer_.

Given this string, return the original integers in sorted order. In the example above, this would be `357`.

[Number Anagram](dcp_359.py)

----

360. ### Spotify

You have access to ranked lists of songs for various users. Each song is represented as an integer, and more preferred songs appear earlier in each list. For example, the list `[4, 1, 7]` indicates that a user likes song 4 the best, followed by songs 1 and 7.

Given a set of these ranked lists, interleave them to create a playlist that satisfies everyone's priorities.

For example, suppose your input is `{[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]}`. In this case a satisfactory playlist could be `[2, 1, 6, 7, 3, 9, 5]`.

[Interleave Lists](dcp_360.py)

----
