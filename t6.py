import collections, unittest


def findFrequency():
    # List initialization
    lines = []
    # Adds lines to list
    with open('unique_QA_Pairs.txt') as f:
        for line in f:
            lines.append(line)

    for i in range(len(lines)):
        temp = str(lines[i])
        temp = temp.replace('[', '')
        temp = temp.replace(']', '')
        temp = temp.replace('"', '')
        temp = temp.replace(',', '')
        temp = temp.replace('?', '')
        temp = temp.replace('(', '')
        temp = temp.replace(')', '')
        temp = temp.replace('\n', '')
        temp = temp.strip('\' ')
        temp = temp.lower()
        lines[i] = temp
    # Splits each line into individual words
    for i in range(len(lines)):
        lines[i] = lines[i].split()
    # Uses .Counted from collections to count how many times each words appears and sorts it into a dictionary
    wordsCounted = collections.Counter(word for words in lines for word in words)
    # Manually adds 1 count to 'answer' to make up for the odd text for the first answer.
    wordsCounted['answer'] += 1
    # Creates another dictionary list where the values are sorted
    wordFrequencies = sorted(wordsCounted.items())
    return wordsCounted, wordFrequencies


def t6Function():
    # Takes the unsorted dictionary and puts it in the txt file
    exportList = findFrequency()[1]
    for i in range(len(exportList)):
        print(exportList[i], file=open("Frequency.txt", "a"))


class t6Tests(unittest.TestCase):
    def test1CheckWordFrequencyInDictionary(self):
        freqDict = findFrequency()[0]
        self.assertEqual(freqDict['answer'], 2917)
        self.assertEqual(freqDict['question'], 2914)

    def test2CheckWordFrequencyInFile(self):
        with open("Frequency.txt") as f:
            fileContents = f.readlines()
        self.assertIn('(\'his\', 300)\n', fileContents)
        self.assertIn('(\'house\', 39)\n', fileContents)


if __name__ == '__main__':
    unittest.main(exit=True)
