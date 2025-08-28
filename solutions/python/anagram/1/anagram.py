def find_anagrams(word, candidates):
    anagrams = []
    check = []
    for cand in candidates:
        capInsens, word = cand.lower(), word.lower()
        for i in list(capInsens):
            if word != capInsens and i in word  and capInsens.count(i) == word.count(i):
                check.append(True)
            else:
                check.append(False)
        if all(check):
            anagrams.append(cand)
        check.clear()
    return anagrams
    