# Sentiment Analysis
Python programs used to perform sentiment analysis on movie reviews

The goal of this project is to take in a movie review and provide an estimation of the sentiment felt by the author when making the review. It is trained on a corpus of movie reviews with their relevant sentiment classifications.

A list of words and bigrams are created with their associated word count for and whether or not they are associated with a positive or negative review. These values are then used to calculate the weight that an individual word has on its likelyhood of being positive or negative, e.g., 'the' will not contain much weight as it is frequently in both types of review, whereas 'amazing' will more frequently occur in positive reviews.

After the completion of the training program, a review is read in and works its way down a descision list tree of the word values and generates a score for either positive or negative.

The final program evalutes the score of how well the program performed at assigning its classifications.

This is a subset of the Pang and Lee 2002 Sentiment Classification / Movie Review data,
created by Ted Pedersen (tpederse@d.umn.edu).

This is the direct link to the original tar file :

http://www.cs.cornell.edu/people/pabo/movie-review-data/mix20_rand700_tokens_0211.tar.gz

The page with other versions and more info is found here :

http://www.cs.cornell.edu/people/pabo/movie-review-data/

# Running the Program
The program is run in three parts
```
python3 decision-list-train.py sentiment-train.txt > sentiment-decision-list.txt
python3 decision-list-test.py sentiment-decision-list.txt sentiment-test.txt > sentiment-system-answers.txt
python3 decision-list-eval.py sentiment-gold.txt sentiment-system-answers.txt > sentiment-system-answers-scored.txt
```
