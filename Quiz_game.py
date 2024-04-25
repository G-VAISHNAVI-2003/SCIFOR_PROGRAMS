class quiz:
    def __init__(self, question, option, ans):
        self.question = question
        self.option = option
        self.ans = ans

    def disp(self):
        print(self.question)
        for i, j in enumerate(self.option):
            print(str(i + 1) + ". " + j)
        print()

    def check(self, inp_ans):
        return inp_ans == self.ans

class udemy:
    def __init__(self, ques):
        self.ques = ques
        self.sc = 0
        self.curr_ques = 0

    def disp_q(self):
        self.ques[self.curr_ques].disp()

    def ch_ans(self, inp_ans):
        if self.ques[self.curr_ques].check(inp_ans):
            print("The answer is correct!..\n")
            self.sc += 1
        else:
            print("Incorrect answer!..\n")
        self.curr_ques += 1

    def res(self):
        print("Your score: " + str(self.sc) + " for " + str(len(self.ques)) + " questions!")

q1 = quiz("What symbol is used for comments in Python?", ["//", "/*", "#", "--"], "3")
q2 = quiz("Which data type is used to store a sequence of characters in Python?", ["int", "str", "float", "list"], "2")
q3 = quiz("What is the output of 'print(3 == 3.0)' in Python?", ["True", "False", "Error", "None"], "1")

ques_list = [q1, q2, q3]

my_quiz = udemy(ques_list)

while my_quiz.curr_ques < len(my_quiz.ques):
    my_quiz.disp_q()
    user_input = input("Enter your answer: ")
    my_quiz.ch_ans(user_input)

my_quiz.res()
