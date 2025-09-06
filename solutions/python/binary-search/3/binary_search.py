def find(search_list, value):
    split = 1
    backup = search_list
    left = 0
    right = len(search_list) - 1
    while right >= left and len(search_list) > 0:
        middleVal = search_list[left + ((right-left)//2)]
        if middleVal < value:
            left = search_list.index(middleVal) + 1
        elif middleVal > value:
            right = search_list.index(middleVal) -1
        else:
            return backup.index(middleVal)
    raise  ValueError("value not in array")

