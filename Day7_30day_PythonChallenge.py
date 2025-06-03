from collections import Counter as c
import re #regular expression module 

def count_word(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Convert text to lowercase
        words = re.findall(r'\b\w+\b', text)  # Extract words using regex
        word_count = c(words)  # Count word frequencies
    return word_count

#passing file name 
filename = 'WordFrequency.txt' 

#calling count_word function with variable filename
frequencies = count_word(filename)

# Printing count of each word
for word, count in frequencies.most_common():
    print(f'{word}: {count}')
