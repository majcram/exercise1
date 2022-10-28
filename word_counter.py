text = '''
The question is in a way meaningless, she knows, 
but one must ask. Love in such situations is 
rarely real. Sex is the engine, exalting and 
ruining people, sex and frustration. Love is 
what people believe is worth the path of 
devastation. - Wolf Border, Sarah Hall'''
    
def read_text(text):
    text = text.replace("\n", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.lower()
    
    words = text.split(" ")   # convert str to list
    return words

def count_words(words):
    # define a dict to store the word count
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1  # increment count for word
        else:
            word_count[word] = 1   # add word with count of 1
    return word_count

def display_word_count(word_count):
    words = list(word_count.keys())
    words.sort(key=str.lower)
    for word in words:
        count = word_count[word]
        print(word, "=", count)

def main():
    print("The Word Counter program")
    print()

    

    # get words, count, and display
    words = read_text(text) # get list of words
    word_count = count_words(words)       # create dict from list
    display_word_count(word_count)
    
if __name__ == "__main__":
    main()