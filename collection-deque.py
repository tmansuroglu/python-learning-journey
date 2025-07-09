# for fast pop and append
from collections import deque

queue = deque([1, 2, 3, 4, 5])

queue.appendleft(7)

print(queue)
