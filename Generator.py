import random
import re

# Read the sample text
with open("D:\DATA\FelixOneDrive\OneDrive\Python\MarkovChain\sampletext.txt", encoding='utf-8') as f:
    sampletext = f.readlines()
    sampletext = "".join(sampletext)

# Clean the text
sampletext = sampletext.replace("\n", " ")
sampletext = sampletext.replace("\"", " ")
sampletext = sampletext.replace("'", " ")
sampletext = sampletext.replace(",", " ")
sampletext = sampletext.replace("[", " ")
sampletext = sampletext.replace("]", " ")

# Cut into sentences
sampletext = sampletext.split(".")

sentences = []
for i in sampletext:
    i = i.strip().lower()
    sentences.append(i.split())
    #print(i)
    
chained_words = []
starter_words = []
for sentence in sentences:
    for i in range(len(sentence)):
        if i == 0:
            starter_words.append(sentence[i].strip())
            
        if i+1 < len(sentence):
            chained_words.append([sentence[i].strip(), sentence[i+1].strip()])
        else:
            chained_words.append([sentence[i].strip(), '.'])

print(starter_words)

for count in range(20):
    final_string = random.choice(starter_words)
    current = final_string
    while True:
        if '.' in current or '!' in current or '?' in current: break

        valid_chains = []
        for i in chained_words:
            if i[0] == current:
                valid_chains.append(i)

        if len(valid_chains) > 0:
            choice = random.choice(valid_chains)
            final_string += ' ' + choice[1]
            current = choice[1]
        else: break

    print(final_string[:-2]+ ".")
    print("-------------------------------------------")
