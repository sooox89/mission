class Node2():
    def __init__(self):
        self.plink = None
        self.data = None
        self.nlink = None

def print_nodes(start):
    current = start
    if current.nlink == None:
        return
    print("정방향 -- >", end = ' ')
    print(current.data, end = ' ')
    while current.nlink != None:
        current = current.nlink
        print(current.data, end = ' ')
    print()
    print("역방향 -- >", end = ' ')
    print(current.data, end = ' ')
    while current.plink != None:
        current = current.plink
        print(current.data, end = ' ')


memory = []
head, current, pre = None, None, None
data_array = ["파이리", "꼬부기", "어니부기", "거북왕", "삐"]

if __name__ == "__main__":

    node = Node2()
    node.data = data_array[0]
    head = node
    memory.append(node)

    for data in data_array[1:]:
        pre = node
        node = Node2()
        node.data = data
        pre.nlink = node
        node.plink = pre
        memory.append(node)

    print_nodes(head)