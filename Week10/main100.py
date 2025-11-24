from QuizManager.manager import QuizManager
manager = QuizManager()
titles=[]
while True:
    print("1. Create Quiz")
    print("2. Solve Quiz")
    print("Enter any other key to Exit")

    ch = int(input("Choice: "))
    if ch == 1:
        title=input("Enter the title of the quiz: ")
        quiz = manager.create_quiz(title)
        n=int(input("Enter the number of questions: "))
        for i in range(n):
            q=input("Enter the question: ")
            op=[]
            for i in range(1,5):
                o=input(f"Enter option {i}: ")
                op.append(o)
            ca=int(input("Enter Correct Option Number: "))
            quiz.add_question(
                q,op,op[ca-1]
            )
        print("Quiz created successfully!")
        titles.append(title)

    elif ch == 2:
        print("Quizzes:")
        for i in range(len(titles)):
            print(f"{i+1} {titles[i]}")
        q=int(input("Enter the number of the Quiz you want to solve: "))
        quiz = manager.get_quiz(titles[q-1])
        if quiz:
            manager.solve_quiz(quiz)
        else:
            print("Quiz not found!")
    else:
        print("Exiting Program")
        break


