import unittest


def exportAnswers():
    # List initialization
    answers = []
    # Only adds answer lines to list
    with open('unique_QA_Pairs.txt') as f:
        for line in f:
            if line.startswith("answer") or line.startswith("ï»¿answer"):
                answers.append(line.split('\n'))
    for i in range(len(answers)):
        temp = str(answers[i])
        temp = temp.replace('answer', '')
        temp = temp.replace('[', '')
        temp = temp.replace(']', '')
        temp = temp.replace('"', '')
        temp = temp.replace(',', '')
        temp = temp.replace('ï»¿ï»¿', '')
        temp = temp.strip('\' ')
        answers[i] = temp
    # Adds all answer lines to txt file
    for i in range(len(answers)):
        print(answers[i], file=open("Answers.txt", "a"))


class t5Tests(unittest.TestCase):
    def test1CheckAnswerA(self):
        with open("Answers.txt") as f:
            fileContents = f.readlines()
        self.assertIn('forge her own destiny\n', fileContents)

    def test1CheckQuestionB(self):
        with open("Answers.txt") as f:
            fileContents = f.readlines()
        self.assertIn('rumors that he has a supernatural link to his direwolf and that he is invulnerable\n',
                      fileContents)


if __name__ == '__main__':
    unittest.main(exit=True)