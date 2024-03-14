#!/usr/bin/python3
"""
A module for working with lockboxes.
"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked given that the first box is unlocked.

    Args: A list of lists containing the keys (indices) to other boxes.

    Returns: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    seen_boxes = {0}
    unseen_boxes = set(boxes[0]) - {0}

    while unseen_boxes:
        box_idx = unseen_boxes.pop()
        if not 0 <= box_idx < n:
            continue
        if box_idx not in seen_boxes:
            unseen_boxes.update(boxes[box_idx])
            seen_boxes.add(box_idx)

    return n == len(seen_boxes)
