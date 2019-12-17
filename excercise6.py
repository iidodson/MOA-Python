def break_words(stuff):
    # This function will break up break_words
    words = stuff.split(' ')
    return words

print(break_words("Indya Imani Dodson"))

def sort_words(words):
    # This function will sort sort_words
    return sorted(words)

def print_first_word(words):
    # Prints the first word after popping it off
    word = words.pop(0)
    print(word)

def sort_sentences(sentence):
    # This takes a fill sentence and returned the sortred sort_words
    words = break_words(sentence)
    return sort_words(words)

#def print_first_and_last(sentence):
