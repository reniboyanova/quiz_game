from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []


for dict_pair in question_data:
    question_text = dict_pair['question']
    question_answer = dict_pair['correct_answer']
    question = Question(question_text, question_answer)
    question_bank.append(question)

game = QuizBrain(question_bank)

while game.still_have_questions():
    game.next_question()

print("You complete teh challenge!")
print(f"Your final score was: {game.score}/{game.question_number}")


