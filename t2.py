import unittest


def storeUniquePairs():
    # List initialization
    lines = []
    uniquePairs = []
    overlapping = []
    pairList = []
    heldLines = []
    # Make lines from txt into list
    with open('QA_Pairs.txt') as f:
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

    # Make tuple pairs knowing every odd line is a question
    for i in range(len(lines)):
        if i % 2 == 1:
            pairList.append((lines[i - 1], lines[i]))
    # Loop to sort through unique and overlapping pairings
    q = 0
    a = 1
    for i in range(len(pairList)):
        # Checks if either the question or answer in a pair has already been encountered before. If both are unique,
        # adds them to the unique list, otherwise puts the pair in the overlapping list
        if (pairList[i][q]) not in heldLines:
            if (pairList[i][a]) not in heldLines:
                uniquePairs.append(pairList[i])
                heldLines.append(pairList[i][q])
                heldLines.append(pairList[i][a])
            else:
                overlapping.append(pairList[i])
        else:
            overlapping.append(pairList[i])

    # Puts both lists into their own txt files
    for i in range(len(uniquePairs)):
        print(uniquePairs[i][q], file=open("unique_QA_Pairs.txt", "a"))
        print(uniquePairs[i][a], file=open("unique_QA_Pairs.txt", "a"))
        pass

    for i in range(len(overlapping)):
        print(overlapping[i][q], file=open("Overlapping.txt", "a"))
        print(overlapping[i][a], file=open("Overlapping.txt", "a"))
        pass

    return uniquePairs, overlapping


class t2Tests(unittest.TestCase):
    def test1CheckUnique(self):
        with open("unique_QA_Pairs.txt") as f:
            fileContents = f.readlines()

        self.assertIn("answer winterfell\n", fileContents)
        self.assertIn("question where did arya return to?\n", fileContents)
        self.assertIn("answer storm\n", fileContents)
        self.assertIn("question in what storm is the ship badly damaged?\n", fileContents)

    def test2CheckOverlapping(self):
        with open("Overlapping.txt") as f:
            fileContents = f.readlines()

        self.assertIn("answer mycah\n", fileContents)
        self.assertIn("question who does nymeria cut when he threatens arya?\n", fileContents)
        self.assertIn("answer winterfell\n", fileContents)
        self.assertIn("question where does eddard send his daughters back to?\n", fileContents)


if __name__ == '__main__':
    unittest.main(exit=True)
