import sys
from collections import deque
sys.setrecursionlimit(1000000000)
n = 0
k = 0
costs = []
input_file = open("shopin.txt", "r")
output_file = open("shopout.txt", "w")

input_line = input_file.readline()
n, k = map(int, input_line.split())
input_line = input_file.readline()
costs = list(map(int, input_line.split()))
items = deque(costs)
count = 0
l = 0
r = n - 1
while l <= r <= n - 1:
    while k > 0:
        count += items[0]
        items.pop()
        items.popleft()
        k -= 1
    if not (l <= r <= n - 1):
        break
    r = l + 1
    try:
        count += items[r]
    except IndexError:
        break
    l += 2
    r += 2
output_file.write("%d\n" % count)
input_file.close()
output_file.close()
