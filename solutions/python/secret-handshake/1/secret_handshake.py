def commands(binary_str):
    binary_str = binary_str[::-1]
    trans = []
    for i in range(0,len(binary_str)):
        if binary_str[i] != "0":
            if i == 0:
                trans.append("wink")
            elif i == 1:
                trans.append("double blink")
            elif i == 2:
                trans.append("close your eyes")
            elif i == 3:
                trans.append("jump")
            else:
                trans = trans[::-1]
    return trans
