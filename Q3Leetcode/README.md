This is the question 3 of Leetcode.

There are two methods: Bruteforce and efficient.

For bruteforece which is O(N^3).
why bruteforce is wasteful: imagine checking "abca"

* we check a, b, c->all good
* we check a again-> duplicate
* Then we throw away all that work and start fresh with "bcab"



!\[BruteForce Solution](Brutforce.jpg)



And better solution is sliding:



instead of going through every possible combination, just move along the window and remove the left duplicate



!\[Sliding Window Example 1](https://raw.githubusercontent.com/majdst/LeetCode2026/main/slide1.jpg)

and

!\[Sliding Window Example 1](https://raw.githubusercontent.com/yourusername/yourrepo/main/slide1.jpg)

