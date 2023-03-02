spam = open("SMSSpamCollection.txt")

spam_count = 0
ham_count = 0
spam_word_count = 0
ham_word_count = 0
spam_exclamation = 0

for line in spam:
    line = line.rstrip()
    words = line.split()
    if words[0] == "spam":
        spam_count += 1
        spam_word_count += len(words) - 1
        if words[len(words) - 1].endswith("!"):
            spam_exclamation += 1
    else:
        ham_count += 1
        ham_word_count += len(words) - 1

print(f"Spam message count:{spam_count}, avg. word count:{spam_word_count/spam_count}")
print(f"Spam messages ending with !: {spam_exclamation}")
print(f"Ham message count:{ham_count}, avg. word count:{ham_word_count/ham_count}")

spam.close()
