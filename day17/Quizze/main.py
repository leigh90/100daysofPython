from question_model import Question
from day17.Quizze.data import question_data
from quiz_brain import QuizBrain



# # zawadi
# question_list = []
# for qst in question_data:
#     new_question = Question(qst['text'], qst['answer'])
#     question_list.append(new_question)
#     # print([qst['text'], qst['answer']])
#     # question_bank.append([new_question.text, new_question.answer])
# # print(question_list)
#
# # OR
# # question_bank = []
# # for question in question_data:
# #     question_text = question['text']
# #     question_answer = question['answer']
# #     new_question = Question(question_text, question_answer)
# #     question_bank.append(new_question)
# # print(question_bank)
#
# quiz = QuizBrain(question_list)
# while quiz.still_has_questions():
#     quiz.next_question()
#
# # if not quiz.still_has_questions():
# print("You have completed the quiz")
# print(f' Your final score was {quiz.score} out of {quiz.question_number}')

question_list = []
for qst in question_data:
    new_question = Question(qst['question'], qst['correct_answer'])
    question_list.append(new_question)

quiz = QuizBrain(question_list)
while quiz.still_has_questions():
    quiz.next_question()

# if not quiz.still_has_questions():
print("You have completed the quiz")
print(f' Your final score was {quiz.score} out of {quiz.question_number}')



