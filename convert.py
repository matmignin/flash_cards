#!/usr/bin/env python
import re

with open('patho.txt', 'r') as f:
    list_of_questions = f.read()
    convert_html = re.sub('\n', '<br>', list_of_questions)
        #replaces all the linefeeds to html linefeeds
    post_number = re.sub(r'(?<=\d)\.', '<br>', convert_html)
        #adds a new line and deletes the period after the questions number
    question = (post_number.split('<br><br>'))
        #splits the questions into a list with the coorisonding number. question [0] is the title of the file


number_of_questions = len(question) - 1
