import unittest


def countQAPairs():
    lines = []
    qCount = 0
    aCount = 0
    # For loop that counts every line that starts with "question" or "answer"
    with open('QA_Pairs.txt') as f:
        for line in f:
            lines.append(line.split(None, 1)[0])
    # Counts the number of questions and answers
    for i in range(len(lines)):
        if lines[i].__contains__("question"):
            qCount += 1
    for i in range(len(lines)):
        if lines[i].__contains__("answer"):
            aCount += 1
    # Returns the lower value between the number of questions and number of answers (pair needs one question and one
    # answer, the number of pairs is dependant on whichever value is lower)
    if qCount == aCount:
        return qCount
    elif qCount > aCount:
        return aCount
    else:
        return qCount


class t1Tests(unittest.TestCase):
    def test1NumberOfPairs(self):
        QAPairCount = countQAPairs()
        self.assertEqual(QAPairCount, 5725) # 5725 is the expected amount of pairs

    def test2NumberOfLines(self):
        numLines = []
        with open('QA_Pairs.txt') as f:
            for line in f:
                numLines.append(line.split(None, 1)[0])

        self.assertEqual((len(numLines)//2), countQAPairs()) # Double check number of pairs, since pair takes 2 lines


if __name__ == '__main__':
    unittest.main(exit=True)
