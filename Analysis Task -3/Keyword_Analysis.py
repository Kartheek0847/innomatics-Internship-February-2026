query = "Buy mobile phone buy phone online"
query = query.lower()
query = query.replace(",", "").replace(".", "")

words = query.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
result = {}

for word, count in word_count.items():
    if count > 1:
        result[word] = count

print(result)
