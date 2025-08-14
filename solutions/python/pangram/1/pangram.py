from string import ascii_lowercase


def is_pangram(sentence):
    check = (ch in sentence.lower() for ch in ascii_lowercase)
    return all(check)



