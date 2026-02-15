def get_unique_words(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    unique_words = set(words)
    return unique_words
sentence_input = input("Enter sentence: ")
result = get_unique_words(sentence_input)
print("Unique words count:", len(result))
print("Unique words:", result)
