memory = list()
disk = list()

# read two files respectively
f = open('page_data', 'r')

raw_line = f.readline()
while(raw_line):
    raw_line = (raw_line[9:]).strip()
    memory.extend(raw_line.split(' '))
    raw_line = f.readline()

f = open('disk_data', 'r')

raw_line = f.readline()
while(raw_line):
    raw_line = (raw_line[9:]).strip()
    disk.extend(raw_line.split(' '))
    raw_line = f.readline()

# print 'memory: ', len(memory)
# print 'disk: ', len(disk)

PD_BASE = 0xd80

def va2pa(VA):
    print 'Virtual Address ', hex(VA)

    m1 = 0b0111110000000000
    m2 = 0b0000001111100000
    m3 = 0b0000000000011111
    p1 = (m1 & VA) >> 10
    p2 = (m2 & VA) >> 5
    offset = m3 & VA

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
        # print '\t\t\t--> Fault (page table entry not valid)'
        addr = (pfn << 5) + offset
        print '\t\t\t--> To Disk Sector Address ', addr, ' --> Value: ', disk[addr]
        return

    pa = (pfn << 5) + offset
    print '\t\t\t--> Translates to Physical Address ', hex(pa), ' --> Value: ', memory[pa]

va_list = [0x6653, 0x1c13, 0x6890, 0x0af6, 0x1e6f]

for va in va_list:
    va2pa(va)
