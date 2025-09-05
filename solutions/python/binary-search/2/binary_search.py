def find(search_list, value):
    split = 1
    backup = search_list
    while split > 0 and len(search_list) > 0:
        split = len(search_list) // 2
        middleVal = search_list[split]
        if middleVal == value:
            return backup.index(middleVal)
        if middleVal > value:
            search_list = search_list[:search_list.index(middleVal)]
        else:
            search_list = search_list[search_list.index(middleVal)+1:]
    raise ValueError("value not in array")

