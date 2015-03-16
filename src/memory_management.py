
# [(start1, end1), (start2, end2), ...]
# memory size is 512K
mem_size = 512 * 1024
spare = [(0, mem_size)]
used = list()

def malloc(length):
    if len(spare) == 0:
        print 'memory used up. abort. '
        return

    # sort spare spaces according to size
    spare.sort(key = lambda tup: abs(tup[0] - tup[1]))
    # find the smallest spare block that is larger than length
    flag = -1
    for i in range(len(spare)):
        if abs(spare[i][0] - spare[i][1]) >= length:
            flag = i
            break

    if flag == -1:
        print 'too large to alloc. abort. '
        return

    block = spare.pop(flag)
    used.append((block[0], block[0] + length))
    if abs(block[0] - block[1]) != length:
        spare.append((block[0] + length, block[1])

def mfree(addr):
    # to do
