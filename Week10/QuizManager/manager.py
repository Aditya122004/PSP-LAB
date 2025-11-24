from QuizManager.quiz import Quiz

class QuizManager:
    def __init__(self):
        self.quizzes = {}   

    def create_quiz(self, title):
        quiz = Quiz(title)
        self.quizzes[title] = quiz
        return quiz

    def get_quiz(self, title):
        return self.quizzes.get(title)

    def solve_quiz(self, quiz):
        print(quiz.title)

        score = 0
        for q in quiz.questions:
            print(q["question"])
            for idx, opt in enumerate(q["options"], start=1):
                print(f"{idx}. {opt}")

            ans = int(input("Your answer: ")) - 1
            if q["options"][ans] == q["answer"]:
                score += 1

        print("Your Score:", score, "/", len(quiz.questions))
