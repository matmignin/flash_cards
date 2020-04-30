#!/usr/bin/env python
import re

with open('patho.txt', 'r') as f:
    list_of_questions = f.read()
    convert_linefeeds = re.sub('\n', '<br>', list_of_questions)
        #replaces all the linefeeds to html linefeeds
    add_linebreak = re.sub(r'(?<=\d)\.', '<br><h2>', convert_linefeeds)
        #adds a new line and deletes the period after the questions number
    convert_to_numerical_list = re.sub('a\.', '</h2><ol type="A"><br><li>', add_linebreak)
    #convert_answers_list = re.sub(r'(?<=[a-z])\.', ')<br>&nbsp;', add_linebreak)
    convert_answers_list = re.sub('<br>[b-z]\.', '</li><li>', convert_to_numerical_list)
    question= (convert_answers_list.split('<br><br>'))
        #splits the questions into a list with the coorisonding number. split_questions[0] is the title of the file


number_of_questions = len(question) - 1
