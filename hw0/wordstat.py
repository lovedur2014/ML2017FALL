import sys
def wordstat(infilename, outfilename):
    uniquewords = []
    wordstat = {}
    with open(infilename) as infile:
        for line in infile:
            for word in line.split():
                if word not in wordstat:
                    uniquewords.append(word)
                    wordstat[word] = 1
                else:
                    wordstat[word] = wordstat[word] + 1
    with open(outfilename, 'w') as outfile:
        for i in range(len(uniquewords)):
            print("%s %d %d" % (uniquewords[i], i, wordstat[uniquewords[i]]),file = outfile)
    infile.close()
    outfile.close()

if __name__ == "__main__":
    wordstat(sys.argv[1], "Q1.txt")

            
