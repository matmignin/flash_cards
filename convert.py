#!/usr/bin/env python
import re

with open('patho.txt', 'r') as f:
    list_of_questions = f.read()
    convert_html = re.sub('\n', '<br>', list_of_questions)
    post_number = re.sub(r'(?<=\d)\.', '<br>', convert_html)
    question = (post_number.split('<br><br>'))

print(question[0])
