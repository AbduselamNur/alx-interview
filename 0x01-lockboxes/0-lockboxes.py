#!/usr/bin/python3
from collections import deque
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    queue = deque([0])

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
