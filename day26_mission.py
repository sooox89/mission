import random

#클래스와 함수 선언 부분#
def seq_search(array, f_data):
    global  count
    pos = -1
    for i in range(len(array)):
        count += 1
        if array[i] == find_data:
            pos= i
            break
    return pos

def bin_search(array,f_data):
    global count
    start = 0
    end = len(array) -1

    while(start <= end):
        count +=1
        mid = (start + end) //2

        if f_data == array[mid]:
            return mid
        elif f_data > array[mid]:
            start = mid +1
        else:
            end = mid -1

# 전역 변수 선언 부분 #

data_array ,sorted_array = [] ,[]
find_data = 7878
count = 0

# 메인 코드 부분 #
data_array = [random.randint(0,999999) for _ in range(1000000)]
data_array.insert(random.randint(0,1000000), find_data)
sorted_array = sorted(data_array)

print(f'#비정렬 배열(100만개) --> {data_array[0:5]} ~~~~ {data_array[-5:len(data_array)]}')
print(f'#정렬 배열(100만개) --> {sorted_array[0:5]} ~~~~ {sorted_array[-5:len(sorted_array)]}')

count = 0
pos = seq_search(data_array,find_data)
if pos != -1:
    print(f'순차 검색(비정렬 데이터) --> {count}회 ')

count = 0
pos = bin_search(sorted_array,find_data)
if pos != -1:
    print(f'이진 검색(정렬 데이터) --> {count}회')