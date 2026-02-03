Whole point is in understanding two lines:
where the code start: current = i - (current - 1) // 2
and what to return: s[current: current+maxL]

s = "ababc"
    01234
m = 5

i = 0:
  l1 = x(0, 0) → "a" (length 1)
  l2 = x(0, 1) → "ab" not palindrome (length 0)
  leng = max(1, 0) = 1
  maxL = 1, current = 0 - 0 = 0

i = 1:
  l1 = x(1, 1) → "aba" ✅ (length 3)
  l2 = x(1, 2) → "ba" not palindrome (length 0)
  leng = max(3, 0) = 3
  maxL = 3, current = 1 - 1 = 0

i = 2:
  l1 = x(2, 2) → "aba" again (length 3)
  l2 = x(2, 3) → "ab" not palindrome
  leng = 3
  (Same as maxL, no update)

i = 3:
  l1 = x(3, 3) → "b" (length 1)
  l2 = x(3, 4) → "bc" not palindrome
  leng = 1

i = 4:
  l1 = x(4, 4) → "c" (length 1)
  leng = 1

Final:
  current = 0
  maxL = 3
  
Return s[0:3] = "aba" ✅