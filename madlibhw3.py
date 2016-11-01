# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import random
import nltk
from nltk.book import text2
from nltk.tokenize import sent_tokenize, word_tokenize

# print (type(text2))
# print (len(text2))
# print(dir(text2))

tagged_tokens = nltk.pos_tag(text2)
# print (text2[:150])

tag_map = {"NN":"a noun","NNS":"a plural noun","VB":"a verb", "VBD":"a verb, past tense", "JJ":"an adjective"}
subst_probabs = {"NN":.15,"NNS":.1,"VBD":.1, "VB":.1,"JJ":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []
og_text = []


for (word, tag) in tagged_tokens[:150]:
	og_text.append(spaced(word))
	if tag not in subst_probabs or random.random() > subst_probabs[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tag_map[tag]))
		final_words.append(spaced(new_word))

print ("Original text:\n")
print ("".join(og_text))
print ("\nMadlibbed text:\n")
print ("".join(final_words))

print("\n\nEND*******")
