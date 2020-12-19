# Aaron Martin
# Sentiment Analysis testing program
#
# Program that reads in a decision list and a list of reviews and uses that decision list to determine if a review is positive or negative
#
# 1. Parse each review as before
# 	a. Preprocess the content with not handling and bigram creation as before
# 	b. Parse the decision list
#		i. if the review contains the word, assign the word's pos/neg value to the review
# 			- Output result
#			- Break
#
# review1.txt __ this was a terrible experience
# review2.txt __ this was a really good movie
#
# good 1 (heavy)
# terrible 0 (heavy)
#
# Output:
# review1.txt 0
# review2.txt 1

import sys
import re

# Handle 'not' of text, same as training program
def notHandle(text):

	notSwitch = False

	textL = text.split()
	L = []

	for word in textL:
		
		if re.search(r"[.!?]", word):
			notSwitch = False

		if notSwitch:
			combine = ("not", word)
			word = " ".join(combine)

		if word == "not":
			notSwitch = True

		L.append(word)

	return L

# Bigram creation, same as training program
def makeBigram(L):

	nl = []

	for i in range(len(L) - 1):
		nl.append("_".join(L[i:i+2]))

	return nl

# Determine if review is positive or negative
def determineCap(content, masterDict, cap):
	posScore = 0
	negScore = 0

	# For each word in the decision list, starting at top of sorted list
	for (key, i) in zip(masterDict, range(cap)):
		# Check if key is in the review
		if key in content[2:]:
			if masterDict[key][0] == str(1):
				posScore += float(masterDict[key][1])
			else:
				negScore += float(masterDict[key][1])

			# If word is found, return the determination
			#return masterDict[key][0]
	if posScore > negScore:
		return 1
	if negScore > posScore:
		return 0
	return -1

def determineFull(content, masterDict):
	posScore = 0
	negScore = 0

	# For each word in the decision list, starting at top of sorted list
	for key in masterDict:
		# Check if key is in the review
		if key in content[2:]:
			if masterDict[key][0] == str(1):
				posScore += float(masterDict[key][1])
			else:
				negScore += float(masterDict[key][1])

			# If word is found, return the determination
			#return masterDict[key][0]
	if posScore > negScore:
		return 1
	if negScore > posScore:
		return 0
	return -1

def determineWeight(content, masterDict):
	posScore = 0
	negScore = 0

	# For each word in the decision list, starting at top of sorted list
	for key in masterDict:
		# Check if key is in the review
		if key in content[2:]:
			if float(masterDict[key][1]) < 1:
				break
			if masterDict[key][0] == str(1):
				posScore += float(masterDict[key][1])
			else:
				negScore += float(masterDict[key][1])

			# If word is found, return the determination
			#return masterDict[key][0]
	if posScore > negScore:
		return 1
	if negScore > posScore:
		return 0
	return -1

def determine(content, masterDict):
	for key in masterDict:
		if key in content[2:]:
			return masterDict[key][0]
	return -1

def main(argv):
	
	masterDict = {}

	cap = int(input())

	flist = open(argv[1], "r")

	fdata = open(argv[2], "r")

	dlist = flist.readlines()

	data = fdata.readlines()



	# Take in decision list and make a dictionary with it
	for word in dlist:
		content = word.split()
		masterDict.setdefault(content[0], [content[1], content[2]])

	# For each review
	for review in data:

		# Preproccessing
		content = notHandle(review)
		content.extend(makeBigram(content))

		#Output title and its determination
		print(content[0], end=" ")

		print(determine(content, masterDict))
		#print(determineCap(content, masterDict, cap))
		#print(determineFull(content, masterDict))
		#print(determineWeight(content, masterDict))

	flist.close()
	fdata.close()

main(sys.argv)
