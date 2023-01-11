import sys
from load import *

# this function counts the number of class type appeared in the data instances
def class_count(sample, training):
    count = 0
    for l in training:
        if sample in l:
            count += 1
    return count

# this function counts the number of assigned feature appeared under the condition of another feature
def condition_count(feature, sample, training):
    count = 0
    for l in training:
        if (feature in l) and (sample in l):
            count += 1
    return count

# this function calculates the pseudo-probability of each class based on all the given features
def probabilities(sample, training, input):
    sample_count = class_count(sample, training)
    p_class = sample_count / len(training)

    result = p_class
    for feature in input[:-1]:
        result *= condition_count(feature, sample, training) / sample_count
    return result

# this function finds the key using a value in a dictionary of value lists
def find_key(dict, found):
    k = ""
    items_list = list(dict.items())
    for i in range(len(items_list)):
        for j in range(len(items_list[i])):
            if found in items_list[i][j]:
                k = items_list[i][j-1]
    return k

def main():
    argv = sys.argv[1:]
    if len(argv) == 3:
        training_data = load(argv[0])
        input_data = load(argv[1])
        prediction = argv[2]
        if training_data[0] != input_data[0]:
            print("Training and Input files are not matched! Choose a different file!")
    else:
        # print("There should be 3 files total. Can't run the program!")
        return None
    
    sample = training_data[1][0][-1]
    k = find_key(training_data[0], sample)
    sample_class = training_data[0].get(k)
    fout = open(prediction, "w")
    
    for line in input_data[1]:
        max_output = ""
        max_prob = -1
        list_type = []
        total_prob = 0
        for type in sample_class:
            prob = probabilities(type, training_data[1], line)
            total_prob += prob
            list_type.append(prob)
            if prob > max_prob:
                max_prob = prob
                max_output = type
        fout.write(max_output + "   ")
        for i in range(len(list_type)):
            real_prob = round(list_type[i] / total_prob, 2)
            fout.write(str(real_prob) + " ")
        fout.write("\n")
    fout.close()
main()
