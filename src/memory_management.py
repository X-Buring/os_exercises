
# [(start1, end1), (start2, end2), ...]
# memory size is 512K
mem_size = 512
spare = [[0, mem_size]]
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
    used.append([block[0], block[0] + length])
    if abs(block[0] - block[1]) != length:
        spare.append([block[0] + length, block[1]])

def mfree(addr):
    flag = -1
    for i in range(len(used)):
        if used[i][0] == addr:
            flag = i
            break

    if flag == -1:
        print 'the block is not used. fail to free. '
        return

    block = used.pop(flag)
    for idx, tup in enumerate(spare):
        if (tup[1] == block[0]):
            spare.pop(idx)
            block[0] = tup[0]
        if (tup[0] == block[1]):
            spare.pop(idx)
            block[1] = tup[1]

    spare.append(block)

def mem_stat():
    print 'used: ', used
    print 'free: ', spare


malloc(128)
# used: [0, 128]
mem_stat()
malloc(64)
# used: [0, 128], [128, 192]
mem_stat()
malloc(256)
# used: [0, 128], [128, 192], [192, 448]
mem_stat()
mfree(128)
# used: [0, 128], [192, 448]
mem_stat()
malloc(512)
# err
mem_stat()
mfree(192)
mem_stat()
malloc(32)
mem_stat()
malloc(32)
mem_stat()
malloc(320)
mem_stat()
malloc(128)
