# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    f = open(filename, 'r')
    lines = f.read()
    f.close()
    return lines

# read_file_content('story.txt')



def count_words(text):
    text = read_file_content(text).lower()
    a = text.count('as ')
    b = text.count('would ')
    mesg = {'as':a, 'would':b}
    print (mesg)
    return

count_words('story.txt')
