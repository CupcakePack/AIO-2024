# q5 tennis robot ii

# read files
f = open("tennisin.txt", "r")
w = open("tennisout.txt", "w")

n, m = map(int, f.readline().split())
bins = list(map(int, f.readline().split()))
instructions_from = []
instructions_to = []
for i in range(m):
    fr, to = map(int, f.readline().split())
    instructions_from.append(fr)
    instructions_to.append(to)

print(n, m, bins, instructions_from, instructions_to)


# main program
def checksame(list1, list2):
    if list1 == list2:
        return True
    return False


count = 0

while True:
    after = bins[:]
    for i in range(m):
        after[instructions_from[i] - 1] -= 1
        # if a robot takes a ball from an empty bin
        if after[instructions_from[i] - 1] < 0:
            print(count)
            w.write(str(count))
            exit()
        after[instructions_to[i] - 1] += 1
        count += 1

    # print(bins, after)
    if checksame(bins, after):
        print("FOREVER")
        w.write("FOREVER")
        exit()
    else:
        bins = after
        after = bins[:]

# all correct, just too slow 0/100 10:38
# removed the print statements? now 25/100 subtask 1 correct 11:43
