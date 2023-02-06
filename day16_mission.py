import random
import math

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def print_storages(start):
    current = start
    if current == None:
        return

    while current.link != head:
        current = current.link
        x,y = current.data[1:]
        print(current.data[0],'번 창고, 위치:', math.sqrt(x*x + y*y))
    print()

def make_storage_list(storage):
    global memory, head, current, pre

    node = Node()
    node.data = storage
    memory.append(node)

    if head == None:
        head = node
        node.link = head
        return
    node_x, node_y = node.data[1:]
    node_dis = math.sqrt(node_x*node_x + node_y*node_y)
    head_x, head_y = node.data[1:]
    head_dis = math.sqrt(head_x*head_x + head_y*head_y)

    if head_dis > node_dis :
        node.link = head
        last = head
        while last.link != head:
            last= last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        curr_x, curr_y = current.data[1:]
        curr_dis = math.sqrt(curr_x* curr_x + curr_y*curr_y)
        if curr_dis > node_dis:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head

memory =[]
head, current, pre = None, None, None

if __name__== "__main__":

    storage_Array =[]
    storage_num = 1
    for _ in range(10):
        storage = (storage_num, random.randint(1,100),random.randint(1,100))
        storage_Array.append(storage)
        storage_num +=1

    for storage in storage_Array:
        make_storage_list(storage)

    print_storages(head)