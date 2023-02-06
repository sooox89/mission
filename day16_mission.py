import random

def is_stack_full():
    global size, stack, top
    if (top >= size-1):
        return True
    return False

def is_stack_empty():
    global size, stack, top
    if (top == -1):
        return True
    return False

def push(data):
    global size, stack, top
    if(is_stack_full()):
        return
    top +=1
    stack[top] = data

def pop():
    global size, stack, top
    if(is_stack_empty()):
        return None
    data = stack[top]
    stack[top] = None
    top -=1
    return data

def peek():
    global size, stack, top
    if(is_stack_empty()):
        return None
    return stack[top]

size = 10
stack = [None for _ in range(size)]
top = -1

if __name__== "__main__":
    where_arr = ["은행", "우체국", "편의점", "교직원 식당", "인하대학교"]
    random.shuffle(where_arr)

    print("어니부기 집에 가는 길 ", end = ' ')
    for where in where_arr:
        push(where)
        print(where, "-->", end = ' ')
    print("어니부기 집")

    print("파이리 집에 가는 길 ", end = ' ')
    while True:
        where = pop()
        if where == None:
            break
        print(where,"-->",end = ' ')
    print("파이리 집")