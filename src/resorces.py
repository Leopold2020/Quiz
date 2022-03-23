
from random import randint
class Question:
    def __init__(self, question, answer, alterantives) -> None:
        self.question = question            # själva frågan
        self.answer = answer                # svaret
        self.alternatives = alterantives    # alternativen

    def ask_question(self):
        answer = input("Your answer: ")
        if answer == self.answer:
            print("Correct!!")

class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions
        #self.points = 0
        #self.list = randint(1, 2)

    def get_name(self):
        return self.name

    def get_list(self):
        return self.list

    
    # def generate_list(self):
    #     random_list = randint(0, 10)
        # if random_list == 0: self.list =  
        # elif random_list == 1: self.list =  
        # elif random_list == 2: self.list =  
        # elif random_list == 3: self.list =  
        # elif random_list == 4: self.list =  
        # elif random_list == 5: self.list =  
        # elif random_list == 6: self.list =  
        # elif random_list == 7: self.list =  
        # elif random_list == 8: self.list =  
        # elif random_list == 9: self.list =  
        # elif random_list == 10: self.list =  

    
    def generate_question(self):
        if self.list == 1:
            awnser = input(f"what year is it? \n1. 2014 \n2. 2020 \n3. 2022")
            if awnser == "3" or "3." or "2022":
                print("Rigth awnser")

            else: 
                print("wrong")
        elif self.list == 2:
            print("NO")
    