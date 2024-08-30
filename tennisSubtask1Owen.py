f = open("tennisin.txt", "r")
w = open("tennisout.txt", "w")
n, m = map(int, f.readline().split())
bins = list(map(int, f.readline().split()))
original = []
for b in bins:
    original.append(b)
moves = []
acc = []
count = 0
for i in range(m):
    moves.append(tuple(map(int, f.readline().split())))
j = 0
while True:
    for i, mo in enumerate(moves):
        if bins[mo[0] - 1] == 0:
            w.write(str(j * m + i))
            exit()
        bins[mo[0] - 1] -= 1
        bins[mo[1] - 1] += 1
    if original == bins:
        w.write("FOREVER")
        exit()
    j += 1
