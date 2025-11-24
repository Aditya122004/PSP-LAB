class Quiz:
    def __init__(self, title):
        self.title = title
        self.questions = [] 

    def add_question(self, question_text, options, correct_answer):
        q = {
            "question": question_text,
            "options": options,
            "answer": correct_answer
        }
        self.questions.append(q)
