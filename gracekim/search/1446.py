# 1446 지름길 / Silver 1

import sys
input = sys.stdin.readline

n, d = map(int, input().split())

dp = [i for i in range(d+1)]

shortcuts = []

for _ in range(n):
  start, dest, length = map(int, input().split())
  if dest - start > length:
    shortcuts.append((start, dest, length))
shortcuts.sort()

for start, dest, length in shortcuts:
  for i in range(1, d+1):
    if dest == i:
      dp[i] = min(dp[i], dp[start]+length)
    else:
      dp[i] = min(dp[i], dp[i-1]+1)
print(dp[d])