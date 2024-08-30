# q2 subbookkeeper

# read files
f = open("bookin.txt", "r")
w = open("bookout.txt", "w")

books = []
n = int(f.readline())
for char in f.readline():
    books.append(char)

print(n, books)


# main program
score = 0
for i in range(n):
    print(books[i])
    if books[i] == "?":
        if books[i + 1] == books[i - 1]:
            score += 2
        else:
            score += 1
    elif books[i] == books[i + 1]:
        score += 1

print(score)
w.write(str(score))

# full marks 9:21
