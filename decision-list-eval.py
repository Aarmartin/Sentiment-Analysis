# Aaron Martin
# Sentiment Analysis evaluation program
#
# Program that compares the results of sentiment analysis with the correct values and outputs Recall, Precision, and Accuracy
#
# 1. Read in tested results and gold answers
# 2. Parse the titles
#	a. Compare the result with the answer,
# 	b. If the are the same
#		i.  Add to number of correct
#		ii. Add to either true positive or true negative depending on the value
#	c. If the are not the same
#		i. Add to either false positive or false negative depening on values
#	d. Print title, result, and true
# 3. Compute Recall, Precision, and accuracy
# 4. Output results
#
# Output:
# review1.txt True: 1 Test: 1
# review2.txt True: 0 Test: 1
# review3.txt True: 0 Test: 0
# Precision: (calculated precision)
# Recall: (calculated recall)
# Accuracy: (Calculated accuracy)

import sys

def main(argv):

	fgolds = open(argv[1], "r")
	fresults = open(argv[2], "r")

	golds = fgolds.readlines()
	results = fresults.readlines()

	fgolds.close()
	fresults.close()

	correct = 0

	truePos = 0
	trueNeg = 0
	falsePos = 0
	falseNeg = 0

	for (gold, result) in zip(golds, results):
		g = gold.split()
		r = result.split()
		if g[1] == r[1]:
			if(g[1] == str(1)):
				truePos += 1
			else:
				trueNeg += 1

			correct += 1
		else:
			if(g[1] == str(1)):
				falseNeg += 1
			else:
				falsePos += 1
		print(g[0] + " True: " + str(g[1]) + " Test: " + str(r[1]))

	precision = truePos / (truePos + falsePos)
	recall = truePos / (truePos + falseNeg)
	accuracy = (truePos + trueNeg) / (truePos + falsePos + trueNeg + falseNeg)

	print("\nNumber of correct evaluations: " + str(correct) + " out of " + str(len(golds)))
	print("Accuracy: " + str(accuracy))
	print("Precision: " + str(precision))
	print("Recall: " + str(recall))

main(sys.argv)
