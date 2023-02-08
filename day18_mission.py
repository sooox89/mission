## 클래스 및 함수 선언 부분 ##
class Graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g) :
	print('		 ', end = ' ')
	for v in range(g.SIZE) :
		print("%9s" % name_array[v][0], end =' ')
	print()
	for row in range(g.SIZE) :
		print("%9s" % name_array[row][0], end =' ')
		for col in range(g.SIZE) :
			print("%9d" % g.graph[row][col], end = ' ')
		print()
	print()

## 전역 변수 선언 부분 ##
G1 = None
name_array = [["GS25", 30], ["CU", 60], ["Seven11", 10], ["Ministop", 90], ["Emart24", 40]]
GS25,CU,Seven11,Ministop,Emart24 = 0, 1, 2, 3, 4


## 메인 코드 부분 ##
gSize = 5
G1 = Graph(gSize)
G1.graph[GS25][CU]=1; G1.graph[GS25][Seven11]=1
G1.graph[CU][GS25]=1; G1.graph[CU][Seven11]=1; G1.graph[CU][Ministop]=1
G1.graph[Seven11][GS25]=1; G1.graph[Seven11][CU]=1; G1.graph[Seven11][Ministop]=1
G1.graph[Ministop][CU]=1; G1.graph[Ministop][Seven11]=1; G1.graph[Ministop][Emart24]=1
G1.graph[Emart24][Ministop]=1
print('## 편의점 그래프 ##')
printGraph(G1)




stack = []
visited_array = []	# 방문한 노드

current = 0	# 시작 정점
max_store = current
max_honeychip = name_array[current][1]
stack.append(current)
visited_array.append(current)

while (len(stack) != 0) :
	next = None
	for vertex in range(gSize) :
		if G1.graph[current][vertex] != 0 :
			if vertex in visited_array :	# 방문한 적이 있는 정점이면 탈락
				pass
			else :			# 방문한 적이 없으면 다음 정점으로 지정
				next = vertex
				break

	if next != None :				# 다음에 방문할 정점이 있는 경우
		current = next
		stack.append(current)
		visited_array.append(current)
		if name_array[current][1]> max_honeychip :
			max_honeychip =name_array[current][1]
			max_store =current
	else :					# 다음에 방문할 정점이 없는 경우
		current = stack.pop()

print("허니버터칩 최대 보유 편의점 : ", name_array[max_store][0], "/ 개수: ", name_array[max_store][1])