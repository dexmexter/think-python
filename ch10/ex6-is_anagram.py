def is_anagram(word1, word2):
    if len(word1) == len(word2):
        for i in list(word1):
            if i not in list(word2):
                return False
        return True
    return False

print(is_anagram("that", "tath"))

print(is_anagram("that", "tatg"))

print(is_anagram("aa", "aaa"))