with open('Words.txt', 'r') as inf:
    for line in inf:
        if line.strip():
            print(line)
with open('Words.txt', 'r') as inf, open('Polish_words.txt', 'w') as out:
    for line in inf:
        if line.strip():
            out.write(line)