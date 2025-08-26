def commands(binary_str):
    result = []
    actions = {
         4: "wink",
         3: "double blink",
         2: "close your eyes",
         1: "jump"     
    }

    # itearate through the str in reverse order from the last to the first chr
    for i in range(len(binary_str)-1,-1,-1):
        if binary_str[i] == "1":
            if i >= 1:
                result.append(actions[i])
            else:
                result = result[::-1]
    return result
