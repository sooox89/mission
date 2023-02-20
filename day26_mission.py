## 함수 선언 부분 ##

def binary_search(array, find_data):
    start = 0
    end = len(array) - 1

    while (start <= end):
        mid = (start + end) // 2
        if find_data == array[mid]:
            return array[mid]
        elif find_data > array[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


## 전역 변수 선언 부분 ##
product_sold = ['코카콜라', '츄파춥스', '도시락', '삼각김밥', '레쓰비캔커피', '츄파춥스', '도시락', '츄파춥스',
                '레쓰비캔커피', '코카콜라', '코카콜라', '도시락', '코카콜라', '삼각김밥', '삼각김밥', '바나나맛 우유', '삼각김밥', '츄파춥스', '바나나맛 우유', '코카콜라']
product_type = []

## 메인 코드 부분 ##
print(f'#오늘 판매된 전체 물건(중복O, 정렬X) --> {product_sold}')
product_sold.sort()
print(f'#오늘 판매된 전체 물건(중복O, 정렬O) --> {product_sold}')
product_type = list(set(product_sold))
print(f'#오늘 판매된 물품 종류(중복X) --> {product_type}')

count_list = []
for product in product_type:
    count = 0
    position = 0
    while position != -1:
        position = binary_search(product_sold, product)
        if position != -1:
            count += 1
            del(product_sold[position])
    count_list.append((product, count))
print()
print(f'결산 결과 --> {count_list}')
