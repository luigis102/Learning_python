def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")
    backup = search_list
    while True:
        middleVal = search_list[len(search_list) // 2]
        if middleVal == value:
            return backup.index(middleVal)
        if middleVal > value:
            search_list = search_list[:search_list.index(middleVal)]
        else:
            search_list = search_list[search_list.index(middleVal)+1:]

