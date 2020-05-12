#Question
class Question : 
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer

q1 = Question('en iyi programlama dili hangisidir?',['C#','Python','javascript','java'], 'python')  
q2 = Question('en popüler programlama dili hangisidir?',['C#','Python','javascript','java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir?',['C#','Python','javascript','java'], 'python')
liste = [q1,q2,q3]

print(q1.checkAnswer('python'))
print(q2.checkAnswer('c#'))
#Quiz
class Quiz:
    def __init__(self,questions):
        self.questions= questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f' Soru {self.questionIndex + 1} : {question.text} ') 

        for q in question.choices:
            print('-'+q)

        answer = input('cevap:')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex +=1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.ShowScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def displayProgress(self):
        totalquestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        
        if questionNumber > totalquestion:
            print("quiz bitti")
        else:
            print(f'Question {questionNumber} of {totalquestion}'.center(100,'*'))

    def ShowScore(self):
        print('score',self.score)

q1 = Question('en iyi programlama dili hangisidir?',['C#','Python','javascript','java'], 'python')  
q2 = Question('en popüler programlama dili hangisidir?',['C#','Python','javascript','java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir?',['C#','Python','javascript','java'], 'python')
questions = [q1,q2,q3]
 
quiz = Quiz(questions)
quiz.loadQuestion()





  