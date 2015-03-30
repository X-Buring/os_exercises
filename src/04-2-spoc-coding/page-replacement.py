# LRU simulation in python

class Page:
    index = int()
    mod = int()

    def __init__(self, index, mod):
        self.index = index
        self.mod = mod

MAX_LEN = 5
        
def visitPage(page_list, index):
    found = False
    for i in range(len(page_list)):
        if(page_list[i].index == index):
            found = True
            for i in range(len(page_list)):
                if page_list[i].index != index:
                    page_list[i].mod += 1
                else:
                    page_list[i].mod = 0
            break

    if not found:
        # get the index of the oldest page
        m = -1
        ind = -1
        for i in range(len(page_list)):
            if page_list[i].mod > m:
                m = page_list[i].mod
                ind = i

        if len(page_list) >= MAX_LEN:
            page_list.pop(ind)
        page_list.append(Page(index, 0))
        for i in range(len(page_list)):
            if page_list[i].index != index:
                page_list[i].mod += 1
        
def showList(page_list):
    for page in page_list:
        print 'index: %d; \t mod: %d ' %(page.index, page.mod)
    print '\n'

                
def test():
    page_list = list()
    for i in range(1, 6):
        visitPage(page_list, i)
        showList(page_list)

    visitPage(page_list, 3)
    showList(page_list)
    visitPage(page_list, 1)
    showList(page_list)
    visitPage(page_list, 6)
    showList(page_list)


if __name__ == '__main__':
    test()
