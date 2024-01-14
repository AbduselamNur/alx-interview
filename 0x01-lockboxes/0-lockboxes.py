#!/usr/bin/python3
"""
Lockboxes
"""
from collections import deque


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened.
    """
    total_boxes = len(boxes)
    unlocked = [False] * total_boxes
    unlocked[0] = True
    keys = [key for key in boxes[0] if key < total_boxes]

    while keys:
        new_keys = []
        for key in keys:
            if not unlocked[key]:
                unlocked[key] = True
                new_keys += [new_key for new_key in boxes[key]
                             if new_key < total_boxes]
        keys = new_keys

    return all(unlocked)
