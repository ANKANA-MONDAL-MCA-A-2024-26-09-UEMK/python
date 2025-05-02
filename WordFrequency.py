# Program to Count Word Frequency in a Sentence

from collections import Counter

def count_word_frequency(sentence):
    words = sentence.split()
    word_count = Counter(words)
    return word_count

# Example Usage
sentence = "this is a test sentence and this is a test"
results = count_word_frequency(sentence)
print(results)
