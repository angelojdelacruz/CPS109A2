from t6 import findFrequency
import unittest


def t7Function():
    # Takes a dictionary from the function in t6
    exportedList = findFrequency()[0]
    # Sorts the exported dictionary by values from smallest to largest, then reverses it to get a descending order
    resortedValues = sorted(exportedList.items(), key=lambda value: value[1])
    resortedValues.reverse()
    # Adds the exported dictionary entries into a txt file
    for i in range(len(resortedValues)):
        print(resortedValues[i], file=open("Decreasing_Frequency.txt", "a"))


class t7Tests(unittest.TestCase):
    def test1CheckWordFrequencyInDictionary(self):
        freqDict = findFrequency()[0]
        self.assertEqual(freqDict['answer'], 2917)
        self.assertEqual(freqDict['question'], 2914)

    def test2CheckWordFrequencyInFile(self):
        with open("Decreasing_Frequency.txt") as f:
            fileContents = f.readlines()
        self.assertIn("('the', 2148)\n", fileContents)
        self.assertIn("('what', 1769)\n", fileContents)
        self.assertIn("('to', 1381)\n", fileContents)
        self.assertIn("('does', 1081)\n", fileContents)
        self.assertIn("('of', 979)\n", fileContents)


if __name__ == '__main__':
    unittest.main(exit=True)
