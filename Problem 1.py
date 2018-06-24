muls = []
for i in range(1000):
  if i % 3 == 0 or i % 5 == 0:
    muls.append(i)
print(muls)
sum = 0
for x in muls:
  sum += x
print(sum)
