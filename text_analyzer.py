import locale
import string
from sys import argv

locale.setlocale(locale.LC_ALL, "en_US")

def clear_punctuation(word,clear_words):
    """Take the string and list then removes the punctuations before and after it and returns it in a list"""
    while word[-1] in string.punctuation: #If there is a punctuation mark at the end,clear it until there is no punctuation mark.
        word = word[:-1]
    while word[0] in string.punctuation: #If there is a punctuation mark at the beginning, clear it until there is no punctuation mark.
        word = word[1:]
    clear_words.append(word)
    return clear_words

def write_title():
    """"Take the input.txt and write the name part in the output with the statistics about"""
    with open(argv[2],"w") as f_out:
        f_out.write("Statistics about {:7}:\n".format(argv[1]))

def count_words_sentences_and_calculate_ratio():
    """Take the input.txt and count number of words and sentences and then calculate the average number of words per sentence. Finally, write these information to output.txt"""
    with open(argv[1],"r") as f_in:
        text = f_in.read() # Pull the text from the input
    clear_words = [] #we set an empty list to take all words without punctuations
    for word in text.split():  # we separate all words from spaces and punctuation marks and put them into the clear_words list
        clear_punctuation(word,clear_words)
    word_count = len(clear_words)  #Find how many words used in text
    sentence_counter = 0 # we set sentence counter to 0 and start to count
    i = 0
    while i < len(text): #if we see . ! ? or ... in our text we will increment the sentence_counter by one to find out how many sentences there are because these finish the sentences.
        if text[i:i + 3] == "...": #three dot is a special case so firstly we look is it three dot or not if it is three dot we jump that and we increment the sentence counter
            i += 3
            sentence_counter += 1
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            sentence_counter += 1
        i += 1
    average_number_of_words_per_sentence = word_count/sentence_counter #find average number of words per sentence simple formula
    with open(argv[2],"a") as f_out:
        f_out.write("{:24}: {}\n".format("#Words",word_count))
        f_out.write("{:24}: {}\n".format("#Sentences",sentence_counter))
        f_out.write("{:24}: {:.2f}\n".format("#Words/#Sentences",average_number_of_words_per_sentence))

def find_characters():
    """Take the input.txt and count characters with and without spaces and punctuations, finally, write these information to output.txt"""
    with open(argv[1],"r") as f_in:
        text = f_in.read() # pull the text from the input.txt
    character_count = len(text) #this counting counts all characters(including punctuations and white-spaces)
    clear_words = [] #we set an empty list to take all words without spaces and punctuations
    for word in text.split():  # we separate all words from spaces and punctuation marks and put them into the clear_words list
        clear_punctuation(word,clear_words)
    character_countJustWords = 0 # we set a character_count(Just Words Edition) value to 0
    for word in clear_words: # We obtain the total value by adding the number of characters of each word
        character_countJustWords += len(word)
    with open(argv[2],"a") as f_out:
        f_out.write("{:24}: {}\n".format("#Characters",character_count))
        f_out.write("{:24}: {}\n".format("#Characters (Just Words)",character_countJustWords))

