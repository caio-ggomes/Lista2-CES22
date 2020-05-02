#----------------------------TOOLS----------------------------

def is_between(a, b, c):
    if a>=b and a<=c:
        return True
    return False


def is_low_case(character):
    if is_between(ord(character), 97, 122):
        return True
    return False


def is_high_case(character):
    if is_between(ord(character), 65, 90):
        return True
    return False


def is_char(character):
    if is_low_case(character) or is_high_case(character):
        return True
    return False

#---------------------------FUNCTIONS-------------------------

def cleanword(word):
    new_word = ""
    for character in word:
        if is_char(character):
            new_word = new_word + character
    return new_word


def has_dashdash(word):
    for i in range(len(word)-1):
        if word[i] == '-' and word[i+1] == '-':
            return True
    return False


def extract_words(phrase):
    first_letter = -1
    last_letter = -1
    words = []
    aux = ""
    for i in range(len(phrase)):
        if first_letter == -1 and is_char(phrase[i]):
            first_letter = i
            last_letter = i
        if is_char(phrase[i]):
            last_letter = i
        elif not is_char(phrase[i]) and first_letter != -1:
            for j in range(first_letter, last_letter + 1):
                aux = aux + phrase[j]
            aux = aux.lower()
            words.append(aux)
            aux = ""
            first_letter = -1
    if is_char(phrase[len(phrase)-1]):
        for j in range(first_letter, last_letter + 1):
            aux = aux + phrase[j]
        aux = aux.lower()
        words.append(aux)
        aux = ""
        first_letter = -1
    return words


def wordcount(word, word_list):
    count = 0
    for element in word_list:
        if element == word:
            count += 1
    return count


def wordset(word_list):
    word_set = []
    for word in word_list:
        if word not in word_set:
            word_set.append(word)
    word_set = sorted(word_set)
    return word_set


def longestword(word_list):
    max = 0
    for word in word_list:
        if len(word) > max:
            max = len(word)
    return max