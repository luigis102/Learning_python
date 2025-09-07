def find(search_list, value):
    left = 0
    right = len(search_list) - 1
    while right >= left:
        middle_val = left + ((right - left) // 2)
        if search_list[middle_val] < value:
            left = middle_val + 1
        elif search_list[middle_val] > value:
            right = middle_val - 1
        else:
            for i in range(left,middle_val+1):
                if search_list[i] == value:
                    return i
    raise ValueError("value not in array")
