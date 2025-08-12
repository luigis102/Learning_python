def response(hey_bob):
    b = hey_bob.strip()
    if b == "":
        return "Fine. Be that way!"
    elif b.endswith("?") and b.isupper():
        return "Calm down, I know what I'm doing!"
    elif b.isupper():
        return "Whoa, chill out!"
    elif b.endswith("?"):
        return "Sure."
    else:
        return "Whatever."