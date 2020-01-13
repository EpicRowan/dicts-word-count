# put your code here.

def count_da_words(file_name):
    """ """

    the_test =open(file_name)

    word_counts = {}
    #big_string = ""

    # idea 1:
    # count the number of lines in file
    # add to dictionary theough the length of the file.

    # idea 2:
    # make file a large string
    # count using dictionary

    for line in the_test:
        line = line.rstrip()
        line = line.split(' ') # makes line a list
        # big_string += line

        for word in line:
            word_counts[word] = word_counts.get(word, 0) + 1


    for word, number in word_counts.items():
        print(f'{word} {number}')
    # return word_counts


# print(count_da_words("test.txt"))
count_da_words("twain.txt")