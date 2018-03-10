stringToReverse = raw_input("Reverse this: ")

print "reverse word: %s" % stringToReverse[::-1]


for char in range(wordLength):
    print stringToReverse[(wordLength - 1) - char]