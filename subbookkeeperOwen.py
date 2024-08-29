f = open("bookin.txt", "r")
w = open("bookout.txt", "w")
n = int(f.readline())
word = f.readline()
word = list(word)
for i in range(len(word)):
    if word[i] == "?":
        search = i
lCount = 1
rCount = 1
final = 0
for i in range(search, n):
    if word[i] != word[i + 1]:
        break
    rCount += 1
for i in range(search, -1, -1):
    if word[i] != word[i - 1]:
        break
    lCount += 1
if lCount >= rCount:
    word[search] = word[search - 1] if search - 1 >= 0 else word[search + 1]
else:
    word[search] = word[search + 1] if search + 1 < n else word[search - 1]
for i in range(n - 1):
    if word[i] != word[i + 1]:
        continue
    final += 1
w.write(str(final))

