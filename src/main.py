from resorces import Quiz, Question


def main():
    q1 = Question("Vilken färg är himlen?", "blå", ["blå", "röd", "grön", "gul"])
    q2 = Question("Hur många tjejer går i INF20?", "2", ["2,", "3", "10", "5"])
    oskar_quiz = Quiz("Random NTI Facts" , [q1, q2])

    quiz1 = Quiz("Quiz 1", 0)
    

if __name__ == "__main__":
    main
    