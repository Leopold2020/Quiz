
from random import shuffle


class Question:
    def __init__(self, question, answer, alterantives : list):
        self.question = question            # själva frågan
        self.answer = answer                # svaret
        self.alternatives = alterantives    # alternativen
        shuffle(self.alternatives)

    def get_answer(self):
        return self.answer

    def get_answer(self):
        return self.answer

    def get_alternatives(self):
        return self.alternatives 
    

    def ask_question(self):
        print()
        print(self.question)
        for alt in self.alternatives:
            print(alt)
        answer = input("Your answer: ")
        if answer == self.answer:
            print("Correct!!!")
            # self.points += 1
        else:
            print("Incorrect...")



class Quiz:
    def __init__(self, name, questions: list):
        self.name = name
        self.questions = questions
        shuffle(self.questions)
        # self.points = []

    def get_name(self):
        return self.name
    
    def get_questions(self):
        return self.questions

    # def get_points(self):
    #     return self.points
    
    def start_quiz(self):
        #input(f"{self.questions}")
        print(f"Welcome to the {self.name} quiz!")
        for question in self.questions:
            question.ask_question()
            # print(f"You have {self.points} points")
    
def load_questions():
    quiz = []
    with open ("questions.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            Line = line.split("/")
        qu = Question(Line[0],
                     Line[1],
                     [Line[2],
                     Line[3],
                     Line[4]])

        quiz.append(qu)
    return quiz
