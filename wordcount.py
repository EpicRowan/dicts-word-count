# put your code here.

def count_da_words(file_name):
    """ """

    the_test =open(file_name)

    word_counts = {}

    for line in the_test:
        line = line.rstrip()
        # line = line.split('')

    for word in line:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


print(count_da_words("test.txt"))