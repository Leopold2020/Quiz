from resorces import Quiz, Question


def main():
    q1 = Question("Vilken färg är himlen?", "blå", ["blå", "röd", "grön", "gul"])
    q2 = Question("Hur många tjejer går i INF20?", "2", ["2", "3", "10", "5"])
    oskar_quiz = Quiz("Random NTI Facts" , [q1, q2])


    oskar_quiz.start_quiz()

    #läs in frågor från fil!
    # spara dessa på formen
    # Fråga/Svar/Alternativ1,alternativ2,alternativ3
    # osv.

    # ex. Vilken färg är himlen?/blå/blå, röd, grön, gul
    # for-loopa igenom filen med f.readlines()
    # varje index i f.readlines är en rad (lagrad som en lista)

if __name__ == "__main__":
    main()
