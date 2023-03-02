song = open("song.txt")
word_dict = {}

for line in song:
    words = line.rstrip()
    words = words.split()
    for word in words:
        word = word.rstrip(",")
        if word.lower() in word_dict:
            word_dict[word.lower()] += 1
        else:
            word_dict[word.lower()] = 1

for el in word_dict:
    if word_dict[el] == 1:
        print(el)

song.close()
