import unittest


def uniqueDictionary():
    # List initialization
    lines = []
    uniqueLinesDict = {}
    # Convert lines into a list
    with open('unique_QA_Pairs.txt') as f:
        for line in f:
            lines.append(line)

    for i in range(len(lines)):
        temp = str(lines[i])
        temp = temp.replace('[', '')
        temp = temp.replace(']', '')
        temp = temp.replace('"', '')
        temp = temp.replace(',', '')
        temp = temp.strip('\' ')
        temp = temp[:-1]
        temp = temp.lower()
        lines[i] = temp
    # Add entries to the dictionaries with the answer as the key and question as value
    for i in range(len(lines)):
        if i % 2 == 1:
            uniqueLinesDict[(lines[i - 1])] = lines[i]
    # Adds dictionary to txt file
    f = open("QA_Dictionary.txt", "a")
    f.write(str(uniqueLinesDict))
    f.close()

    return uniqueLinesDict


class t3Tests(unittest.TestCase):
    def test1CheckEntryA(self):
        uniDict = uniqueDictionary()
        self.assertEqual("question who is the half-brother of arya's half-brother?",
                         uniDict.get('answer jon snow king'))

    def test2CheckEntryB(self):
        uniDict = uniqueDictionary()
        self.assertEqual('question tyrion is genuinely loyal to those who treat him with what?',
                         uniDict.get('answer love and respect'))


if __name__ == '__main__':
    unittest.main(exit=True)