def find_longest_shortest_word_and_frequency():
    """Take the input.txt and find frequencies of all words and find the longest word(or words) and the shortest word(or words). Tgen, write these information to output.txt"""
    with open(argv[1],"r") as f_in:
        text = f_in.read()
    clear_words = [] #we set an empty list to take all words without spaces and punctuations
    for word in text.split(): # we separate all words from spaces and punctuation marks and put them into the clear_words list.
        clear_punctuation(word.lower(),clear_words) # we take word with lowercase because we don't want to python thinks "Gorkem" and "gorkem" are different words(this gives damage our find shortest longest and calculate frequency algorithm)
    frequency_dictionary = {} #we set an empty dictionary to get word and frequency in a matched form
    for word in clear_words:
        """Calculating frequency and put the dictionary with the word"""
        frequency = clear_words.count(word) / len(clear_words)
        frequency_dictionary[word] = frequency
    sorted_for_values_dictionary = dict(sorted(frequency_dictionary.items(), key=lambda item: (-item[1],item[0]))) # we sort the values from largest to smallest, and if the values are the same, we sort the keys according to the alphabet.
    """Find shortest algorithm"""
    length = len(clear_words[0])
    index = 0
    shortest_list = []
    while index < len(clear_words):
        if len(clear_words[index]) < length: # if new word's length shorter than the shortest word , clear the list and append this new word and arrange length to new word's length
            length = len(clear_words[index])
            shortest_list.clear()
            shortest_list.append(clear_words[index])
        elif len(clear_words[index]) == length: # if new word_s length equal to the shortest word, only append this new word and continue
            shortest_list.append(clear_words[index])
        index += 1
    shortest_set = set(shortest_list) # a code to ensure that there is one of each element
    shortest_list = list(shortest_set)
    if len(shortest_list) == 1: # if there is one shortest word write to output
        with open(argv[2],"a") as f_out:
            f_out.write("{:24}: {:24} ({:.4f})\n".format("The Shortest Word",shortest_list[0],sorted_for_values_dictionary[shortest_list[0]]))
    elif len(shortest_list) > 1: # if there is more than one shortest word write two output but sorted
        with open(argv[2],"a") as f_out:
            f_out.write("{:24}:\n".format("The Shortest Words"))
            shortest_dictionary = {}
            for word in shortest_list:
                shortest_dictionary[word] = sorted_for_values_dictionary[word]
            sorted_shortest_dictionary = dict(sorted(shortest_dictionary.items(),key=lambda item: (-item[1],item[0]))) # we sort the values from largest to smallest, and if the values are the same, we sort the keys according to the alphabet.
            for (key,value) in sorted_shortest_dictionary.items():
                f_out.write("{:24} ({:.4f})\n".format(key,value))
    """Find Longest Algorithm"""
    length2 = 0
    index2 = 0
    longest_list = []
    while index2 < len(clear_words):
        if len(clear_words[index2]) > length2:  # if new word's length longer than the longest word , clear the list and append this new word and arrange length to new word's length
            length2 = len(clear_words[index2])
            longest_list.clear()
            longest_list.append(clear_words[index2])
        elif len(clear_words[index2]) == length2: # if new word_s length equal to the longest word, only append this new word and continue
            longest_list.append(clear_words[index2])
        index2 += 1
    longest_set = set(longest_list) # a code to ensure that there is one of each element
    longest_list = list(longest_set)
    if len(longest_list) == 1: # if there is one longest word write to output
        with open(argv[2],"a") as f_out:
            f_out.write("{:24}: {:24} ({:.4f})\n".format("The Longest Word",longest_list[0],sorted_for_values_dictionary[longest_list[0]]))
    elif len(longest_list) > 1: # if there is more than one longest word write to output but sorted
        with open(argv[2],"a") as f_out:
            f_out.write("{:24}:\n".format("The Longest Words"))
            longest_dictionary = {}
            for word in longest_list:
                longest_dictionary[word] = sorted_for_values_dictionary[word]
            sorted_longest_dictionary = dict(sorted(longest_dictionary.items(),key=lambda item: (-item[1],item[0]))) # we sort the values from largest to smallest, and if the values are the same, we sort the keys according to the alphabet.
            for (key,value) in sorted_longest_dictionary.items():
                f_out.write("{:24} ({:.4f})\n".format(key,value))
    """write the frequencies to output"""
    with open(argv[2],"a") as f_out:
        f_out.write("{:24}:\n".format("Words and Frequencies"))
        for (key,value) in sorted_for_values_dictionary.items():
            if key == list(sorted_for_values_dictionary.keys())[-1]:
                f_out.write("{:24}: {:.4f}".format(key,value))
            else:
                f_out.write("{:24}: {:.4f}\n".format(key,value))

def main():
    write_title()
    count_words_sentences_and_calculate_ratio()
    find_characters()
    find_longest_shortest_word_and_frequency()

if __name__ == "__main__":
    main()