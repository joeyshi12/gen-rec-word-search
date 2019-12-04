import enchant


# EFFECTS: returns true if word is in the Canadian english dictionary; else, returns false
def is_valid_word(word: str) -> bool:
    dictionary = enchant.Dict("en_CAN")
    return dictionary.check(word)


# EFFECTS: returns a list of all unique next possible strings
def next_words(word: str, chars: list) -> list:
    if not chars:
        return []
    else:
        if chars[0] in chars[1::]:
            return next_words(word, chars[1::])
        else:
            return [word + chars[0]] + next_words(word, chars[1::])


# REQUIRES: chars is a list of characters
# EFFECTS: returns a list of all possible words from chars with length n
def search_words(chars: list, n: int) -> list:
    def fn_for_word(word: str) -> list:
        if len(word) == n:
            if is_valid_word(word):
                return [word]
            else:
                return []
        else:
            return fn_for_words(next_words(word, chars))

    def fn_for_words(words: list) -> list:
        if not words:
            return []
        else:
            return fn_for_word(words[0]) + fn_for_words(words[1::])

    return fn_for_word('')