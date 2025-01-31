sentence = "You cannot end a sentence with because is a conjunction"
word = "because"
index = -1
sentence_length = len(sentence)
word_length = len(word)

for i in range(sentence_length - word_length + 1):
    match = True
    for j in range(word_length):
        if sentence[i + j] != word[j]:
            match = False
            break
    if match:
        index = i
        break

print("First occurrence:", index)
