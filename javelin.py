f = open("javelin.txt", "r")
w = open("javelout.txt", "w")
n = int(f.readline())
scores = list(map(int, f.readline().split()))
current = []
curMax = -1000000000
count = 0
for s in scores:
    current.append(s)
    if s > curMax:
        count += 1
        curMax = s
w.write(str(count))
