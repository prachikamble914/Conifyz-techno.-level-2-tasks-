print("************File Manipulation************")
from collections import Counter
import string
def filemanipulation(file1):
    word_count = Counter()
    translator = str.maketrans('','',string.punctuation)
    with open(file1,'r') as file:
        for line in file:
            line = line.translate(translator)
            words = line.lower().split()
            word_count.update(words)
        for word, count in sorted(word_count.items()):
            print(f"{word};{count}")
file = r"c:\Users\prachi\OneDrive\Desktop\prachi.txt"
filemanipulation(file)


