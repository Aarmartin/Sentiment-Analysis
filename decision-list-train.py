# Aaron Martin
# Program reads in a list of reviews, and creates a decision list of words, based on that content, that are sorted by weight of their "usefulness" in determening whether or not a review is positive or negative
#
# 1. Take in input of text reviews
# 2. Separate by line (each line is a review)
# 3. Parse each review
#	a. Tokenize every word in the list (First is title, second is pos/neg value, start at 3)
#	b. Run tokenized list through 'not' handling function
#	c. Create tokenized bigram list of the content, and append it to the original list
#	d. Parse each word in this list
# 		i.   If the word has not been encountered, add it to dictionary
# 		ii.  If the review is positive, and the word has not been encountered, add + 1 to that word's positive count
# 		iii. If the review is negative, and the word has not been encountered, add + 1 to that word's negative count
# 		iv.  If the review is positive, and the word has not been encountered, add + 1 to the total positive count
# 		v.   If the review is negative, and the word has not been encountered, add + 1 to the total negative count
# 4. Parse the dictionary
# 	a. Calculate the word's weight
# 	b. Assign the word as positive or negative depending on probability values
# 5. Sort dictionary by weight
# 6. Output dictionary with each words value and weight to decision list
#
# 1 for positive and 0 for negative:
# review1.txt 1 this review is good
# review2.txt 0 this review is terrible
#
# Output:
# good 1 (heavy weight)
# terrible 0 (heavy weight)
# this (whichever value is dominant) (zero weight)
# review (whichever value is dominant) (zero weight)
# is (whichever value is dominant) (zero weight)

import sys
import re
import math

def notHandle(text):

	# Switch to determine if word needs to become not_word
	notSwitch = False;

	textL = text.split()
	L = []

	for word in textL:

		# Check if token is an end character in case not switch is turned on
		if re.search(r"[.!?]", word):
			notSwitch = False

		# If not switch is turned on, convert word to not_word
		if notSwitch:
			combine = ("not", word)
			word = "_".join(combine)

		# If current token is not, invert the not switch
		if word == "not":
			if not notSwitch:
				notSwitch = True
			else:
				notSwitch = False
		
		L.append(word)
		
	return L

# Take list of words and make list of bigrams
# "The quick brown fox"
# [ "The_quick", "quick_brown", "brown_fox" ]
def makeBigram(L):

	nl = []
	for i in range(len(L[2:]) - 1):
		nl.append("_".join(L[i+2:i+4]))

	return nl

def logCalc(masterDict, posNegDict):

	for key in masterDict:

		# Number of positive and negative instances
		numPos = masterDict[key][1]
		numNeg = masterDict[key][0]

		# Probability calculated
		pPos = (numPos + 1) / (posNegDict[1] + len(masterDict))
		pNeg = (numNeg + 1) / (posNegDict[0] + len(masterDict))
		
		# Log calculation
		val = math.fabs( math.log2( pPos / pNeg ) )

		# Associate positive or negative value with word
		if pPos > pNeg:
			masterDict[key].append(1)
		elif pNeg > pPos:
			masterDict[key].append(0)
		else:
			if posNegDict[1] > posNegDict[0]:
				masterDict[key].append(1)
			else:
				masterDict[key].append(0)

		# Associate weight with the word
		masterDict[key].append(val)

	return masterDict

# Outut function
def output(masterDict):
	for key in masterDict:
		print(key[0] + " " + str(key[1][2]) + " " + str(key[1][3]))

def main(argv):

	# Create List object filled with reviews, each element is full title, val, and review
	f = open(argv[1], "r")
	flines = f.readlines()
	f.close()

	masterDict = {}

	# Dictionary object key 0 is number of negative and key 1 is number of positive
	posNegDict = {0:0, 1:0}

	# For each review in flines
	for review in flines:

		# Create list of 'not' handled words
		content = notHandle(review)

		# Add in bigrams to total content
		content.extend(makeBigram(content))

		# Initialze set to hold words already encountered
		counted = set()

		#For each word in the review after title and val
		for word in content[2:]:

			if word not in counted:
			# Increment positive or negative count, create word with counts of zero if not found
				masterDict.setdefault(word, [0, 0])[int(content[1])] += 1
			

			#masterDict.setdefault(word, [0, 0])[int(content[1])] += 1

			# If word has not been encountered, add it to the set and increment amount of positive or negative words
			if word not in counted:
				counted.add(word)
			
			#Add to total number of positive or negative words
				posNegDict[int(content[1])] += 1


	# Append masterDict with associated pos/neg value and weight
	final = logCalc(masterDict, posNegDict)

	# Output sorted
	output(sorted(final.items(), key=lambda item: item[1][3], reverse=True))

main(sys.argv)
