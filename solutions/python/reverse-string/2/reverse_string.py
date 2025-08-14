def reverse(text):
    text = list(text)
    new = [text[i] for i in range(-1,-len(text)-1,-1)]
    return "".join(new)
