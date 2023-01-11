import readline

# a function that takes the name of a arff file and returns a dictionary of lists as features
# and a list of lists of all the samples
def load(fileName):
    fin = open(fileName, "r")
    lines = fin.readlines()

    features = {}
    remove_char = ['{', '}', ',']
    sample = []
    start_line = ["@attribute", "@relation", "@data", "%"]
    for line in lines:
        values = []
        if (line.startswith(start_line[0])):
            for c in remove_char:
                line = line.replace(c, "")
            k = line.split()
            values = k[2:]
            features[k[1]] = values
        
        elif not (line.startswith(start_line[1]) or line.startswith(start_line[2]) or line.startswith(start_line[3])):
            k = line.strip()
            if (len(k) != 0):
                values = k.split(",")
                sample.append(values)

    fin.close()
    return features, sample

# def main():
#     # print(load("sampletraining.arff"))
#     # print(load("sampleinput.arff"))
#     print(load("contact-lenses.arff"))
    
# main()