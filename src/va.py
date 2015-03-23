pde_mask = 0xffc00000
pde_shift = 22
pte_mask = 0x003ff000
pte_shift = 12
page_mask = 0xfffff000
page_shift = 8

def read_data():
    f_handle = open('data', 'r')
    va_pa = list()
    raw_line = f_handle.readline()
    while(raw_line):
        l = raw_line.split(', ')
        l[0] = l[0][3:].strip()
        l[1] = l[1][3:].strip()
        va_pa.append(l)
        raw_line = f_handle.readline()
    return va_pa

def convert(pa_va):
    for ele in pa_va:
        va = int(ele[0], 16)
        pa = int(ele[1], 16)

        pde_idx = (va & pde_mask) >> pde_shift
        pde_ctx = ((pde_idx - 0x300 + 1) << 12) | 0x003
        pte_idx = (va & pte_mask) >> pte_shift
        pte_ctx = (pa & page_mask) | 0x003

        print 'va: %s, pa: %s, pde_idx, %s, pde_ctx, %s, pte_idx: %s, pte_ctx: %s' %(hex(va), hex(pa), hex(pde_idx), hex(pde_ctx), hex(pte_idx), hex(pte_ctx))

def main():
    convert(read_data())

if __name__ == '__main__':
    main()
