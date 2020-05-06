# Cleaning text steps
# 1. Create the text file and select the text from it
# 2. Convert the entire text into lowercase
# 3. remove punctuations

import string
from collections import Counter
import matplotlib.pyplot as plt

# reading the text from file
text = open('read.txt', encoding='utf-8').read()
# print(string.punctuation)

# converting the text into lowercase
lower_case = text.lower()
# print(lower_case)

# removing punctuations using string.punctuation

# first parameter: characters that needs to be replaced
# second parameter: character with which it needs to be replaced
# third parameter: characters that needs to be deleted

# str.maketrans makes a transition table that will be returned after making changes to the string
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
# print(cleaned_text)

# Tokenisation
tokenized_words = cleaned_text.split()
# print(tokenized_words)

# Remove stop words (I, he, she etc) [nltk contains all the stop words]
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
# print(final_words)

# NLP Emotion algorithm:
# 1. Check if the word from final_words is present in the emotions.txt file
#       - open emotion file
#       - Loop through each line and clear it
#       - Extract the word and emotion using split
# 2. If the word is present,  add the emotion to emotion list
# 3. Finally count each emotion in the emotion list

emotions_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        # print(clear_line)
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotions_list.append(emotion)

# print(emotions_list)
w = Counter(emotions_list)
# print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('Graph.png')
plt.show()




