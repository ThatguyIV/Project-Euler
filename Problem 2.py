fibs = {1:1,2:2}
def fib(i):
  if i in fibs:
    return fibs[i]
  else:
    fibs[i] = fib(i-1) + fib(i-2)
    return fibs[i]
nums = []
x = 1
while fib(x) <= 4000000:
  if fib(x) % 2 == 0:
    nums.append(fib(x))
  x += 1
sum = 0
for y in nums:
  sum += y
print(sum)
