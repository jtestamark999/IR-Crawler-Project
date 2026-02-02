import os
import string
from collections import Counter
word=""
def clean_text(text):
    text = text.lower()
    text=text.translate(str.maketrans("","", string.punctuation))
    words=text.split()
    return words

files =[]

for file in os.listdir():
    if file.startswith("page_")and file.endswith(".txt"):
        files.append(file)

print("Total files: ",len(files))

word_counter=Counter()
doc_freq=Counter()
total_words=0

for filename in files:
    with open(filename,"r",encoding="utf-8") as f:
        content=f.read()
    words=clean_text(content)
    total_words+=len(words)
    word_counter.update(words)
    unique_words=set(words)
    for word in unique_words:
        doc_freq[word]+=1

num_docs=len(files)
unique_word_count=len(word_counter)
average_length=total_words/num_docs

print("\n===== Information ====="
      "\nTotal words   : ",total_words,
      "\nUnique words  : ",unique_word_count,
      "\nAverage words : ",round(average_length,2))

top_30=word_counter.most_common(30)
pointer = int(1)
print("\n=====Top 30 words:=====")
for word,count in top_30:
    print(pointer,".", word,"CF:",count," DF: ",doc_freq[word])
    pointer +=1

stop_words={"the"
    ,"and","is","in","to","of","a","that","it","for",
    "on","with","as","this","by","be","are","was","at","or"}

filtered_counter=Counter()
for word,count in word_counter.items():
    if word not in stop_words:
        filtered_counter[word]=count

filtered_top_30=filtered_counter.most_common(30)
print("\n=====Top 30 (No STop Words)=====")
pointer = int(1)
for word,count in filtered_top_30:
    print(pointer,".", word,count)
    pointer+=1


