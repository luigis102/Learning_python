def find_anagrams(word, candidates):
    anagrams = []
    for cand in candidates:
        check_cand, check_word = cand.lower(), word.lower()
        n = 0
        check = True
        while n <= len(word)-1 and len(word) == len(cand):
            if sorted(check_cand)[n] != sorted(check_word)[n] or word.lower() == cand.lower():
                check = False
                break
            n += 1
        if check and len(word) == len(cand):
            anagrams.append(cand)
    return anagrams
    