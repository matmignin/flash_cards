#!/usr/bin/env python
import re

with open('patho.txt', 'r') as f:
    list_of_questions = f.read()
    converted_list = re.sub('\n', '<br>', list_of_questions)
    questions = (converted_list.split('<br><br>'))
    for question in questions:
        question = re.sub('\. ', "<br>", question, 1)
        #print(question)

print(question[2])
