def response(hey_bob):
    b = hey_bob.strip()
    if b == "":
        return "Fine. Be that way!"
    if b.isupper():
        if b.endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if b.endswith("?"):
        return "Sure."
    return "Whatever."