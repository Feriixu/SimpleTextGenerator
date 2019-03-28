import random
import re

# Read the sample text
with open(r"D:\DATA\FelixOneDrive\OneDrive\Python\MarkovChain\sampletext.txt", encoding='utf-8') as f:
    sampletext = f.readlines()
    sampletext = "".join(sampletext)

# Clean the text
sampletext = sampletext.replace("\n", " ")
sampletext = sampletext.replace("\"", " ")
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
        if i == 0 and i+1 < len(sentence):
            starter_words.append([sentence[i].strip(), sentence[i+1].strip()])
            
        if i+2 < len(sentence):
            chained_words.append([sentence[i].strip(), sentence[i+1].strip(), sentence[i+2].strip()])
        else:
            chained_words.append([sentence[i].strip(), '.', ''])
            break

print(starter_words)

generated = []
for count in range(10):
    starter_word = random.choice(starter_words)
    final_string = str(starter_word[0][0]).upper() + starter_word[0][1:]
    current = [' ', starter_word[0], starter_word[1]]
    while True:
        
        if '.' in current[2] or '!' in current[2] or '?' in current[2]: break
        
        valid_chains = []
        for i in chained_words:
            if i[0] == current[1] and i[1] == current[2]:
                valid_chains.append(i)

        if len(valid_chains) > 0:
            choice = random.choice(valid_chains)
            final_string += ' ' + choice[1]
            current = [choice[0], choice[1], choice[2]]
        else: break

    print(final_string[:-2]+ ".")
    #print("-------------------------------------------")
    generated.append(final_string)


#file = open("generated.txt", "a")
#for i in generated:
#    file.write(i + "\n")
#file.close()
