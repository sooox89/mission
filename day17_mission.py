def is_queue_full():
    global front, rear, SIZE, queue
    if rear != SIZE-1:
        return False
    elif rear == SIZE-1 and front == -1:
        print("큐가 꽉 찬 상태다 !")
        return True
    else:
        for i in range(front+1,SIZE):
            queue[i-1]=queue[i]
            queue[i]=None
        front-=1
        rear-=1
        return False

def is_queue_empty():
    global front, rear, SIZE, queue
    if rear==-1 and front==-1:
        return True
    return False

def en_queue(data):
    global front, rear, SIZE, queue
    if (is_queue_full()):
        return
    else:
        rear+=1
        queue[rear] = data

def de_queue():
    global front, rear, SIZE, queue
    if(is_queue_empty()):
        return
    else:
        front+=1
        data=queue[front]
        queue[front]=None
        return data
        print(data)

        for i in range(front+1,rear+1):
            queue[i-1]=queue[i]
            queue[i]=None
        front-=1
        rear-=1

def peek():
    global front, rear, SIZE, queue
    if(is_queue_empty()):
        print("큐가 비어있습니다")
        return None
    else:
        return queue[front+1]


# 전역변수 선언
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__=="__main__":
    en_queue("태양")
    en_queue("지디")
    en_queue("대성")
    en_queue("탑")
    en_queue("수경")
    print("대기 줄 상태 : ",queue)

    for i in range(rear+1):
        print(de_queue(),"님 식당에 들어감")
        print("대기 줄 상태 : ",queue)

    print("대기 줄 없음!")
