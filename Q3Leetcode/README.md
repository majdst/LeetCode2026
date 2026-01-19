This is the question 3 of Leetcode.

There are two methods: Bruteforce and efficient.

For bruteforece which is O(N^3).
why bruteforce is wasteful: imagine checking "abca"

* we check a, b, c->all good
* we check a again-> duplicate
* Then we throw away all that work and start fresh with "bcab"



!\[Linked List remove](https://raw.githubusercontent.com/majdst/LeetCode2026/main/Q3Leetcode/Brutforce.JPG)



And better solution is sliding:



instead of going through every possible combination, just move along the window and remove the left duplicate



!\[Description](slide1.jpg)

and

!\[Description](slide2.jpg)

