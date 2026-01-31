The first method to solve this question is to find the length and then find the middle and return middle and rest.

It perfectly work and Time complexity is O(n) but based on what I see, having a def inside another def is not

what reviewers are looking for.

!\[Brutforce](BF.jpg)



But there is another way: weird but works.

you have two indicator, left and right, right jumps two when left jump one.

When right reaches to end, left is in the middle.

