
# [(start1, end1), (start2, end2), ...]
# memory size is 512K
mem_size = 512
spare = [[0, mem_size]]
used = list()

def malloc(length):
    # debug
    print 'alloc: ', length

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
    used.append([block[0], block[0] + length])
    if abs(block[0] - block[1]) != length:
        spare.append([block[0] + length, block[1]])

def mfree(addr):
    # debug
    print 'free: ', addr

    flag = -1
    for i in range(len(used)):
        if used[i][0] == addr:
            flag = i
            break

    if flag == -1:
        print 'the block is not used. fail to free. '
        return

    block = used.pop(flag)
    front = -1
    back = -1
    for idx, tup in enumerate(spare):
        if (tup[1] == block[0]):
            block[0] = tup[0]
            front = idx

        if (tup[0] == block[1]):
            block[1] = tup[1]
            back = idx
    if front >= 0:
        spare.pop(front)
    if back >= 0:
        spare.pop(back)
    spare.append(block)

def mem_stat():
    print 'used: ', used
    print 'free: ', spare, '\n'

# TEST CASES
malloc(128)
malloc(128)
malloc(128)
mem_stat()
mfree(128)
mem_stat()
mfree(256)
mem_stat()
malloc(64)
malloc(64)
mem_stat()
mfree(127)
mfree(128)
mem_stat()
malloc(128)
mem_stat()
malloc(32)
mem_stat()
