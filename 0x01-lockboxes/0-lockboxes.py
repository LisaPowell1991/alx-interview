#!/usr/bin/python3

""" A module that contains a function, canUnlockAll """


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): A list containing lists representing locked boxes.
    Each box may contain keys to other boxes.

    Returns
    bool: True if all boxes can be opened, else return False.
    """

    # Get total, create empty set and add first box(alrady unlocked)
    num_boxes = len(boxes)
    unlocked_boxes = set()
    unlocked_boxes.add(0)

    # Queue to keep track of boxes needed to be explored
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        # Check all keys in current box
        for key in boxes[current_box]:
            if key < num_boxes and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                queue.append(key)

    # if all boxes have been unlocked, return true
    return len(unlocked_boxes) == num_boxes
