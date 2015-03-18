f_handle = open('memory', 'r')

memory = list()
raw_line = f_handle.readline()
while(raw_line):
    raw_line = (raw_line[9:]).strip()
    memory.extend(raw_line.split(' '))
    raw_line = f_handle.readline()

# VA = 0x6c74
PD_BASE = 0x220


def va2pa(VA):
    print 'Virtual Address ', hex(VA)

    m1 = 0b0111110000000000
    m2 = 0b0000001111100000
    m3 = 0b0000000000011111
    p1 = (m1 & VA) >> 10
    p2 = (m2 & VA) >> 5
    offset = m3 & VA
    ## debug
    # print bin(p1), ' ', bin(p2), ' ', bin(offset)

    pde_index = PD_BASE + p1
    valid = (int(memory[pde_index], 16) & 0b10000000) >> 7
    pfn = int(memory[pde_index], 16) & 0b01111111
    print '\tpde index: ', hex(pde_index), ' pde content: (valid ', valid, ', pfn ', hex(pfn), ') '
    if valid == 0:
        print '\t\t--> Fault (page directory entry not valid)'
        return

    pte_index = (pfn << 5) + p2
    valid = (int(memory[pte_index], 16) & 0b10000000) >> 7
    pfn = int(memory[pte_index], 16) & 0b01111111
    print '\t\tpte index: ', hex(pte_index), ' pte content: (valid ', valid, ', pfn ', hex(pfn), ') '
    if valid == 0:
        print '\t\t\t--> Fault (page table entry not valid)'
        return

    pa = (pfn << 5) + offset
    print '\t\t\t--> Translates to Physical Address ', hex(pa), ' --> Value: ', int(memory[pa], 16)

va_list = [0x6c74, 0x6b22, 0x03df, 0x69dc,
            0x317a, 0x4546, 0x2c03, 0x7fd7, 0x390e, 0x748b]

for va in va_list:
    va2pa(va)
