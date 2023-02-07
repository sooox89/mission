def is_queue_full():
    global front, rear, SIZE, queue
    if (rear+1)%SIZE == front:
        print("큐가 꽉 찼습니다")
        return True
    return False

def is_queue_empty():
    global front, rear, SIZE, queue
    if front == rear:
        print("큐가 비었습니다")
        return True
    return False

def en_queue(data):
    global front, rear, SIZE, queue
    if (is_queue_full()):
        return
    rear=(rear+1)%SIZE
    queue[rear] = data


def de_queue():
    global front, rear, SIZE, queue
    if(is_queue_empty()):
        return
    front=(front+1)%SIZE
    data=queue[front]
    queue[front]=None
    return data

def peek():
    global front, rear, SIZE, queue
    if(is_queue_empty()):
        print("큐가 비어있습니다")
        return None
    return (queue[(front+1)%SIZE])

def estimate_time():
    global front, rear, SIZE, queue
    time_sum = 0
    for i in range((front+1)%SIZE, (rear+1)%SIZE):
        time_sum += queue[i][1]
    return time_sum


# 전역변수 선언
SIZE = 6
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__=="__main__":
    wait_call= [['사용',10],['고장',5],['환불',3],['환불',3],['고장',5]]

    for call in wait_call:
        print("귀하의 대기 예상 시간은", estimate_time(), "분입니다.")
        print("현재 대기 콜-->", queue)
        en_queue(call)
        print()

    print("최종 대기 콜--> ", queue)
    print("프로그램 종료!")
