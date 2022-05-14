import unittest


def exportQuestions():
    # List initialization
    questions = []
    # Only adds question lines to list
    with open('unique_QA_Pairs.txt') as f:
        for line in f:
            if line.startswith("question"):
                questions.append(line.split('\n'))
    for i in range(len(questions)):
        temp = str(questions[i])
        temp = temp.replace('question', '')
        temp = temp.replace('[', '')
        temp = temp.replace(']', '')
        temp = temp.replace('"', '')
        temp = temp.replace(',', '')
        temp = temp.strip('\' ')
        questions[i] = temp
    # Adds all questions from the list to a txt file
    for i in range(len(questions)):
        print(questions[i], file=open("Questions.txt", "a"))


class t4Tests(unittest.TestCase):
    def test1CheckQuestionA(self):
        with open("Questions.txt") as f:
            fileContents = f.readlines()
        self.assertIn('who does arya take after?\n', fileContents)

    def test1CheckQuestionB(self):
        with open("Questions.txt") as f:
            fileContents = f.readlines()
        self.assertIn('who are the two murderers who threaten arya and gendry?\n', fileContents)


if __name__ == '__main__':
    unittest.main(exit=True)