# Naive Bayes and Leave-One-Out Cross-Validation


First part: Implementing Naive Bayes
The program does the following steps:
1. Take inputs from text files that contains a all the training and input data through the function load()
2. Assess each line of sample in the input data 
3. Calculate the pseudo-probability of each type of the class sample using the line information with Naive Bayes Classifer
4. Calculate the total pseudo-probabilities of all the types
5. Get the real probabilities by dividing each pseudo-probability by the tottal pseudo-probabilities
6. Output the type and all the real probabilities in a corresponding order to a designated file

To test the file, run as follow: $python3 naivebayes.py sampletraining.arff sampleinput.arff predictions.txt

Second part: Implementing Leave-One-Out Cross-Validation
The program does the following steps:
1. Create a test file that contains only 1 sample
2. Create a training file that contains the remaining samples
3. Call naivebayes.py with various input files
4. Contain all of the results inside a list
5. Put all of this in a loop that iterate "n" times to have each sample in the dataset as the test sample once
6. Create a confusion matrix to calculate the number of matches and mismatches
7. Calculate the overall accuracy from the matrix

To test the file, run as follow: $python3 evaluate.py contact-lenses.arff