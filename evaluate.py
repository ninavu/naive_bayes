import os
import sys
import readline
from load import *
from naivebayes import *

# this function creates a string to build a matrix from a list
def matrix_str(L):
    s = ''
    for i in range(len(L)-1):
        s += str(L[i])
        s += "  "
    s += str(L[-1])
    return s

# this function creates a string in the test file from a list
def to_string(L):
    s = ""
    for i in range(len(L)-1):
        s += str(L[i])
        s += ","
    s += str(L[-1])
    return s + "\n"

# this function creates a string in the training file from a list of lists
def ll_to_string(L):
    s = ""
    for data in range(len(L)):
        for i in range(len(L[data])-1):
            s += str(L[data][i])
            s += ","
        s += str(L[data][-1])
        s += "\n"
    return s

# this function copies all the features from the sample files to the new training and test files
def features_str(features):
    s = ""
    k = list(features.keys())

    for i in range(len(k)):
        s += "@attribute "
        s += k[i]
        val = features.get(k[i])
        s += "     {"
        for j in range(len(val)-1):
            s += val[j]
            s += ", "
        s += val[-1]
        s += "} \n"
    return s + "\n"

# this function perfroms leave-one-out-cross validation
def LOOCV(data, att):
    result = []

    for i in range(len(data)):
        fte = open("test.txt", "w")
        fte.write(features_str(att))
        fte.write(to_string(data[i]))
        fte.close()

        ftr = open("training.txt", "w")
        ftr.write(features_str(att))
        ftr.write(ll_to_string(data[:i]))
        ftr.write(ll_to_string(data[i+1:]))
        ftr.close()

        os.system('python3 naivebayes.py training.txt test.txt result.txt')

        L = []
        fre = open("result.txt", "r")
        line = fre.readline().split()
        L.append(line[0])
        for j in line[1:]:
            L.append(round(float(j), 2))
        result.append(L)
        fre.close()
    return result

# this function construct a confusion matrix
def confusion_matrix(result, data, att):
    L = [[0] * (len(att)) for i in range(len(att))]

    for i in range(len(result)):
        predicted = result[i][0]
        actual = data[i][-1]
        for j in range(len(att)):
            if predicted == actual and actual == att[j]:
                L[j][j] += 1
            else: 
                for k in range(len(att)):
                    if actual == att[j] and predicted == att[k]:
                        L[j][k] += 1
    return L

# this function calculates all accurate results from the confusion matrix
def accuracy(matrix, len_data):
    acc = 0
    for i in range(len_data):
        acc += matrix[i][i]
    return acc

def main():
    argv = sys.argv[1:]
    if len(argv) == 1:
        features = load(argv[0])[0]
        input = load(argv[0])[1]
    else:
        print("There should be 1 input file total. Can't run the program!")
        return None

    result = LOOCV(input, features)

    sample = input[0][-1]
    k = find_key(features, sample)
    category  = features.get(k)
    L = confusion_matrix(result, input, category)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s1 = ""
    for i in range(len(category)):
        s1 += alphabet[i]
        s1 += "  "
    print(s1 + " <== classified as")

    for i in range(len(category)):
        s2 = matrix_str(L[i]) 
        s3 = "| " + alphabet[i] + "= " + str(category[i])
        print(s2 + s3.rjust(12))

    acc = round(accuracy(L, len(category)) / len(result) * 100, 2)
    print("Overall Accuracy: " + str(accuracy(L, len(category))) + "/" + str(len(result)) + " " + str(acc) + "%")

main()