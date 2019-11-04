from collections import deque
graph = {
    1: [2, 3, 8],
    2: [1, 7, 9],
    3: [1, 4, 10],
    4: [3, 6],
    5: [6, 10],
    6: [4, 5],
    7: [2, 8, 9],
    8: [1, 10],
    9: [2, 6, 7],
    10: [3, 5, 8]
}

visited = set()
q = deque()
s = []
def bfs(a):
    if a in visited:
        return
    visited.add(a)
    s.append(a)
    for i in graph[a]:
        if not i in visited:
            q.append(i)
    while q:
        bfs(q.popleft())

start, find = map(int, input().split())
bfs(start)
print(s.count(find) > 0)
