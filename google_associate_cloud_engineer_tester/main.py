#!/usr/local/bin/python3

import re
import random
import os
from datetime import datetime

all_questions = []
question_dir = "questions-answers/"
chapters_amount = 18
test_questions_amount = 10

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Answer:
    letter = ""
    text = ""
    correct = False
    description = ""

    def __init__(self, letter, text, correct, description):
        self.letter = letter
        self.text = text
        self.correct = correct
        self.description = description

class Question:
    text = ""
    answers = []

    def __init__(self, text):
        self.text = text
        self. answers = []

class Test:
    questions = []

def collect_questions():
    for chapter in range(1, chapters_amount + 1):
        print(chapter)
        with open(question_dir + str(chapter) + ".questions" ) as question_file, open (question_dir + str(chapter) + ".answers") as answers_file:
            for question in range(0,20):
                raw_question_text = question_file.readline()
                question_text = re.sub(r'\d+\.','', raw_question_text)
                test_question = Question(question_text)
                raw_correct_answer_text = answers_file.readline()
                correct_answer_letter = str(re.findall(r'[A-Z]\.', raw_correct_answer_text)[0]).strip().strip(".")
                correct_answer_text = str(re.sub(r'^\d+\.\ [A-Z]{1}\.', '', raw_correct_answer_text))
                for answer_number in range(0,4):
                    raw_answer_text = question_file.readline()
                    answer_letter = str(re.findall(r'[A-Z]\.', raw_answer_text)[0]).strip().strip(".")
                    answer_text = re.sub(r'[A-Z]\.','', raw_answer_text)
                    if correct_answer_letter == answer_letter:
                        test_question.answers.append(Answer(answer_letter, answer_text, True, correct_answer_text))
                    else:
                        test_question.answers.append(Answer(answer_letter, answer_text, False, ""))
                all_questions.append(test_question)

def generate_test():
    questions = 0
    already_chosen_questions = []
    final_test = Test()
    current_test_questions_amount = len(final_test.questions)
    while current_test_questions_amount != test_questions_amount:
        total_questions = len(all_questions)
        random_number = random.randint(0, total_questions - 1)
        if random_number not in already_chosen_questions:
            final_test.questions.append(all_questions[random_number])
            already_chosen_questions.append(random_number)
            current_test_questions_amount = len(final_test.questions)
    return final_test

def start_test(test):
    score = 0
    failed_questions = []
    for question in test.questions:
        os.system('clear')
        print(f"{question.text}")
        correct_answer = None
        user_answer = None
        for answer in question.answers:
            print(f"{answer.letter}.{answer.text}")
            if answer.correct:
                correct_answer = answer
        user_input = str.capitalize(input("Enter Answer: "))
        for answer in question.answers:
            if user_input == answer.letter:
                user_answer = answer

        os.system('clear')
        if user_answer == correct_answer:
            print(f"{bcolors.OKGREEN}{correct_answer.letter}. {correct_answer.text}{bcolors.ENDC}")
            score = score + 1
        else:
            print(f"{bcolors.FAIL}{user_answer.letter}. {user_answer.text}{bcolors.ENDC}")
            print(f"{bcolors.OKGREEN}{correct_answer.letter}. {correct_answer.text} {correct_answer.description}{bcolors.ENDC}")
            failed_questions.append(question)
        input()

    os.system('clear')
    end_score = (float( float(score) / float(len(test.questions)) ) * 100)
    print(f"End Of Test, Total Score: {end_score}%")
    if len(failed_questions) > 0:
        print("FAILED QUESTIONS")
        suffix = datetime.today().strftime('%Y_%m_%d_%H_%M')
        with open(question_dir + "failed." + suffix, 'a+') as failed_log:
            for question in failed_questions:
                print(f"QUESTION: {question.text}")
                failed_log.write(f"QUESTION: {question.text}")
                for answer in question.answers:
                    if answer.correct:
                        print(f"CORRECT ANSWER: {answer.letter}. {answer.text}")


if __name__ == "__main__":

    collect_questions()
    test = generate_test()
    start_test(test)
