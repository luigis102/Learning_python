def commands(binary_str):
    result = []
    actions = {
        -1: "wink",
        -2: "double blink",
        -3: "close your eyes",
        -4: "jump"     
    }
    
    for i in range(-1,-len(binary_str)-1,-1):
        if binary_str[i] == "1":
            if i >= -4:
                result.append(actions[i])
            else:
                result = result[::-1]
    return result
