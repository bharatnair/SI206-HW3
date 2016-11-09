# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

print ()
print ("*** SI 206 - HW 3 - Madlib Program ***")
print ("\nName: Bharat Nair\nUniqname: bnair")

print("\n*******START*******\n")

import random
import nltk
from nltk.book import text2
from nltk.tokenize import sent_tokenize, word_tokenize

# print (type(text2))
# print (len(text2))
# print(dir(text2))

#applying part of speech tags to the first 150 tokens
tagged_tokens = nltk.pos_tag(text2[:150])
# print (text2[:150])
# print (tagged_tokens)

#the below code adds a tag map and also creates a dict of probabilities substitutions
tag_map = {"NN":"a noun","NNS":"a plural noun","VB":"a verb", "VBD":"a verb, past tense", "JJ":"an adjective"}
subst_probabs = {"NN":.15,"NNS":.1,"VBD":.1, "VB":.1,"JJ":.1}

#the below code takes care of spacing before pucntuation
def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []
og_text = []

#the below code analyzes every token's and checks whether it needs to be substituted or not
#if it does, then it takes user input to make the substitution
for (word, tag) in tagged_tokens[:150]:
	og_text.append(spaced(word))
	if tag not in subst_probabs or random.random() > subst_probabs[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tag_map[tag]))
		final_words.append(spaced(new_word))

print ("\nOriginal text:\n")
print ("".join(og_text))
print ("\nMadlibbed text:\n")
print ("".join(final_words))

print("\n\n*******END*******\n")
